# Gates de revisión técnica

| Gate | Criterio y estado al 2026-11-16 |
| --- | --- |
| Integridad y trazabilidad | Verificar versión, entradas, hash cuando exista y correspondencia claim → resultado. R110 local tiene reproducción del resultado registrado. B-001 y B-002 conservan estatus histórico reportado. |
| Adquisición comparable | Registrar todas las lecturas de valores ocultos. Simular ramas con datos de entrenamiento y revelar únicamente el atributo elegido. S2 y S3 históricos fallan el criterio de coste comparable. |
| Emisión con cobertura | Validar de forma independiente la cobertura del catálogo y la autenticidad de las mediciones. Con cobertura abierta se conserva HOLD en el gate local. La certificación externa queda pendiente. |
| Evaluación lingüística | Separar por documento, mantener gold fuera de inferencia, fijar controles y seguir detección, candidatos, enlaces end-to-end y cobertura. SHADOW-004B histórico quedó en NOT RUN externo en el checkpoint consultado. El ensayo local LitBank tiene linaje propio y usa tokenización y segmentación publicadas. |
| Realización léxica NLX | Mantener el plan y la evidencia como autoridad. El checkpoint consultado registra contrato acotado y un proxy sintético. La evaluación humana externa sigue pendiente en el material revisado. |
| Revisión de publicación | Comprobar procedencia y visibilidad antes de incorporar código, datos o citas. El alcance del PR es documental. |
| Localidad y corrección | **PASS de sandbox**. El vínculo requiere coincidencia de ruteo y respuesta. Los controles cruzados, de espejo, evidencia ausente y sobre alterado terminan en HOLD. La corrección invalida el vínculo afectado y suspende su derivación dependiente. |
| Candidatos sobre esquema conocido | **PASS de sandbox**. Un candidato compatible sin resolver suspende la derivación. La consulta posterior restablece o cambia el vínculo cuando discrimina. Espejo y ausencia de evidencia conservan HOLD. |
| Integración externa | **Pendiente**. Autenticar fuente y localidad fuera del banco, acreditar independencia y cobertura, y ejecutar la ruta de ingreso a AnswerPlan y salida verificada. |

Los dos PASS de sandbox se refieren a fixtures con telemetría de CartPole y claves, catálogo y eventos de transferencia controlados. [Auditoría de pipeline](https://app.notion.com/p/41a26e56c2f781b6ae7de14d01d790e7)

La validación externa de emisión requiere casos nuevos sellados, comparación bajo igualdad de evidencia y un umbral prospectivo de error. Las ejecuciones previas sirven como referencia histórica. [Resultados y dependencias](../../evidence/traceability.md).
