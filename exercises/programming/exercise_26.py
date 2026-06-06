def clasificar_archivo (lista_de_archivos):

    csv_archivos = []
    json_archvios = []
    xml_archivos = []

    for i in lista_de_archivos:

        if i.endswith(".csv"):
            csv_archivos.append(i)

        elif i.endswith(".json"):
            json_archvios.append(i)

        elif i.endswith(".xml"):
            xml_archivos.append(i)
    
    print(csv_archivos)
    print(json_archvios)
    print(xml_archivos)

lista = [
    "ventas.csv",
    "clientes.json",
    "productos.xml",
    "empleados.csv"
]

clasificar_archivo(lista)