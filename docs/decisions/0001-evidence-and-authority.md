# ADR 0001 · Trazabilidad y autoridad

Fecha: 2026-11-16  
Estado: propuesta para revisión

## Contexto

Los registros históricos mezclan diseño, resultados documentados, verificaciones de contrato y decisiones de alcance. Hay nombres reutilizados entre experimentos y artefactos con disponibilidad diferente.

## Decisión propuesta

Registrar cada claim con fuente, fecha, estatus histórico, evidencia contrastada, alcance y pendiente. Mantener el resultado de una reproducción separado del resultado reportado. Registrar un reemplazo como evento de supersesión con su propio alcance. Un recálculo de métricas conserva la procedencia de las predicciones y el gold usados.

Se consideró trasladar páginas o paquetes completos. El resumen por claim reduce la exposición y permite revisar cada vínculo. Los identificadores técnicos y fechas son públicos en este registro. La correspondencia a páginas restringidas queda en el registro local de procedencia bajo control del proyecto.

## Consecuencias

Un veredicto aplica a su protocolo y población. Una prueba contractual puede verificar el comportamiento frente a un fixture sin certificar el dominio. Las promociones requieren una decisión de autoridad independiente de este PR. Las fuentes documentales internas se pueden auditar con su registro de procedencia.
