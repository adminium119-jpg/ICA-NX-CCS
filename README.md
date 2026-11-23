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

Cada ruta se materializa al incorporar su primer documento o artefacto. Para cada claim, registrar identificador, fecha y estado original, revisión o artefacto identificable, evidencia, alcance y pendiente. Enlazar el protocolo con el código, el resultado y el gate. Si la fuente es restringida, usar un identificador estable y conservar la correspondencia bajo acceso restringido.

## Estados y revisión

Distinguir especificación, hipótesis, decisión, observación de código, resultado reportado y resultado reproducido. Un resultado reproducido declara entradas, versión, comando, salida y diferencias. Un gate conserva su fecha y dominio. Un PASS contractual solo cubre las condiciones ensayadas. Un ensayo pendiente se registra como NOT RUN. Si falta evidencia para decidir, conservar HOLD y el requisito que permitiría resolverlo.

Las propuestas se revisan por PR. Publicar únicamente material técnico autorizado para este repositorio público. Excluir datos privados, identificadores de acceso, adjuntos restringidos y material sensible de ramas fuera de alcance. Una revisión documental carece de autoridad para modificar el Core canónico o efectuar promociones, que requieren su propio proceso.

## Checkpoint experimental del 23 de noviembre de 2026

- [Estado y límites](docs/checkpoints/2026-11-23.md)
- [Roadmap y gates propuestos](docs/roadmap/2026-11-23.md)
- [Revisión contrastada de Gemini](docs/reviews/gemini-2026-11-23.md)
- [Métricas curadas del gate](evidence/2026-11-23/summary.json)

Estado de autoridad: HOLD. La evidencia completa permanece en el archivo experimental privado. Este checkpoint contiene documentación y métricas curadas.
