import numpy as np

np.random.seed(42)

TRAIN_ENTS  = ["ana", "luis", "pedro", "sofia"]
TEST_ENTS   = ["maria", "juan"]
UNSEEN_ENTS = ["elena", "carlos"]
TRAIN_OBJS  = ["llave", "carta", "manzana"]
TEST_OBJS   = ["libro", "moneda"]

PREPS = ["a", "de", "un", "una", "el", "la"]
VERBS = ["entrego", "dio", "envio", "recibio", "tomo"]
NEGS  = ["no"]

VOCAB = ["<PAD>", "<ENT_OOV>"] + TRAIN_ENTS + TRAIN_OBJS + PREPS + VERBS + NEGS
w2i = {w: i for i, w in enumerate(VOCAB)}

def tokenize_and_bind(sentence):
    tokens = sentence.lower().replace(".", "").split()
    ids = [w2i[t] if t in w2i else w2i["<ENT_OOV>"] for t in tokens]
    return ids, tokens

def generate_grounded_dataset(entities, objects, n_samples=600):
    data = []
    for _ in range(n_samples):
        e1, e2 = np.random.choice(entities, size=2, replace=False)
        obj = np.random.choice(objects)
        det = np.random.choice(["un", "una", "el", "la"])
        neg = np.random.rand() < 0.3
        neg_str = "no " if neg else ""
        if np.random.rand() < 0.5:
            v = np.random.choice(["entrego", "dio", "envio"])
            sent = f"{e1} {neg_str}{v} {det} {obj} a {e2}"
        else:
            v = np.random.choice(["recibio", "tomo"])
            sent = f"{e2} {neg_str}{v} {det} {obj} de {e1}"
        pol = -1.0 if neg else 1.0
        data.append((sent, (e1, e2, obj, pol)))
    return data

train_data = generate_grounded_dataset(TRAIN_ENTS, TRAIN_OBJS, n_samples=600)

V_sz = len(VOCAB)
W_slot = 0.05 * np.random.randn(V_sz, 4)        # [OTHER, ENT, VERB, NEG]
W_prep_role = 0.05 * np.random.randn(V_sz, 3)   # [ARG0, THEME, ARG2]
W_verb_persp = 0.05 * np.random.randn(V_sz, 2, 2) # [ARG0, ARG2] -> [SRC, DST]
W_pol = np.zeros(V_sz)

def softmax(x, axis=-1):
    x_m = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(x_m)
    return e / np.sum(e, axis=axis, keepdims=True)

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -15, 15)))

def forward_phi(sentence):
    ids, surfaces = tokenize_and_bind(sentence)
    slot_probs = softmax(W_slot[ids], axis=-1)
    prev_ids = [w2i["<PAD>"]] + ids[:-1]
    ctx_probs = softmax(W_prep_role[prev_ids], axis=-1)

    p_ent = slot_probs[:, 1:2]
    arg_scores = p_ent * ctx_probs
    arg_weights = arg_scores / (np.sum(arg_scores, axis=0, keepdims=True) + 1e-8)

    raw_p_verb = slot_probs[:, 2]
    p_verb = raw_p_verb / (np.sum(raw_p_verb) + 1e-8)
    M_verbs = softmax(W_verb_persp[ids], axis=1)
    M_sent = np.tensordot(p_verb, M_verbs, axes=([0], [0]))

    sem_src_dst = arg_weights[:, [0, 2]] @ M_sent
    sem_theme = arg_weights[:, 1]
    p_flip = sigmoid(W_pol[ids] - 2.0)
    pol_pred = np.prod(1.0 - 2.0 * p_flip)

    return {
        "ids": ids, "surfaces": surfaces, "prev_ids": prev_ids,
        "slot_probs": slot_probs, "ctx_probs": ctx_probs,
        "arg_weights": arg_weights, "p_verb": p_verb,
        "M_verbs": M_verbs, "M_sent": M_sent,
        "sem_src_dst": sem_src_dst, "sem_theme": sem_theme,
        "pol_pred": pol_pred, "p_flip": p_flip
    }

