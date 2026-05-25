# Simulacro de examen — Álgebra Lineal y Optimización

**Maestría en Ciencia de Datos**  
**Duración sugerida:** 50 minutos  
**Instrucciones:** Resuelve cada ejercicio de forma clara y ordenada. Justifica tus respuestas. Puedes escribir tus procedimientos en forma algebraica y, cuando aplique, interpretar geométricamente el resultado.

---

## Parte I. Álgebra lineal

### 1) Independencia lineal y combinación lineal
Considere los vectores en \(\mathbb{R}^3\):

\[
 v_1 = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}, \quad
 v_2 = \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}, \quad
 v_3 = \begin{bmatrix} 3 \\ 5 \\ -1 \end{bmatrix}
\]

1. Verifique si los vectores son linealmente independientes.
2. Si lo son, encuentre una combinación lineal de ellos que sea igual a \(\begin{bmatrix} 4 \\ 7 \\ -2 \end{bmatrix}\).
3. Si no lo son, encuentre una combinación lineal que dé como resultado el vector cero.

---

### 2) Producto punto, norma y ortogonalidad
Sean

\[
 u = \begin{bmatrix} 1 \\ -2 \\ 2 \end{bmatrix}, \quad
 w = \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}
\]

1. Calcule \(u \cdot w\).
2. Determine si los vectores son ortogonales.
3. Calcule \(\|u\|\).

---

### 3) Matrices y multiplicación
Sean

\[
A = \begin{bmatrix} 1 & 2 \\ 0 & -1 \end{bmatrix}, \quad
B = \begin{bmatrix} 3 & 1 \\ 4 & 2 \end{bmatrix}
\]

1. Calcule \(A + B\).
2. Calcule \(AB\).
3. Calcule \(BA\) y compare el resultado con \(AB\).

---

### 4) Matriz transpuesta e interpretación
Sea

\[
C = \begin{bmatrix}
1 & 0 & 2 \\
-1 & 3 & 1
\end{bmatrix}
\]

1. Encuentre \(C^T\).
2. Determine las dimensiones de \(C\) y \(C^T\).
3. Explique qué cambia al transponer una matriz.

---

### 5) Sistema de ecuaciones lineales
Considere la matriz de coeficientes

\[
M = \begin{bmatrix}
1 & 1 & 1 \\
2 & 1 & 3 \\
1 & 2 & 4
\end{bmatrix}
\]

y el vector de términos independientes

\[
b = \begin{bmatrix} 3 \\ 7 \\ 8 \end{bmatrix}
\]

1. Escriba el sistema de ecuaciones asociado a \(Mx=b\).
2. Determine si el sistema tiene solución única, infinitas soluciones o ninguna solución.
3. Justifique su respuesta.

---

### 6) Inversa y determinante
Sea

\[
D = \begin{bmatrix}
2 & 1 \\
5 & 3
\end{bmatrix}
\]

1. Calcule \(\det(D)\).
2. Determine si \(D\) es invertible.
3. Si existe, calcule \(D^{-1}\).

---

### 7) Rank e imagen de una transformación
Sea la matriz

\[
E = \begin{bmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
0 & 1 & 1
\end{bmatrix}
\]

1. Determine el rango de \(E\).
2. Describa la dimensión del espacio columna.
3. Interprete geométricamente la imagen de la transformación lineal asociada a \(E\).

---

### 8) Autovalores y autovectores
Sea

\[
F = \begin{bmatrix}
4 & 1 \\
1 & 4
\end{bmatrix}
\]

1. Encuentre los autovalores de \(F\).
2. Encuentre un autovector asociado a cada autovalor.
3. Determine si \(F\) es diagonalizable.

---

## Parte II. Optimización

### 9) Sucesiones
Considere la sucesión

\[
a_n = \frac{(-1)^n}{n}
\]

1. Determine si la sucesión está acotada.
2. Determine si converge.
3. Encuentre su límite si existe.

---

### 10) Máximos y mínimos en un conjunto
Sea la función

\[
f(x,y) = x^2 + y^2 - 2x - 4y
\]

definida sobre el cuadrado

\[
D = \{(x,y) \in \mathbb{R}^2 : 0 \le x \le 3,\ 0 \le y \le 4\}
\]

1. Encuentre los puntos críticos de \(f\).
2. Determine el mínimo y el máximo de \(f\) sobre \(D\).
3. Indique en qué puntos se alcanzan.

---

### 11) Gradiente y derivada direccional
Sea

\[
g(x,y) = x^2y + y^3
\]

1. Calcule \(\nabla g(x,y)\).
2. Calcule la derivada direccional de \(g\) en el punto \((1,1)\) en la dirección del vector \(v = \begin{bmatrix} 3 \\ 4 \end{bmatrix}\).
3. Interprete el resultado geométricamente.

---

### 12) Hessiana y clasificación de puntos críticos
Sea

\[
h(x,y) = x^4 - 4x^2 + y^4 - 2y^2
\]

1. Calcule la matriz Hessiana de \(h\).
2. Encuentre los puntos críticos de \(h\).
3. Clasifique cada punto crítico como máximo local, mínimo local o punto silla.

---

## Pregunta extra integradora

### 13) Interpretación geométrica de una transformación
Sea \(T:\mathbb{R}^2 \to \mathbb{R}^2\) dada por

\[
T(x) = Ax, \quad A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
\]

1. Describa el efecto geométrico de \(T\).
2. ¿Qué le ocurre a la norma de un vector bajo esta transformación?
3. ¿Qué relación tiene esta matriz con una rotación?

---

## Indicaciones para autoevaluarte

- Si dominas del 1 al 8, tienes buena base de álgebra lineal.
- Si dominas del 9 al 12, estás bien preparado en optimización.
- Si resuelves la 13 con interpretación clara, tienes nivel muy competitivo para el examen.

