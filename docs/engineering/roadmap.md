# Alcances y roadmap de ingeniería de NX-CCS

Corte de auditoría del 19 de noviembre de 2026. Este documento organiza el trabajo de ingeniería experimental. El estado de referencia documentado es Core 0.9.7, runtime 18.1, Bridge 13.4 y State/Authority Map v25. Cualquier cambio de autoridad requiere su propia revisión.

## Alcances

| Alcance | Evidencia | Límite |
| --- | --- | --- |
| Custodia y reproducción | 14 replays locales pasaron. Cuatro ensayos regeneraron sus JSON archivados. | El piloto asistido y los cinco adjuntos fuente de R110 quedan pendientes de cotejo. |
| Inferencia, identidad y backplay | El banco simulado conecta CartPole con observación de ruteo, derivación, corrección y verificación. | Las claves, el catálogo y los eventos de transferencia pertenecen al fixture. |
| Mundo abierto y adquisición | Se reprodujeron la reapertura de inferencias y la selección de mediciones bajo presupuestos sintéticos. | Falta conectar las observaciones alternativas a adaptadores ejecutables y verificar cobertura y procedencia en la ruta integrada. |
| Lenguaje | Se reprodujo el tramo archivado de LitBank con respuestas de Qwen conservadas. | La prueba externa SHADOW-004B y el adaptador hacia AnswerPlan están pendientes. |
| CLR histórico | Integridad y agregados reproducidos desde 576 casos y 4.608 controles. | El ZIP de resultados carece del ejecutor original para regenerar las predicciones. |

## Orden de ejecución y criterios de salida

| Orden | Trabajo | Criterio de salida |
| --- | --- | --- |
| P0 | Completar custodia de los insumos activos. Conservar manifiestos, revisiones y hashes. | Cada dependencia crítica tiene bytes verificados o un faltante explícito. Las copias se cotejan por contenido. |
| P1 | Versionar el contrato de observación entre adaptadores y motor. Incluir identidad, ventana, fuente, origen compartido, tipo, unidad, alternativas y revocación. | Pruebas aceptan la observación válida, rechazan alteraciones y conservan HOLD ante procedencia o cobertura insuficiente. |
| P2 | Conectar las mediciones alternativas al banco. Comparar políticas con entradas y presupuesto iguales. | Registrar la medición comprada, el coste lógico y las hipótesis supervivientes. Reproducir controles de espejo, ruteo cruzado, evidencia ausente y corrección localizada. |
| P3 | Conectar el tramo de lenguaje al motor y a AnswerPlan. Congelar corpus, partición y controles antes de medir. | Desde una fuente nueva, guardar trazas de ingreso, abstención o respuesta, verificación y replay. Reportar cobertura y errores por etapa. |
| P4 | Revisar la evidencia y decidir si corresponde proponer cambios de autoridad. | Decisión explícita con evidencia, alcance y límites. |

## Auditoría de fuentes

El barrido de Drive enumeró carpetas y metadatos. Las coincidencias de nombre y tamaño indican posibles duplicados. El cruce de Notion se hizo por secciones indexadas y contra copias locales previas. La comprobación de bytes se limita a los paquetes con un digest de origen disponible.
