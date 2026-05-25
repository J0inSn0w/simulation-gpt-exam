# Simulacro de examen — Probabilidad y Estadística

**Maestría en Ciencia de Datos**  
**Duración sugerida:** 50 minutos  
**Instrucciones:** Resuelve cada ejercicio de forma clara y ordenada. Justifica tus respuestas y, cuando aplique, interpreta el resultado en contexto.

---

## Parte I. Probabilidad

### 1) Variable aleatoria discreta
Una máquina produce piezas defectuosas con probabilidad 0.08 de manera independiente en cada pieza. Se inspeccionan 10 piezas.

1. Defina la variable aleatoria adecuada.
2. ¿Qué distribución sigue?
3. Calcule la probabilidad de que exactamente 2 piezas sean defectuosas.
4. Calcule la probabilidad de que al menos 1 pieza sea defectuosa.

---

### 2) Binomial
En una encuesta, 60% de los usuarios prefiere una nueva interfaz. Si se seleccionan 8 usuarios al azar:

1. Calcule la probabilidad de que exactamente 5 prefieran la nueva interfaz.
2. Calcule la probabilidad de que como máximo 3 la prefieran.
3. Calcule la esperanza y varianza de la variable aleatoria.

---

### 3) Poisson
En una tienda llegan en promedio 4 clientes por hora.

1. Modela el número de clientes por hora con una distribución adecuada.
2. Calcula la probabilidad de que lleguen exactamente 6 clientes en una hora.
3. Calcula la probabilidad de que lleguen más de 2 clientes en media hora.

---

### 4) Probabilidad condicional
En una empresa, el 70% de los empleados usa laptop y el 40% usa laptop y trabaja remoto. Si se elige un empleado al azar:

1. Calcula la probabilidad de que trabaje remoto dado que usa laptop.
2. Calcula la probabilidad de que use laptop dado que trabaja remoto si además se sabe que el 50% de los empleados trabaja remoto.
3. Interpreta el resultado.

---

### 5) Distribución conjunta y marginal
Sean \(X\) y \(Y\) variables aleatorias discretas con la siguiente función de probabilidad conjunta:

\[
P(X=x, Y=y) =
\begin{cases}
0.2 & (x,y)=(0,0) \\
0.3 & (x,y)=(0,1) \\
0.1 & (x,y)=(1,0) \\
0.4 & (x,y)=(1,1)
\end{cases}
\]

1. Obtén las distribuciones marginales de \(X\) y \(Y\).
2. Verifica si \(X\) y \(Y\) son independientes.
3. Calcula \(P(X=1 \mid Y=1)\).

---

### 6) Esperanza y varianza
Sea una variable aleatoria discreta \(X\) con valores:

\[
X \in \{0,1,2,3\}
\]

y probabilidades

\[
P(X=0)=0.1,\; P(X=1)=0.2,\; P(X=2)=0.4,\; P(X=3)=0.3
\]

1. Calcula \(E[X]\).
2. Calcula \(Var(X)\).
3. Calcula \(E[2X+1]\).

---

## Parte II. Estadística descriptiva

### 7) Medidas de tendencia central y dispersión
Se tienen los siguientes datos de calificaciones:

\[
74,\ 82,\ 68,\ 90,\ 75,\ 88,\ 71,\ 85
\]

1. Calcula la media.
2. Calcula la mediana.
3. Calcula la varianza muestral.
4. Calcula la desviación estándar muestral.

---

### 8) Cuantiles y percentiles
Un grupo de 20 personas tiene las siguientes edades ordenadas:

\[
18, 19, 20, 21, 21, 22, 23, 24, 24, 25, 26, 27, 28, 29, 30, 31, 33, 35, 38, 40
\]

1. Determina el primer cuartil.
2. Determina la mediana.
3. Determina el tercer cuartil.
4. Interpreta el rango intercuartílico.

---

### 9) Histograma y boxplot
Un conjunto de datos presenta una distribución claramente sesgada a la derecha.

1. ¿Qué esperarías observar en el histograma?
2. ¿Cómo se vería el boxplot?
3. ¿Cuál medida de centro describiría mejor estos datos: media o mediana?

---

