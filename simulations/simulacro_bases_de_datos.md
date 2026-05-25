# Simulacro de examen — Bases de Datos y Sistemas de Información

**Maestría en Ciencia de Datos**  
**Duración sugerida:** 50 minutos  
**Instrucciones:** Resuelve cada ejercicio de forma clara y ordenada. Escribe comandos SQL completos cuando corresponda y justifica tus respuestas si se solicita.

---

## Parte I. Modelado de datos

### 1) Conceptos básicos de modelado
Responde brevemente:

1. ¿Qué es una entidad en un modelo de datos?
2. ¿Qué es una relación entre entidades?
3. ¿Cuál es la diferencia entre llave primaria y llave foránea?
4. ¿Por qué es útil normalizar una base de datos?

---

### 2) Identificación de relaciones
Considera las siguientes entidades:

- **Alumno**
- **Materia**
- **Profesor**

1. Propón una relación entre Alumno y Materia.
2. Propón una relación entre Profesor y Materia.
3. Indica si alguna de esas relaciones es de uno a muchos, muchos a muchos o uno a uno.

---

### 3) Diseño de tabla a partir de un modelo
Se desea almacenar información de empleados con los siguientes datos:

- id_empleado
- nombre
- apellido
- fecha_nacimiento
- salario
- id_departamento

1. Identifica cuál campo debería ser llave primaria.
2. Identifica cuál campo podría ser llave foránea.
3. Propón el tipo de dato para cada columna.

---

### 4) Modelo relacional
Responde brevemente:

1. ¿Qué representa una tabla en el modelo relacional?
2. ¿Qué representa una fila?
3. ¿Qué representa una columna?
4. ¿Por qué dos tablas se relacionan mediante llaves?

---

## Parte II. SQL básico

### 5) CREATE TABLE
Escribe la instrucción SQL para crear una tabla llamada `empleados` con las siguientes columnas:

- `id` entero, autoincremental y llave primaria
- `nombre` texto de máximo 50 caracteres
- `apellido` texto de máximo 50 caracteres
- `edad` entero
- `sexo` de un carácter

---

### 6) INSERT
Inserta los siguientes registros en la tabla `empleados`:

- Carmen Pérez, 17 años, M
- María Espino, 22 años, M
- Jorge Vázquez, 21 años, H
- Jaime Pino, 17 años, H

---

### 7) SELECT básico
Escribe una consulta SQL para obtener todos los registros de la tabla `empleados`.

---

### 8) SELECT con filtro
Escribe una consulta SQL para obtener únicamente los nombres y apellidos de los empleados que:

- tengan 21 años o más
- y sean mujeres

---

### 9) UPDATE y DELETE
Sobre la tabla `empleados`:

1. Actualiza la edad de Carmen Pérez a 23 años.
2. Incrementa la edad de todos los empleados en 1 año.
3. Elimina el registro de Jorge Vázquez.

---

### 10) Agregaciones básicas
Escribe consultas SQL para:

1. Contar cuántos empleados hay en la tabla.
2. Obtener la edad promedio de los empleados.
3. Obtener la edad máxima.
4. Obtener la edad mínima.

---

## Parte III. SQL intermedio

### 11) COUNT, DISTINCT y GROUP BY
Considera una tabla `ventas` con columnas:

- `id_venta`
- `producto`
- `categoria`
- `monto`

Escribe consultas SQL para:

1. Contar cuántos registros hay.
2. Obtener los valores distintos de `categoria`.
3. Calcular el monto promedio por categoría.

---

### 12) ORDER BY, LIMIT y filtros
Considera una tabla `empleados` con columnas:

- `nombre`
- `apellido`
- `edad`
- `salario`

Escribe consultas SQL para:

1. Obtener a los empleados ordenados de mayor a menor salario.
2. Obtener los 3 empleados con mayor salario.
3. Obtener a los empleados con salario entre 60000 y 75000.

---

### 13) Subconsulta
Considera una tabla `empleados` con las columnas `nombre`, `apellido` y `salario`.

