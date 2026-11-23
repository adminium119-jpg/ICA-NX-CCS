# Decisiones tipadas para NX-CCS

Usar WinoGrande 1.1 (AllenAI) como tarea de selección con candidatos suministrados. Usar 1.600 ejemplos de train_m para el control entrenado, 80 ejemplos de la partición oficial de validación para calibración y 128 para evaluación. Seleccionar por hash de ID con sal fija, eliminar oraciones duplicadas normalizadas y congelar los identificadores. Mantener el gold fuera del archivo de solicitudes. El test de este experimento es una partición de la validación pública; no es el test oficial de WinoGrande.

Todos los brazos reciben la misma oración, las mismas opciones y la opción NONE cuando ninguna opción completa el sentido. Comparar CCS por reglas de recencia/antecedente, un ranker logístico local y Qwen2.5-0.5B-Instruct Q4_K_M con lectura de probabilidades de un solo token restringido. El backend Qwen representa el patrón de una interfaz de decisión tipada. Jev comercial y su entrenamiento quedan fuera de este ensayo.

En calibración y evaluación, ejecutar la instancia original y una variante que retira el gold. En evaluación, permutar también las dos opciones originales y comparar el mismo ID semántico. En variantes sin gold, la respuesta esperada es NONE por construcción. Las probabilidades se normalizan sobre las opciones ofrecidas. Elegir temperatura en calibración por NLL y reportar cobertura/error de selección con umbral fijado en calibración para un máximo de 15 % de error empírico y al menos ocho emisiones. Cuando el modelo elige NONE o queda por debajo del umbral, registrar HOLD. También reportar acierto sin umbral, Brier multicategoría, NLL, estabilidad al permutar y tiempo local.

Criterio de adopción: aumento de cobertura respecto de reglas a un error igual o menor en evaluación, o igual cobertura y error con una reducción de coste. Reportar por separado la detección de candidato ausente y el acierto de las instancias originales. Ninguna salida del ranker confirma identidad ni modifica el Core.

Corrección antes de puntuar: el servidor asigna parte de la masa fuera de las letras literales incluso con gramática. Se inspeccionan 24 tokens y se renormalizan explícitamente solo las letras permitidas, comprobando que todas estén presentes. Se mantienen prompt, casos y criterios.

Control diagnóstico adicional añadido antes de puntuar. Se ofrece un solo candidato real más NONE, como en el control de retirada, pero aquí el candidato presente es el correcto. Los modelos y el umbral se mantienen congelados. Permite detectar si el criterio sólo aprendió a usar el número de opciones.
