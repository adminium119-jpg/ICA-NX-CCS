# ICA-NX-CCS

Índice de ingeniería para especificaciones y experimentos reproducibles de NX-CCS. El repositorio se inicia como espacio de documentación. El código experimental entra por revisión con procedencia y alcance explícitos.

## Estado verificado — 26 de noviembre de 2026

[Predictor de snapshots y array multietapa](docs/architecture/snapshot-prediction-2026-11-26.md): estados conjuntos correlacionados, etapas tipadas, masa pendiente y memoria revisable. 38 pruebas nuevas y 49 de regresión; contraste con un enumerador separado en 80 modelos pequeños. [Resultados](evidence/snapshot-results-2026-11-26.json) · [Roadmap](docs/roadmap/snapshots-2026-11-26.md).

Relaciones y pesos declarados; aprendizaje desde evidencia externa, integración del ingreso semántico y adquisición externa siguen pendientes. Publicación documental, sin cambio al Core ni promoción. Los ensayos históricos se conservan con sus fechas y alcance.

## Organización

| Ruta | Contenido |
| --- | --- |
| `docs/architecture/` | Componentes, flujos de datos, fronteras de autoridad y mapa entre diseño e implementación. |
| `docs/contracts/` | Entradas, salidas, invariantes, condiciones de fallo y compatibilidad de versiones. |
| `docs/decisions/` | Decisiones con fecha, contexto, estado, alternativas y consecuencias. Conservar el historial de supersesión. |
| `docs/gates/` | Dependencias, criterios prospectivos, controles, condiciones de parada y veredicto por alcance. |
| `experiments/` | Protocolo por experimento, configuración, partición y comando de reproducción. |
| `evidence/` | Índice de claims, resultados, trazas autorizadas, hashes y límites. |
| `src/` y `tests/` | Código y pruebas autorizados, incorporados juntos cuando corresponda. |

Cada ruta se materializa al incorporar su primer documento o artefacto. Para cada claim, registrar identificador, fecha y estado original, revisión o artefacto identificable, evidencia, alcance y pendiente. Enlazar el protocolo con el código, el resultado y el gate. Si la fuente es restringida, usar un identificador estable y conservar la correspondencia bajo acceso restringido.

## Estados y revisión

Distinguir especificación, hipótesis, decisión, observación de código, resultado reportado y resultado reproducido. Un resultado reproducido declara entradas, versión, comando, salida y diferencias. Un gate conserva su fecha y dominio. Un PASS contractual solo cubre las condiciones ensayadas. Un ensayo pendiente se registra como NOT RUN. Si falta evidencia para decidir, conservar HOLD y el requisito que permitiría resolverlo.

Las propuestas se revisan por PR. Publicar únicamente material técnico autorizado para este repositorio público. Excluir datos privados, identificadores de acceso, adjuntos restringidos y material sensible de ramas fuera de alcance. Una revisión documental carece de autoridad para modificar el Core canónico o efectuar promociones, que requieren su propio proceso.
