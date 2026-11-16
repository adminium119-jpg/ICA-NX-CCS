# ICA-NX-CCS

Índice de ingeniería para especificaciones y experimentos reproducibles de NX-CCS. El repositorio se inicia como espacio de documentación. El código experimental entra por revisión con procedencia y alcance explícitos.

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

Cada ruta se materializa al incorporar su primer documento o artefacto. Para cada claim, registrar identificador, fecha y estado original, revisión o artefacto identificable, evidencia, alcance y pendiente. Enlazar el protocolo con el código, el resultado y el gate. Referenciar las páginas técnicas de Notion sujetas a permisos cuando proceda y mantener los adjuntos y referencias sensibles bajo acceso restringido.

## Documentos de ingeniería

- [Arquitectura ICA, CSC, CLR y TSA](docs/architecture/overview.md)
- [Contratos de estado y evidencia](docs/contracts/typed-evidence.md)
- [Gates y criterios de salida](docs/gates/review.md)
- [Evidencia, hashes y fuentes de Notion](evidence/traceability.md)
- [Protocolos de reproducción](experiments/reproduction.md)
- [Decisión sobre trazabilidad y autoridad](docs/decisions/0001-evidence-and-authority.md)

## Estados y revisión

Distinguir especificación, hipótesis, decisión, observación de código, resultado reportado y resultado reproducido. Un resultado reproducido declara entradas, versión, comando, salida y diferencias. Un gate conserva su fecha y dominio. Un PASS contractual solo cubre las condiciones ensayadas. Un ensayo pendiente se registra como NOT RUN. Si falta evidencia para decidir, conservar HOLD y el requisito que permitiría resolverlo.

Las propuestas se revisan por PR. Publicar únicamente material técnico autorizado para este repositorio público. Excluir datos privados, identificadores de acceso, adjuntos restringidos y material sensible de ramas fuera de alcance. Una revisión documental carece de autoridad para modificar el Core canónico o efectuar promociones, que requieren su propio proceso.
