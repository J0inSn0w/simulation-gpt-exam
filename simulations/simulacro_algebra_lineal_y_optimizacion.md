# Simulacro de examen — Álgebra Lineal y Optimización

**Maestría en Ciencia de Datos**  
**Duración sugerida:** 50 minutos  
**Instrucciones:** Resuelve cada ejercicio de forma clara y ordenada. Justifica tus respuestas. Puedes escribir procedimientos algebraicos y, cuando aplique, interpretar geométricamente el resultado.

---

# Parte I. Álgebra lineal

---

## 1) Independencia lineal y combinación lineal

Considere los vectores en R³:

```text
v1 = [ 1 ]
     [ 2 ]
     [-1 ]

v2 = [ 2 ]
     [ 1 ]
     [ 0 ]

v3 = [ 3 ]
     [ 5 ]
     [-1 ]
```

1. Verifique si los vectores son linealmente independientes.

2. Si lo son, encuentre una combinación lineal de ellos que sea igual a:

```text
[ 4 ]
[ 7 ]
[-2 ]
```

3. Si no lo son, encuentre una combinación lineal que dé como resultado el vector cero.

---

## 2) Producto punto, norma y ortogonalidad

Sean:

```text
u = [ 1 ]
    [-2 ]
    [ 2 ]

w = [ 2 ]
    [ 1 ]
    [ 0 ]
```

1. Calcule el producto punto u · w.

2. Determine si los vectores son ortogonales.

3. Calcule la norma de u.

---

## 3) Matrices y multiplicación

Sean:

```text
A = [ 1   2 ]
    [ 0  -1 ]

B = [ 3   1 ]
    [ 4   2 ]
```

1. Calcule A + B.

2. Calcule AB.

3. Calcule BA y compare el resultado con AB.

---

## 4) Matriz transpuesta e interpretación

Sea:

```text
C = [  1   0   2 ]
    [ -1   3   1 ]
```

1. Encuentre la transpuesta de C.

2. Determine las dimensiones de C y de Cᵀ.

3. Explique qué cambia al transponer una matriz.

---

## 5) Sistema de ecuaciones lineales

Considere:

```text
M = [ 1   1   1 ]
    [ 2   1   3 ]
    [ 1   2   4 ]
```

y

```text
b = [ 3 ]
    [ 7 ]
    [ 8 ]
```

1. Escriba el sistema de ecuaciones asociado a Mx = b.

2. Determine si el sistema tiene:
- solución única
- infinitas soluciones
- ninguna solución

3. Justifique su respuesta.

---

## 6) Inversa y determinante

Sea:

```text
D = [ 2   1 ]
    [ 5   3 ]
```

1. Calcule det(D).

2. Determine si D es invertible.

3. Si existe, calcule D⁻¹.

---

## 7) Rango e imagen de una transformación

Sea:

```text
E = [ 1   2   3 ]
    [ 2   4   6 ]
    [ 0   1   1 ]
```

1. Determine el rango de E.

2. Describa la dimensión del espacio columna.

3. Interprete geométricamente la imagen de la transformación lineal asociada a E.

---

## 8) Autovalores y autovectores

Sea:

```text
F = [ 4   1 ]
    [ 1   4 ]
```

1. Encuentre los autovalores de F.

2. Encuentre un autovector asociado a cada autovalor.

3. Determine si F es diagonalizable.

---

# Parte II. Optimización

---

## 9) Sucesiones

Considere la sucesión:

```text
a_n = ((-1)^n)/n
```

1. Determine si la sucesión está acotada.

2. Determine si converge.

3. Encuentre su límite si existe.

---

## 10) Máximos y mínimos

Sea:

```text
f(x,y) = x² + y² - 2x - 4y
```

definida sobre:

```text
D = { (x,y) : 0 ≤ x ≤ 3, 0 ≤ y ≤ 4 }
```

1. Encuentre los puntos críticos de f.

2. Determine el mínimo y máximo de f sobre D.

3. Indique en qué puntos se alcanzan.

---

## 11) Gradiente y derivada direccional

Sea:

```text
g(x,y) = x²y + y³
```

1. Calcule grad g(x,y).

2. Calcule la derivada direccional de g en el punto (1,1) en la dirección:

```text
v = [ 3 ]
    [ 4 ]
```

3. Interprete geométricamente el resultado.

---

## 12) Hessiana y clasificación de puntos críticos

Sea:

```text
h(x,y) = x⁴ - 4x² + y⁴ - 2y²
```

1. Calcule la matriz Hessiana de h.

2. Encuentre los puntos críticos de h.

3. Clasifique cada punto crítico como:
- máximo local
- mínimo local
- punto silla

---

# Pregunta extra integradora

---

## 13) Interpretación geométrica de una transformación

Sea la transformación:

```text
T(x) = Ax
```

donde:

```text
A = [ 0  -1 ]
    [ 1   0 ]
```

1. Describa el efecto geométrico de T.

2. ¿Qué ocurre con la norma de un vector bajo esta transformación?

3. ¿Qué relación tiene esta matriz con una rotación?

---

# Indicaciones para autoevaluarte

- Si dominas del 1 al 8, tienes buena base de álgebra lineal.
- Si dominas del 9 al 12, estás bien preparado en optimización.
- Si resuelves la 13 con interpretación clara, tienes un nivel competitivo para el examen.