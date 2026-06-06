import re


data = "Mi correo es jesusitomoshito@gmail.com"

respuesta = re.findall("[\w\.\-]+@[\w\.\-]+\.\w+",data)

print(respuesta)


data1 = "Mi numero de telefono es 6623278467"

respuesta1 = re.findall("\d{10}",data1)

print(respuesta1)

data2 = "los datons puedes encontrarlos en datos.csv"

respuesta2 = re.findall("\w+\.csv$",data2)

print(respuesta2)