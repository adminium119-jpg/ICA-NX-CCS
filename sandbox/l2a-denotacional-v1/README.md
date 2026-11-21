# NX-CCS · L2A experimental · 21 de noviembre de 2026

## Ejecución comprobada

Se extrajo y ejecutó el script NumPy del adjunto. Reprodujo 200/200 en el test sintético y el estado final llave=carlos. El entrenamiento utiliza objetivos explícitos de origen, destino, objeto y polaridad.

Se ejecutó experiment.py con tres brazos, reglas, supervisión de roles y aprendizaje denotacional por EM exacto sobre 12 programas candidatos. Los tres comparten 80 observaciones y el mismo ejecutor. El brazo denotacional recibe menciones, construcción superficial, estado anterior y posterior en entrenamiento. No recibe gold_program. En evaluación produce predicciones antes de compararlas con el estado posterior reservado.

| Brazo | Nuevas entidades | Modificador añadido |
| --- | --- | --- |
| Reglas | 80/80 | 80/80 |
| Roles supervisados | 80/80 | 80/80 |
| Denotacional | 80/80 | 80/80 |

El denotacional conserva seis programas equivalentes sobre las observaciones sin cambio, 40/80 casos. Los otros 40 admiten un programa. Los 20 casos con verbo desconocido quedan HOLD. Borrar las etiquetas del entrenamiento conserva el ajuste denotacional. Entidades train/test disjuntas. La pérdida media pasó de 1,589 a 0 en el conjunto de entrenamiento.

## Alcance

El ensayo comprueba selección de programas desde transiciones dentro de un lenguaje de operadores predefinido y retención de alternativas indistinguibles. Las menciones de entidades y el identificador de construcción se entregan estructurados. Añadir hoy deja esos campos iguales, por lo que ese control verifica invariancia del ejecutor y requiere un parser aprendido para evaluar robustez lingüística. El inventario de programas y el ejecutor están escritos a mano. La negación usa ausencia de cambio en un micromundo cerrado por diseño. El resultado no establece semántica general de negación en observaciones parciales. Los tres brazos empatan. Se igualaron observaciones, con presupuestos de cómputo distintos. Falta comparación neuronal de presupuesto equivalente.

## Reproducción local

Directorio C:/NX-CCS/ingenieria/l2a-denotacional-v1.
Python 3.14 del entorno aislado .venv. NumPy 2.5.5 instalado únicamente en ese entorno para el script original.

Ejecutar .venv/Scripts/python.exe -B original_numpy.py y .venv/Scripts/python.exe -B experiment.py.

## Gate pendiente

Aprender la extracción de construcción y menciones desde texto, añadir observación parcial y ejecutar particiones por familia sintáctica con semillas múltiples. Conservar alternativas y contrastarlas en estados iniciales discriminantes antes de emitir CandidateDelta. Publicación tipada y multinodo siguen pendientes de integración.
