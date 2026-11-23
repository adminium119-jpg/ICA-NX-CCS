# NX-CCS · Evaluación de una interfaz de decisiones tipadas

**Veredicto: HOLD para adoptar los predictores evaluados.** Se ejecutaron tres brazos sobre las mismas oraciones y opciones de WinoGrande 1.1: regla de recencia, clasificador logístico local y Qwen2.5-0.5B-Instruct Q4_K_M con lectura de probabilidades de un token. El tercer brazo ensaya el patrón de preguntas de elección tipadas. Jev comercial queda fuera de la medición. La regla es un comparable acotado del componente local de CCS, no un resultado del pipeline completo.

| Evaluación sin umbral | Regla CCS | Ranker logístico | Qwen tipado |
|---|---:|---:|---:|
| Antecedente correcto, dos candidatos más NONE | 66/128 | 67/128 | 25/128 |
| Detectó NONE tras quitar el candidato correcto | 3/128 | 128/128 | 37/128 |
| Identificó al candidato correcto cuando era el único disponible más NONE | 123/128 | 0/128 | 89/128 |
| Conservó la misma elección semántica al invertir las opciones | 128/128 | 128/128 | 65/128 |
| Brier en ejemplos originales, menor es mejor | 0,641 | 0,526 | 0,682 |

El ranker logístico aprendió un atajo por número de opciones. Su Brier de 0,000098 en las retiradas se desploma como evidencia de cobertura al ejecutar el control con un candidato correcto y el mismo número de opciones. Qwen tipado tuvo 31/128 aciertos con el orden invertido y cambió de respuesta en 63/128 pares. Los tres brazos quedaron sin un umbral que lograra como mínimo ocho emisiones y como máximo 15 % de error empírico en calibración. Se congeló HOLD para todos. Cero emisiones correctas o erróneas en ese régimen significan cero cobertura.

Se usaron 1.600 ejemplos de entrenamiento, 80 de calibración y 128 de evaluación, separados por ID y oración normalizada. Calibración y evaluación salen de la validación pública, no del test oficial. Las variantes provienen de los mismos 128 casos de evaluación. Las opciones candidatas se suministran y no se extrajeron del texto. La exposición del modelo preentrenado al corpus no es conocida. La latencia HTTP mediana local fue de aproximadamente 268 ms por solicitud tipada con dos solicitudes concurrentes en CPU. No se midió Jev, ni se comparó su precio o latencia.

## Decisión de arquitectura

Conservar el contrato de opciones identificadas y probabilidades auditables para prefiltros o priorización. Mantener HOLD/Confirmado bajo reglas de evidencia, con elección invariante al permutar opciones, controles de cobertura que balanceen cantidad de alternativas y un calibrador validado antes de emitir. La siguiente iteración debe entrenar las opciones NONE y candidato único correcto de forma contrabalanceada, con negativos plausibles sin señales de formato y evaluación sobre una partición nueva. Este resultado no autoriza promoción ni una conclusión sobre Jev.

## Fuentes y reproducción

- [WinoGrande, fuente de AllenAI](https://github.com/allenai/winogrande) · [Publicación](https://cdn.aaai.org/ojs/6399/6399-13-9624-1-10-20200517.pdf)
- [Interfaz de Jev](https://docs.typesafe.ai/introduction) · [Modelo Qwen utilizado](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF)
- Qwen GGUF revisión 9217f5db79a29953eb74d5343926648285ec7e67, SHA-256 74a4da8c9fdbcd15bd1f6d01d621410d31c6fc00986f5eb687824e7b93d7a9db. Servidor llama.cpp b12428 y Python 3.12.

Con llama-server escuchando en 127.0.0.1:18761 y el GGUF cargado:

~~~text
python -B prepare.py
python -B predict.py fit
python -B predict.py cal
python -B score.py calibrate
python -B predict.py test
python -B count_control.py
python -B predict.py count
python -B score.py evaluate
python -B -m unittest -v
~~~

El paquete completo conserva solicitudes, gold separado, modelo local, predicciones y hashes. La puntuación se puede reproducir con las predicciones archivadas sin volver a llamar al modelo.