Escribe una consulta que devuelva el nombre y apellido del empleado con el salario más alto.

---

### 14) JOIN básico
Considere las siguientes tablas:

**departamentos**  
- `id_departamento`
- `nombre_departamento`

**empleados**  
- `id_empleado`
- `nombre`
- `apellido`
- `id_departamento`

Escribe una consulta que muestre:

- nombre del empleado
- apellido del empleado
- nombre del departamento

usando un JOIN entre ambas tablas.

---

### 15) JOIN con condición
Con las mismas tablas del ejercicio anterior:

1. Escribe una consulta que obtenga únicamente los empleados del departamento “Desarrollo”.
2. Escribe una consulta que devuelva todos los empleados aunque no tengan departamento asignado.

---

## Parte IV. Base de datos desde un lenguaje de programación

### 16) Conexión a base de datos
Escribe un pseudocódigo o código en Python para conectarte a una base de datos usando una API.

Tu solución debe incluir:

1. importación de la librería necesaria
2. creación de la conexión
3. ejecución de una consulta
4. cierre de la conexión

---

### 17) Consulta desde Python
Escribe un ejemplo en Python que:

1. se conecte a una base de datos
2. ejecute la consulta `SELECT * FROM empleados;`
3. guarde el resultado en una estructura de datos adecuada
4. muestre los primeros registros

---

### 18) Pandas + SQL
Escribe un ejemplo en Python usando pandas que:

1. lea una tabla de una base de datos
2. la convierta en un DataFrame
3. muestre cuántas filas y columnas tiene
4. filtre los empleados mayores de 30 años

---

### 19) Inserción desde Python
Escribe un ejemplo en Python que:

1. cree un DataFrame con información de clientes
2. lo inserte en una tabla de base de datos
3. especifique el nombre de la tabla destino

---

### 20) Manejo de errores de conexión
Escribe un script breve en Python que:

1. intente conectarse a una base de datos
2. muestre un mensaje si la conexión falla
3. no termine con error abrupto si la base de datos no está disponible

---

## Parte V. NoSQL

### 21) Conceptos de NoSQL
Responde brevemente:

1. ¿Qué es una base de datos NoSQL?
2. ¿Cuál es una diferencia principal entre SQL y NoSQL?
3. Menciona dos tipos de bases de datos NoSQL.

---

### 22) Ejemplos de NoSQL
Indica un ejemplo de uso para cada tipo:

1. key-value
2. documentos
3. grafos
4. series de tiempo

---

### 23) Estructura de documento
Supón que una base de datos de documentos almacena usuarios.

1. Propón un ejemplo de documento JSON para un usuario.
2. Incluye nombre, edad, correo y lista de hobbies.

---

### 24) SQL vs NoSQL
Responde brevemente:

1. ¿Cuándo conviene usar SQL?
2. ¿Cuándo conviene usar NoSQL?
3. ¿Qué ventaja tiene SQL para datos estructurados?

---

## Parte VI. Problema integrador

### 25) Caso práctico completo
Una empresa desea almacenar información de sus empleados y departamentos.

Se tienen las siguientes necesidades:

- Cada empleado pertenece a un departamento.
- Un departamento puede tener muchos empleados.
- Se desea guardar nombre, apellido, edad y salario de cada empleado.
- Se desea guardar el nombre del departamento.

Responde lo siguiente:

1. ¿Qué tablas crearías?
2. ¿Cuál sería la llave primaria de cada tabla?
3. ¿Cuál sería la llave foránea?
4. Escribe el SQL para crear ambas tablas.
5. Escribe una consulta que muestre el nombre completo del empleado y su departamento.

---

## Indicaciones para autoevaluarte

- Si resuelves bien del 1 al 10, dominas fundamentos.
- Si resuelves bien del 11 al 15, tienes buen nivel de SQL intermedio.
- Si resuelves bien del 16 al 20, estás preparado en conexión a bases de datos desde código.
- Si resuelves bien del 21 al 24, entiendes bien SQL vs NoSQL.
- Si completas el 25 con claridad, tienes un nivel muy competitivo para el examen.

