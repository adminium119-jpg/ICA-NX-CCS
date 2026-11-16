# Reproducción del contraste

Revisión local realizada el 2026-11-16 con Python 3.12.14. Los comandos parten de las copias de trabajo de los paquetes del proyecto. El repositorio público aloja la documentación de revisión. Las rutas a continuación se resuelven al extraer los paquetes correspondientes en el entorno del proyecto.

| Paquete o carpeta local | Comando | Resultado de esta revisión |
| --- | --- | --- |
| `nxccs-evidence/` | `python -B reproduce.py` | Manifiesto verificado, 3 comprobaciones de sanidad y 5 pruebas del gate, ejecución histórica y coincidencia exacta del JSON registrado del gate. |
| `nxccs-decision-gate/` | `python -B -m unittest -v test_gate` | 7 pruebas PASS. Incluye rechazo, presupuesto y evaluación exhaustiva del fixture. |
| `nxccs-followup/` | `python -B -m unittest -v test_run` | 2 pruebas PASS. Incluye presupuesto, ganancia y techo de identificabilidad en el fixture. |
| `nxccs-litbank/` | `python -B -m unittest -v test_benchmark` | 3 pruebas PASS. Incluye integridad, separación documental y completitud de preguntas. |
| Copia temporal de `nxccs-litbank/` | `python -B score.py` y `python -B questions.py score` | Coincidencia SHA-256 de ambos JSON de métricas a partir de las predicciones conservadas. Entrenamiento, inferencia y servidor LLM quedan fuera de este recálculo. |

Identificación de paquetes de evidencia por SHA-256 calculado localmente:

| Paquete | SHA-256 |
| --- | --- |
| R110, 2026-11-15 | `bc93f7f931a8ba178654a7dd92eb9fdf3980510df8ae2973c59bee48696a57bb` |
| LitBank y comparación acotada | `cc34f81b245133cd63bfe13189b7db95a714ca5683007c4fcf901c433bb336bb` |
| Gate de evidencia discriminante | `8fe56168b0bf6d31c1f1016072b8f9edd965de2e57b4cf48d3c686b27591f607` |
