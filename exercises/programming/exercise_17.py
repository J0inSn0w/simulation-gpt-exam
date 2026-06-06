"""

1) ¿Qué diferencia hay entre JSON y XML?
JSON es más ligero, fácil de leer y escribir, y se basa en pares clave-valor.
XML es más verboso, usa etiquetas (tags) y permite estructuras más formales y complejas.

👉 En resumen:

JSON = simple, ligero, moderno
XML = más estructurado, pero más pesado
2) ¿Cuándo usarías JSON?

Usaría JSON cuando:

Estoy trabajando con APIs
Intercambio de datos entre sistemas (web, Python, servicios)
Necesito algo fácil de parsear en Python o JavaScript
Manejo de datos semi-estructurados

3) ¿Cómo accederías a un campo dentro de un archivo JSON?

En Python, normalmente usando el módulo json:

import json

data = {
    "nombre": "Juan",
    "edad": 30
}

print(data["nombre"])

import json

with open("archivo.json") as f:
    data = json.load(f)

print(data["nombre"])

import xml.etree.ElementTree as ET

xml_data = """
#<persona>
  #  <nombre>Juan</nombre>
   # <edad>30</edad>
#</persona>
"""

root = ET.fromstring(xml_data)

print(root.find("nombre").text)
print(root.find("edad").text)

"""