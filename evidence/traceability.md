# Registro de evidencia y límites

Corte de revisión: 2026-11-16. Los enlaces de Notion requieren los permisos de la fuente. Los resultados reportados conservan su linaje y fecha.

| Claim | Fuente y fecha | Contraste y alcance |
| --- | --- | --- |
| TRA-01 · Procedencia por claim | [Protocolo de Reconciliación Epistemológica v1](https://app.notion.com/p/3d226e56c2f781a6bd88c91f80a9346b), revisión visible 2026-09-05 | Especificación documental incorporada en la [decisión propuesta](../docs/decisions/0001-evidence-and-authority.md). |
| TSA-01 · Identidad, tipos, procedencia y ausencia | [Scope TSA](https://app.notion.com/p/3e126e56c2f781c49239ea028eefcb9c), revisión visible 2026-10-07 | La copia experimental `core.py` implementa valores tipados y composición. El gate local conserva observaciones ausentes fuera del snapshot y prueba cero como valor. El alcance del contrato TSA completo queda como especificación. |
| MEM-01 · Dos invariantes de integridad | [B-001](https://app.notion.com/p/41426e56c2f781e0af64d1012acfa30f) 2026-11-09 y [B-002](https://app.notion.com/p/41426e56c2f781aca2ecf9ae42afc7d6) 2026-11-10 | 10/10 y coincidencia Python/Go en 85 vectores, respectivamente, según Notion. Sin repetición local de esos paquetes en esta revisión. B-002 limita invariancia topológica al fixture y diferencia su firma del root sensible a IDs. Ingestión de Memory v2 y validación semántica quedan pendientes. |
| R32-01 · Autoridad conductual | [R32 v0](https://app.notion.com/p/3d526e56c2f78104b055fabffdbcffb9), 2026-09-08 | Notion registra 10/10 y 1.000/1.000 asignaciones sintéticas con deltas y acción tipada. Resultado histórico reportado. El código R110 local opera con atributos sintéticos y un orden de consulta. Los binarios históricos de R32 quedaron fuera de esta reproducción. |
| R110-01 · Coste efectivo | Paquete local R110, 2026-11-15 | En `r110_transfer.py`, S2/S3 leen valores de varias ramas antes de incrementar `asked` por la elegida. El gate instrumentado reprodujo el JSON. Con límite de una consulta, aleatorio 49/400, orden transferido 28/400 y ganancia local 43/400, con 312 consultas por brazo. Las máscaras reutilizan 16 fichas sintéticas. |
| GATE-01 · Catálogo y autoridad | Gate local de evidencia discriminante, revisado 2026-11-16 | Las 7 pruebas volvieron a pasar. Con 8 campos y máximo 2 intentos, el fixture completo dio 304 emisiones correctas y 96 HOLD. Al retirar la ficha evaluada y conservar la declaración de completitud, hubo 194 emisiones incorrectas. Con alcance abierto hubo 400 HOLD. El fixture controlado verifica el contrato. |
| NLX-01 · Límite de realización | [NLX Frozen v1](https://app.notion.com/p/3f626e56c2f7817385f8da722a60bac1) y checkpoints del 2026-10-11 | Diseño en sombra. La página registra PASS de contratos acotados y luego entrenamiento limitado de un proxy sintético. Evaluación humana externa pendiente según esos checkpoints. Su runner y sus binarios quedaron fuera de la repetición local. |
| LIT-01 · Linajes de evaluación | [SHADOW-004B](https://app.notion.com/p/3fb26e56c2f781c1b08dca79c5c31a52) y [kit LitBank](https://app.notion.com/p/3fb26e56c2f78154915eee68fbac5611), 2026-10-16. Ensayo local LitBank revisado 2026-11-16 | Notion registra 10/10 fixtures, 4/4 del harness y benchmark externo NOT RUN para el extractor histórico. El ensayo local usa otro extractor. `benchmark.py` predice desde texto tokenizado y `score.py` usa gold para puntuar. La revisión local recalculó F1 de 57,28% y 79,17% y enlaces correctos de 2.781 y 2.514 sobre 4.448, para reglas y extractor entrenado con el mismo resolver. La mejora de menciones coexistió con menor exactitud de enlace. Falta auditar solapamiento con paquetes históricos ausentes. |
| ROUTE-01 · Ruteo y backplay | [Auditoría de pipeline](https://app.notion.com/p/41a26e56c2f781b6ae7de14d01d790e7), 2026-11-16 | El reporte y el paquete local registran 128 HOLD con solo la respuesta, y 16 DERIVED y 112 HOLD tras integrar la toma y ejecutar los controles. En 16 correcciones, el vínculo pasó de DERIVED a HOLD y el despacho siguió Confirmado. |
| OPEN-01 · Reapertura | [Auditoría de pipeline](https://app.notion.com/p/41a26e56c2f781b6ae7de14d01d790e7), 2026-11-16 | De 192 casos, 128 candidatos admitidos suspendieron la derivación antes de consultar. Después hubo 32 destinos nuevos, 32 restauraciones y 64 HOLD. Las 64 observaciones restantes fueron rechazadas por firma o trayectoria. |

### Integridad de los paquetes de continuidad

En esta actualización se cotejaron los SHA-256 de los ZIP locales con los registrados en Notion. Los conteos de casos y los replays son resultados de la auditoría del 16 de noviembre.

| Paquete | SHA-256 |
| --- | --- |
| Auditoría de pipeline | `5c65a3aff9040648d5c61254d2091620c85d29aafc73778c1e414acdc8f0877e` |
| Ruteo y backplay | `f733e04683d6410612aea2cb8cab0e6f7de203cf2cb3f8d779faef0ad9fe9ffb` |
| Reapertura de candidatos | `6f2ea5910ef02cfb7aacb776eebc76a3fcd0a5e06e9b88981ff98d1e6cb56b01` |

En una extracción limpia de los paquetes, con las dependencias congeladas del banco CartPole, ejecutar `python -B -m unittest -v` y `python -B run.py` desde cada paquete. Para el gate de reapertura, ejecutar además `python -B verify.py results.json`. Las entradas, resultados y manifiestos residen en los paquetes de origen.

[Comandos, hashes y resultados de la revisión](../experiments/reproduction.md).
