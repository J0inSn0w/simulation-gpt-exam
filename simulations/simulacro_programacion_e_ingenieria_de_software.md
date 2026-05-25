# Simulacro de examen — Programación e Ingeniería de Software

**Maestría en Ciencia de Datos**  
**Duración sugerida:** 50 minutos  
**Instrucciones:** Resuelve cada ejercicio de forma clara y ordenada. Cuando se pida código, escribe una solución en Python o pseudocódigo según corresponda. Justifica tus respuestas cuando aplique.

---

## Parte I. Fundamentos de programación

### 1) Trazado de código
¿Qué imprime el siguiente código?

```python
x = 0

for i in range(1, 6):
    x += i

print(x)
```

---

### 2) Listas y mutabilidad
¿Qué valores tienen `a` y `b` al final?

```python
a = [1, 2]
b = a.append(3)

print(a)
print(b)
```

---

### 3) Condicionales
Escribe una función en Python llamada `par_impar` que reciba un número entero y regrese:

- `"par"` si el número es par
- `"impar"` si el número es impar

---

### 4) Contar frecuencias
Dada la lista:

```python
nums = [1, 2, 2, 3, 3, 3, 4]
```

Escribe un programa que cuente cuántas veces aparece cada número.

---

### 5) Cadenas
Escribe una función que reciba una cadena y regrese la misma cadena invertida.

No uses slicing (`[::-1]`).

---

### 6) Errores lógicos
Analiza el siguiente código y explica qué problema presenta:

```python
nums = [1, 2, 3]

for n in nums:
    nums.remove(n)

print(nums)
```

---

### 7) Estructuras de datos simples
Responde brevemente:

1. ¿Qué diferencia hay entre una lista y una tupla?
2. ¿Qué diferencia hay entre una lista y un diccionario?
3. ¿Para qué sirve una tabla hash?

---

## Parte II. Diseño de algoritmos y pseudocódigo

### 8) Máximo de una lista
Escribe pseudocódigo para encontrar el valor máximo de una lista de números.

---

### 9) Validación de entrada
Escribe pseudocódigo para validar si una contraseña cumple lo siguiente:

- tiene al menos 8 caracteres
- contiene al menos una letra mayúscula
- contiene al menos un número

---

### 10) Anagramas
Escribe una función en Python llamada `son_anagramas` que reciba dos cadenas y regrese `True` si son anagramas y `False` en caso contrario.

Prueba la función con las palabras `"listen"` y `"silent"`.

---

### 11) Números primos
Escribe una función que determine si un número entero positivo es primo.

---

### 12) Permutaciones y horas válidas
Se te dan 4 dígitos. Escribe un pseudocódigo para encontrar todas las combinaciones posibles que formen una hora válida en formato `HH:MM`.

---

### 13) Búsqueda en una lista
Escribe pseudocódigo para buscar un elemento en una lista y regresar su posición. Si no existe, debe indicar que no fue encontrado.

---

## Parte III. Lectura y transformación de datos

### 14) CSV con pandas
Escribe un programa en Python que lea un archivo CSV llamado `datos.csv` y:

1. muestre las primeras 5 filas
2. elimine una columna llamada `score_general`
3. elimine los renglones donde `cantidad < 50`

---

### 15) Filtrado y agrupación con pandas
Dado un DataFrame con columnas:

- `genero`
- `ingreso`
- `edad`

obtén:

1. el ingreso promedio por género
2. la edad mínima por género

---

### 16) Lectura de Excel
Escribe una función en Python usando pandas que:

1. lea la hoja 3 de un archivo de Excel
2. elimine las columnas `calif_general`, `dirección` y `genero`
3. elimine los renglones donde `edad < 18`
4. grafique un boxplot de `calif_mate` agrupado por `municipio`

---

### 17) JSON y XML
Responde brevemente:

1. ¿Qué diferencia hay entre JSON y XML?
2. ¿Cuándo usarías JSON?
3. ¿Cómo accederías a un campo dentro de un archivo JSON?

---

### 18) Expresiones regulares
Escribe una expresión regular que permita detectar:

1. correos electrónicos
2. números telefónicos de 10 dígitos
3. cadenas que terminen en `.csv`

---

## Parte IV. Manejo de herramientas computacionales

### 19) Git básico
Supón que hiciste cambios en el archivo `limpieza.py` dentro de un repositorio local. Escribe los comandos necesarios para:

1. agregar el archivo al área de preparación
2. guardar los cambios con un commit
3. enviar los cambios al repositorio remoto

---

### 20) Git: concepto
Responde brevemente:

1. ¿Qué diferencia hay entre `fork` y `clone`?
2. ¿Qué hace `git add`?
3. ¿Qué hace `git commit`?

---

### 21) Bash básico
Escribe comandos de línea de comando para:

1. mostrar los archivos de un directorio
2. cambiarte a otro directorio
3. crear una carpeta nueva
4. mostrar el contenido de un archivo de texto

---

### 22) Depuración
Responde brevemente:

1. ¿Para qué sirve un debugger?
2. ¿Qué información te da un profiler?
3. ¿Por qué son útiles en desarrollo de software?

---

## Parte V. Programación y datos en contexto

### 23) Suma de primos
Escribe un programa que calcule la suma de todos los números primos menores a 2 millones.

Se evalúa principalmente la lógica y la eficiencia de tu solución.

---

### 24) Conteo de palabras
Dado un texto, escribe un programa que cuente la frecuencia de cada palabra.

El programa debe:

1. ignorar mayúsculas y minúsculas
2. eliminar signos de puntuación
3. regresar un diccionario con los conteos

---

### 25) Manejo de errores
Escribe un programa en Python que intente leer un archivo CSV. Si el archivo no existe, debe mostrar un mensaje amigable y no terminar abruptamente.

---

### 26) Clasificación de archivos
Supón que tienes varios archivos con extensiones `.csv`, `.json` y `.xml`.

Escribe un algoritmo que reciba una lista de nombres de archivo y los clasifique por tipo de extensión.

---

### 27) Integradora tipo examen
Escribe un programa en Python que haga lo siguiente:

1. lea un archivo CSV
2. elimine columnas innecesarias
3. filtre renglones según una condición
4. agrupe por una columna categórica
5. calcule un resumen estadístico
6. guarde el resultado final en un nuevo archivo

---

## Indicaciones para autoevaluarte

- Si resuelves bien del 1 al 7, tienes buena base de fundamentos.
- Si resuelves bien del 8 al 13, tienes buena lógica algorítmica.
- Si resuelves bien del 14 al 18, estás fuerte en transformación de datos.
- Si resuelves bien del 19 al 22, dominas herramientas de trabajo básicas.
- Si completas el 23 al 27, estás muy bien preparado para el estilo real del examen.

