# Roadmap de integración de snapshots — 26 de noviembre de 2026

Estado: sandbox finito; promoción DENIED. [Checkpoint y evidencia](../architecture/snapshot-prediction-2026-11-26.md).

| Prioridad | Trabajo | Evidencia requerida |
| --- | --- | --- |
| 1 | Ingreso semántico → tarjetas | Entidades, relaciones, negación, tiempo y citas preservados en documentos nuevos |
| 2 | Aprender transiciones y pesos | Observaciones externas, evaluación retenida, calibración y memoria de contraejemplos |
| 3 | Ampliar hipótesis disponibles | Detectar insuficiencia del modelo; contrastar nuevas relaciones sin borrar contradicciones |
| 4 | Adquirir evidencia | Herramientas de consulta, coste y dependencia de sensores; preguntas actuales solo ordenadas |
| 5 | Realizar lenguaje desde AnswerPlan | Fidelidad de cada frase a sus ramas, modalidad, tiempos y testigos |

Ya implementado: distribución conjunta, etapas compartidas, masa pendiente, preguntas bajo observación idealizada, revisión de evidencia, retiro e historial con reinicio. No usar las propias predicciones como observaciones de entrenamiento. Los 38+49 tests y 80 modelos corresponden a esta corrida local; CI remoto no ejecutado.
