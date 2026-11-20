# NX-CCS · Revisión de ingeniería del 20 de noviembre de 2026

**Dictamen experimental.** La capacidad mejor respaldada es reconstruir decisiones tipadas y abstenerse cuando la evidencia estructurada resulta insuficiente. La prioridad es comprobar que cada afirmación emitida conserva cobertura, identidad y procedencia al pasar del motor al texto.

**Evidencia por línea.** El roadmap registra 3.395 antecedentes recuperados entre 4.448 consultas LitBank. En GAP el error entre emisiones llegó al 38,5 %. Conviene medir recuperación de candidatos y error condicional por separado. El corpus TSA 147×8 cubre aritmética, álgebra y física sintéticas. En R110 las cuatro políticas obtuvieron 5/16 en la corrida principal. En el ensayo multicapa, sobre 196 casos, la vista local acertó 45 y la tipada 112. La agregación central y la permutación fija también acertaron 112. Sigue abierta la ventaja específica de la topología.

**Ejecución y límites.** El replay IPC reprodujo 196 casos y descartó 195 respuestas obsoletas en el ensayo de recuperación. El fallo ocurrió en un punto instrumentado. Quedan pendientes la pérdida imprevista del worker y el reinicio del coordinador tras persistir. Hermes verificó siete pruebas sintéticas de incertidumbre. La auditoría del código identificó que validate_plan consulta oracle_pass, calculado a partir del resultado esperado del fixture. La validación de publicación sigue abierta.

**Cambios de ingeniería propuestos, por orden.**

1. Separar la decisión de publicación del evaluador de pruebas. Admitir un AnswerPlan desde un snapshot vigente, con candidato único, unidad, ámbito, revisión y raíces verificadas. Borrar o permutar las etiquetas de evaluación debe conservar cada decisión.
2. Incorporar linaje de fuentes y cobertura explícita. Probar dos alias con una raíz común, dos fuentes independientes, dos candidatos compatibles y ausencia del candidato correcto. Registrar la razón de HOLD. Una corrección debe invalidar únicamente los planes dependientes.
3. Probar texto nuevo con partición por documento y familia. Congelar umbrales en validación y comparar cobertura a igual error con el agregador central y un modelo de referencia. Conservar ejemplos de afirmaciones correctas, falsas y omitidas.
4. Probar recuperación desde un registro durable y duplicación de respuestas tras commit. Medir lotes de 128, 512 y 4.096 estados con igual trabajo útil. La compra de hardware depende del rendimiento, memoria y latencia medidos.

**Alcance.** Revisión de los índices, roadmap y evidencia local de las líneas anteriores. Los resultados numéricos proceden de los registros de los ensayos. Las propuestas quedan en sandbox, pendientes de implementación y verificación.
