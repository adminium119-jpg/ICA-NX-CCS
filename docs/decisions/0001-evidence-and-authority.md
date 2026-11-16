# ADR 0001 · Trazabilidad y autoridad

Fecha: 2026-11-16  
Estado: propuesta para revisión

## Contexto

Los registros históricos mezclan diseño, resultados documentados, verificaciones de contrato y decisiones de alcance. Hay nombres reutilizados entre experimentos y artefactos con disponibilidad diferente.

## Decisión propuesta

Registrar cada claim con fuente, fecha, estatus histórico, evidencia contrastada, alcance y pendiente. Mantener el resultado de una reproducción separado del resultado reportado. Registrar un reemplazo como evento de supersesión con su propio alcance. Un recálculo de métricas conserva la procedencia de las predicciones y el gold usados.

Se consideró trasladar páginas o paquetes completos. El resumen por claim reduce la exposición y permite revisar cada vínculo. Los identificadores técnicos y fechas son públicos en este registro. El registro enlaza las páginas técnicas de Notion con sus permisos de origen. Los adjuntos y las referencias sensibles quedan bajo control del proyecto.

## Consecuencias

Un veredicto aplica a su protocolo y población. Una prueba contractual puede verificar el comportamiento frente a un fixture sin certificar el dominio. Las promociones requieren una decisión de autoridad independiente de este PR. Las fuentes documentales internas se pueden auditar con su registro de procedencia.

El cierre R58 documenta Semantic Core 0.9.7 congelado, runtime 18.1 y Bridge 13.4 como único Bridge canónico en su corte. La auditoría del 16 de noviembre mantiene esa frontera y ubica sus nuevas ejecuciones en sandbox. La incorporación o promoción de un componente requiere evidencia específica del gate y una decisión registrada por la autoridad del proyecto. [Cierre de autoridad R58](https://app.notion.com/p/3d626e56c2f781f3a528c8fa3acbdd94) · [Auditoría de pipeline](https://app.notion.com/p/41a26e56c2f781b6ae7de14d01d790e7)
