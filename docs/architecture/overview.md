# Arquitectura de ingeniería

El Mapa Maestro sitúa los principios en CCF, los mecanismos en ICA y el software experimental en NX-CCS. Las decisiones de ingeniería se apoyan en evidencia con alcance explícito. [Mapa Maestro](https://app.notion.com/p/39226e56c2f781d2947bfde626156ac1)

La arquitectura documental distingue representación de estado, adquisición de evidencia, decisión y realización lingüística. Cada paso conserva su ámbito y su procedencia.

| Frontera | Diseño y alcance comprobado |
| --- | --- |
| Representación TSA | Tipos e identidad explícitos, relaciones con procedencia, snapshots versionados y operaciones compatibles por firma. El contrato es conceptual. La copia experimental v3 contiene valores tipados y composición de diccionarios de dimensiones. |
| Adquisición y decisión | Un snapshot parcial entra al comparador. Un canal valida cada consulta antes de revelar un valor. El gate experimental puede pedir evidencia, abstenerse o emitir dentro de un catálogo declarado completo para el ensayo. |
| Realización NLX | El diseño alimenta un realizador con un plan de respuesta tipado y autorizado. Las sugerencias de superficie pasan por verificación contra el plan. El ingreso semántico de texto externo tiene su propia evaluación. |
| Autoridad canónica | Los experimentos son de lectura o sandbox. Core, runtime, Bridge, CSC y ontología quedan fuera del flujo de escrituras de este repositorio documental. |

Flujo de referencia: observación tipada → snapshot parcial → hipótesis compatibles → consulta, HOLD o emisión acotada. Una emisión verificada puede alimentar un plan de respuesta. La verificación de un hash comprueba integridad respecto de una referencia y requiere un ancla de confianza para atribuir autoridad.

Fuentes y estados en [el índice de evidencia](../../evidence/traceability.md).

## CSC y CLR

El CSC representa el estado estructurado en la especificación histórica. CLR define interfaces sucesivas para traducir entrada en un delta propuesto, seleccionar hipótesis, evaluar el estado, decidir y observar el resultado antes de renderizar. El orden especificado es ESS → HL → ERE+CAL → CE → RVL → TO+OL → Observer → Renderer. [Pipeline Spec v1.0](https://app.notion.com/p/38826e56c2f781a2a96ccedd45af2cb5)

La auditoría de conjunto traza correspondencias funcionales entre ese flujo y los prototipos de ingreso, adquisición, identidad, composición y backplay. Sigue pendiente demostrar el binding de su adyacencia al CSC 147×8. La integración ejecutada va de CartPole y la toma de despacho a evidencia del vínculo, reevaluación y snapshots verificables. El adaptador del grafo a AnswerPlan y la ejecución común desde fuente externa hasta respuesta siguen pendientes. [Auditoría de pipeline](https://app.notion.com/p/41a26e56c2f781b6ae7de14d01d790e7)
