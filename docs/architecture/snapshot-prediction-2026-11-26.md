# NX-CCS — Predicción de snapshots y array multietapa

Actualización: 26 de noviembre de 2026. Estado: sandbox experimental, sin promoción al Core.

La unidad de inferencia es un estado conjunto tipado. Las etapas comparten una asignación del mundo y sus causas; el texto puede expresar después sus conclusiones. Coherencia, verificación de cálculo y corroboración permanecen separadas.

## Implementado

- Red condicional finita con fracciones exactas, padres compartidos y deduplicación por linaje.
- Búsqueda por prefijos con masa pendiente; sin renormalizar solo lo visitado como si fuera exhaustivo.
- Etapas dimensionales y booleanas conectadas, con restricciones refutadas y resultados sin resolver visibles.
- Snapshots alternativos con entidad, relación y tiempo; preguntas ordenadas por información esperada bajo observación idealizada.
- SQLite con versiones de modelos/evidencia, revisión esperada, retiro y cadena de hashes; replay actual tras reinicio.

## Comprobado en esta iteración

| Comprobación | Resultado | Alcance |
| --- | --- | --- |
| Pruebas nuevas | 38/38 | Esquema finito, contexto, masa, tipos y memoria |
| Regresión de candidatos | 15/15 | Módulo previo |
| Regresión de habilidades/memoria | 34/34 | Módulo previo |
| Referencia cartesiana de OpenCode | 80 modelos concordantes | Masas conjuntas y normalizador, mundos de prior positivo |
| Ensayo de reinicio | Hash actual idéntico | Modelo y evidencia declarados |

Hermes entregó H1/H2: contrato y cotas, después revisión matemática. OpenCode entregó O1/O2: referencia independiente por enumeración cartesiana, después auditoría estática. El ingeniero principal ejecutó pruebas y corrigió hallazgos. Cuatro entregas CLI completadas; no se presentan como procesos que continúan activos ni como independencia estadística garantizada.

## Casos

Cocina → posible propagación al garaje → exposición e ignición de llanta → posible daño al vehículo. La revisión del paso cerrado a abierto recalcula las ramas y retira el resultado anterior. Daño no equivale a combustión de todo el vehículo. Las CPT son supuestos sintéticos, no frecuencias físicas ni asesoramiento de incendios.

Causa común → distancia y tasa de consumo → energía/duración → viabilidad. El cálculo evita inventar combinaciones entre marginales incompatibles y permite que una observación actualice una causa compartida. Dos lecturas del mismo sensor conservan un único factor de ruido cuando se declara ese padre latente.

## Pendientes priorizados

1. Conectar ingreso semántico con las tarjetas sin perder citas, negación, identidad ni tiempo.
2. Aprender propuestas de transición y pesos con observaciones externas y evaluación retenida; nunca etiquetar como observación la propia predicción.
3. Detectar que ninguna hipótesis disponible explica la evidencia y contrastar ampliaciones del esquema.
4. Conectar preguntas con adquisición externa, coste y modelo de fiabilidad del sensor.
5. Generar un AnswerPlan expresivo y verificar cada realización lingüística contra ramas y testigos.

## Alcance y autoridad

Probabilidades exactas bajo la factorización declarada, sin calibración empírica establecida. Más de una observación exige declarar su factorización; orígenes distintos no demuestran independencia. Las restricciones son diagnósticas, sin eliminación o renormalización silenciosa. Hay límites lógicos de trabajo; no son límites duros de RSS o tiempo. No es todavía comprensión libre, aprendizaje abierto general o paridad con un LLM.

CSC v1.3 conserva 7 × 3 × 7 × 8, capas Cell/MesoCell/Cluster y write_class independiente. Runtime documental 18.1 y Bridge 13.4_ONLY intactos; promoción DENIED.

## Evidencia y reproducción

Código y pruebas en el PC: `C:/NX-CCS/ingenieria/array-multietapa-v1/`.

```powershell
python -B -X utf8 -m unittest -v test_array
python -B -X utf8 demo.py runs/otra-corrida
```

Usar una carpeta nueva para preservar el historial. Dependencia local: VM de `competencia-integrada-v1`. El ZIP conserva la disposición del sandbox; para reproducir desde cero también se requiere esa dependencia, no incluida en este paquete de módulo. Publicación documental en GitHub no equivale a ejecución de CI.

[Paquete original de módulo en Drive](https://drive.google.com/file/d/1KFugp0Bu_FkUyBtpyCcF0rq-Gz9PkbAm/view?usp=drivesdk). SHA-256: `012c6ac82d120a30367001f5ed5c662b2978c98c9718f3cd0b0e7f4be5e881da`. [Contexto compartido en Drive](https://docs.google.com/document/d/1G4Vah7KvjqDQ_bnA4whc5fTtXfRgYGhSKTj2rzOrrJc/edit). Los hashes establecen integridad, no verdad o autenticidad de fuentes. El ZIP original permanece sin cambios.
