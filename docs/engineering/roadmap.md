# Alcances y roadmap de ingeniería de NX-CCS

Corte de auditoría del 19 de noviembre de 2026. Este documento organiza el trabajo de ingeniería experimental. El estado de referencia documentado es Core 0.9.7, runtime 18.1, Bridge 13.4 y State/Authority Map v25. Cualquier cambio de autoridad requiere su propia revisión.

## Alcances

| Alcance | Evidencia | Límite |
| --- | --- | --- |
| Custodia y reproducción | 14 replays locales pasaron. Cuatro ensayos regeneraron sus JSON archivados. | El cotejo posterior verificó los cinco adjuntos de R110 y los 101 objetos de custodia del piloto asistido. |
| Inferencia, identidad y backplay | El banco simulado conecta CartPole con observación de ruteo, derivación, corrección y verificación. | Las claves, el catálogo y los eventos de transferencia pertenecen al fixture. |
| Mundo abierto y adquisición | Se reprodujeron la reapertura de inferencias y la selección de mediciones bajo presupuestos sintéticos. | Falta conectar las observaciones alternativas a adaptadores ejecutables y verificar cobertura y procedencia en la ruta integrada. |
| Lenguaje | Se reprodujo el tramo archivado de LitBank con respuestas de Qwen conservadas. | Una ruta de texto controlado ya llega a AnswerPlan. La recuperación de texto libre y la prueba externa SHADOW-004B siguen abiertas. |
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

## Checkpoint de paridad y próximo gate

Corte del 19 de noviembre de 2026. Alcance experimental. Se mantiene la autoridad documentada de Core 0.9.7, runtime 18.1, Bridge 13.4 y State/Authority Map v25.

### Ejecución verificada

OpenCode y Hermes completaron la segunda anotación ciega por medio de ChatGPT con modelos distintos. OpenCode usó GPT-6.1 Terra y Hermes GPT-6 Sol. GPT-6.2 Sol revisó por separado 27 citas literales sin acceso al gold. Los pasajes, las ocurrencias X/Y, la división de 8 casos de validación y 16 de test y el criterio de emisión se congelaron antes de puntuar. Este es un piloto de candidatos suministrados en documentos de GAP distintos de los del primer piloto.

| Brazo | Elección correcta en test | NONE correctos |
| --- | ---: | ---: |
| Ranker local de CCS | 6/16 | 0/8 |
| OpenCode | 10/16 | 5/8 |
| Hermes | 11/16 | 5/8 |
| Jev 1.13 Free | 12/16 | 6/8 |

OpenCode y Hermes coincidieron en 14/16 decisiones. La revisión semántica dejó 2 errores en 7 enlaces de OpenCode frente a 3 en 8 sin ese filtro, y 3 en 7 para Hermes frente a 4 en 10. El objetivo predefinido exigía al menos cuatro enlaces y un máximo de 15 % de error. Ningún brazo pasó el criterio de emisión en test. El estado sigue en **HOLD**. Dos ejecuciones del scorer sobre las mismas trazas produjeron el mismo SHA-256: `060880d66ac45e6b8549e3d93be75cda301c17784260ed71e25ad9410ae27ea1`.

### Próximo gate

1. **Respaldo por ocurrencia.** Verificar una relación explícita entre la mención exacta y el pronombre. Distinguir cita literal, soporte semántico, procedencia compartida, contradicción y cobertura. Revisar por separado los casos Q18 y Q23 del piloto que tienen posibles discrepancias de etiqueta.
2. **Cobertura prospectiva.** Congelar documentos fuera de los pilotos e incluir omisiones naturales y menciones espurias con cardinalidad comparable. Fijar tamaño mínimo, límite de error y métricas por documento antes de evaluar. Medir recuperación, falsos enlaces en NONE y rendimiento a igual riesgo.
3. **Integración de extremo a extremo.** Llevar el verificador al recorrido de texto libre a AnswerPlan y al backplay transaccional. Comparar CCS y un LLM de versión fijada con la misma evidencia y el mismo presupuesto. Comparar con Jev en el tramo de juicios tipados. El gate actual mide selección y respaldo en un banco pequeño.

[Corpus GAP](https://github.com/google-research-datasets/gap-coreference) · [API System One de Jev](https://opencode.ai/docs/console/models/#jev)