def compute_loss_and_grads(batch):
    dW_slot = np.zeros_like(W_slot)
    dW_prep = np.zeros_like(W_prep_role)
    dW_persp = np.zeros_like(W_verb_persp)
    dW_pol = np.zeros_like(W_pol)
    total_loss = 0.0

    for sent, (src_t, dst_t, obj_t, pol_t) in batch:
        out = forward_phi(sent)
        ids, prev_ids, surfaces = out["ids"], out["prev_ids"], out["surfaces"]
        L = len(ids)

        y_src = np.array([1.0 if s == src_t else 0.0 for s in surfaces])
        y_dst = np.array([1.0 if s == dst_t else 0.0 for s in surfaces])
        y_obj = np.array([1.0 if s == obj_t else 0.0 for s in surfaces])

        p_src = np.clip(out["sem_src_dst"][:, 0], 1e-7, 1.0)
        p_dst = np.clip(out["sem_src_dst"][:, 1], 1e-7, 1.0)
        p_obj = np.clip(out["sem_theme"], 1e-7, 1.0)
        pol_pred = out["pol_pred"]

        loss = (-np.sum(y_src * np.log(p_src)) - np.sum(y_dst * np.log(p_dst))
                - np.sum(y_obj * np.log(p_obj)) + 0.5 * (pol_pred - pol_t) ** 2)
        total_loss += loss

        d_pol_pred = (pol_pred - pol_t)
        p_flip = out["p_flip"]
        factors = 1.0 - 2.0 * p_flip
        for j in range(L):
            other_prod = np.prod(np.delete(factors, j)) if L > 1 else 1.0
            dW_pol[ids[j]] += d_pol_pred * other_prod * (-2.0) * p_flip[j] * (1.0 - p_flip[j])

        d_sem_src_dst = np.stack([-y_src / p_src, -y_dst / p_dst], axis=1)
        d_sem_theme = -y_obj / p_obj

        arg_02 = out["arg_weights"][:, [0, 2]]
        dM_sent = arg_02.T @ d_sem_src_dst
        d_arg_02 = d_sem_src_dst @ out["M_sent"].T

        d_arg_weights = np.zeros((L, 3))
        d_arg_weights[:, [0, 2]] = d_arg_02
        d_arg_weights[:, 1] = d_sem_theme

        p_ent = out["slot_probs"][:, 1:2]
        ctx_probs = out["ctx_probs"]
        arg_scores = p_ent * ctx_probs
        sums = np.sum(arg_scores, axis=0, keepdims=True) + 1e-8
        d_arg_scores = (d_arg_weights - np.sum(d_arg_weights * out["arg_weights"], axis=0, keepdims=True)) / sums

        d_p_ent = np.sum(d_arg_scores * ctx_probs, axis=1)
        d_ctx_probs = d_arg_scores * p_ent
        d_ctx_logits = ctx_probs * (d_ctx_probs - np.sum(d_ctx_probs * ctx_probs, axis=1, keepdims=True))
        for j in range(L):
            dW_prep[prev_ids[j]] += d_ctx_logits[j]

        p_verb, M_verbs = out["p_verb"], out["M_verbs"]
        d_p_verb = np.sum(M_verbs * dM_sent[None, :, :], axis=(1, 2))
        d_M_verbs = p_verb[:, None, None] * dM_sent[None, :, :]
        d_persp_logits = M_verbs * (d_M_verbs - np.sum(d_M_verbs * M_verbs, axis=1, keepdims=True))
        for j in range(L):
            dW_persp[ids[j]] += d_persp_logits[j]

        raw_p_verb = out["slot_probs"][:, 2]
        sum_v = np.sum(raw_p_verb) + 1e-8
        d_raw_p_verb = (d_p_verb - np.sum(d_p_verb * p_verb)) / sum_v

        d_slot_probs = np.zeros((L, 4))
        d_slot_probs[:, 1] = d_p_ent
        d_slot_probs[:, 2] = d_raw_p_verb
        slot_probs = out["slot_probs"]
        d_slot_logits = slot_probs * (d_slot_probs - np.sum(d_slot_probs * slot_probs, axis=1, keepdims=True))
        for j in range(L):
            dW_slot[ids[j]] += d_slot_logits[j]

    N = len(batch)
    return total_loss / N, (dW_slot / N, dW_prep / N, dW_persp / N, dW_pol / N)

lr, beta = 0.4, 0.9
v_slot, v_prep, v_persp, v_pol = [np.zeros_like(x) for x in (W_slot, W_prep_role, W_verb_persp, W_pol)]

for epoch in range(100):
    np.random.shuffle(train_data)
    for start in range(0, len(train_data), 32):
        loss, (gs, gp, gm, gpol) = compute_loss_and_grads(train_data[start:start+32])
        v_slot  = beta * v_slot  + (1 - beta) * gs;   W_slot       -= lr * v_slot
        v_prep  = beta * v_prep  + (1 - beta) * gp;   W_prep_role  -= lr * v_prep
        v_persp = beta * v_persp + (1 - beta) * gm;   W_verb_persp -= lr * v_persp
        v_pol   = beta * v_pol   + (1 - beta) * gpol; W_pol        -= lr * v_pol

def decode_H(sentence):
    out = forward_phi(sentence)
    s = out["surfaces"]
    src = s[int(np.argmax(out["sem_src_dst"][:, 0]))]
    dst = s[int(np.argmax(out["sem_src_dst"][:, 1]))]
    obj = s[int(np.argmax(out["sem_theme"]))]
    pol = +1 if out["pol_pred"] >= 0 else -1
    return (src, dst, obj, pol)

def apply_event_algebra(possession, H):
    src, dst, obj, pol = H
    if pol == 1 and (possession.get(obj) == src or obj not in possession):
        possession[obj] = dst
        return True
    return False

for label, sent in [
    ("A", "maria entrego un libro a juan"),
    ("B", "juan recibio un libro de maria"),
    ("C", "maria no entrego el libro a juan"),
    ("D", "juan entrego un libro a maria"),
    ("OOV_1", "elena entrego una moneda a carlos"),
    ("OOV_2", "carlos recibio una moneda de elena"),
]:
    print(f"{label:6s}: {sent:36s} -> H = {decode_H(sent)}")

test_unseen = generate_grounded_dataset(TEST_ENTS + UNSEEN_ENTS, TEST_OBJS, n_samples=200)
acc = sum(1 for s, g in test_unseen if decode_H(s) == g) / 200.0
print(f"Exactitud OOD entidades/objetos inéditos (N=200): {acc:.3f}")

# Composición multi-oración sobre estado algebraico
state = {}
apply_event_algebra(state, decode_H("ana entrego una llave a luis"))
apply_event_algebra(state, decode_H("luis no entrego la llave a pedro"))  # bloqueado por pol=-1
apply_event_algebra(state, decode_H("luis entrego la llave a carlos"))
print("Estado compuesto final:", state)