### 10) Correlación y dispersión
Se observó que al aumentar las horas de estudio también aumenta la calificación obtenida.

1. ¿Qué tipo de correlación existe?
2. ¿Cuál sería el signo del coeficiente de correlación?
3. ¿La correlación implica causalidad? Justifica.

---

### 11) Tabla de frecuencias
En una muestra de 25 personas, las respuestas a una pregunta fueron:

- Sí: 15
- No: 6
- Tal vez: 4

1. Construye la tabla de frecuencias absolutas.
2. Calcula las frecuencias relativas.
3. Determina el porcentaje de respuestas afirmativas.

---

## Parte III. Inferencia estadística

### 12) Intervalo de confianza para una media
Una muestra aleatoria de 36 observaciones tiene media 52 y desviación estándar 6.

1. Construye un intervalo de confianza del 95% para la media poblacional.
2. Interpreta el intervalo.

---

### 13) Prueba de hipótesis para una media
Una fábrica afirma que el peso promedio de sus paquetes es de 2 kg. Se toma una muestra de 25 paquetes y se obtiene una media de 1.92 kg con desviación estándar 0.20 kg.

1. Plantea las hipótesis.
2. Realiza la prueba a un nivel de significancia de 0.05.
3. Concluye en contexto.

---

### 14) Prueba de hipótesis para una proporción
En una campaña digital se afirma que al menos 60% de los usuarios hace clic en un anuncio. En una muestra de 100 usuarios, 54 hicieron clic.

1. Plantea las hipótesis adecuadas.
2. Realiza la prueba para \(\alpha = 0.05\).
3. Interpreta el resultado.

---

### 15) Diferencia de medias
Dos métodos de entrenamiento se aplican a dos grupos independientes de tamaño 30 y 35. Los promedios obtenidos fueron 78 y 83, con desviaciones estándar 10 y 12 respectivamente.

1. Plantea una prueba para comparar las medias.
2. Explica qué significaría rechazar la hipótesis nula.
3. Indica qué información adicional sería útil para concluir con precisión.

---

### 16) Comparación de varianzas
Dos máquinas producen piezas con variabilidad distinta. Se tiene una muestra de 15 piezas de la máquina A y 12 de la máquina B.

1. Explica qué prueba usarías para comparar varianzas.
2. ¿Qué hipótesis plantearías?
3. ¿Qué concluyes si el cociente de varianzas muestrales es muy grande?

---

### 17) ANOVA de una vía
Se quiere comparar el rendimiento de tres algoritmos de recomendación diferentes.

1. Explica qué hipótesis se evalúan en un ANOVA de una vía.
2. ¿Qué significa obtener un valor-p menor que 0.05?
3. ¿Qué harías después de rechazar la hipótesis nula?

---

## Parte IV. Problema integrador

### 18) Análisis de una muestra realista
Se midieron los tiempos de respuesta de un sistema en segundos:

\[
12, 15, 14, 16, 18, 15, 13, 17, 19, 14
\]

1. Calcula media, mediana y desviación estándar muestral.
2. Construye una interpretación breve de los resultados.
3. Si el sistema debe responder en promedio en menos de 15 segundos, ¿qué dirías con base en estos datos?

---

### 19) Interpretación de percentiles
En una evaluación, un estudiante quedó en el percentil 85.

1. ¿Qué significa eso?
2. ¿Ese estudiante obtuvo una calificación mayor o menor que el 85% del grupo?
3. ¿Es lo mismo percentil 85 que sacar 85/100? Explica.

---

### 20) Pregunta conceptual tipo examen
Responde brevemente:

1. ¿Cuál es la diferencia entre una variable aleatoria discreta y una continua?
2. ¿Qué información te da una desviación estándar grande?
3. ¿Por qué el boxplot es útil para detectar valores atípicos?
4. ¿Qué significa rechazar la hipótesis nula?

---

## Indicaciones para autoevaluarte

- Si dominas del 1 al 6, tienes buena base en probabilidad.
- Si dominas del 7 al 11, estás bien en estadística descriptiva.
- Si dominas del 12 al 17, estás listo para la parte inferencial del examen.
- Si respondes bien el 18 al 20, tienes una comprensión fuerte y completa del área.

