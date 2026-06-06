def palabra_invertida(palabra):

    resultado = ""

    for i in range(len(palabra)-1, -1, -1):
        resultado = resultado + palabra[i]

    print (resultado)

palabra_invertida("hola")