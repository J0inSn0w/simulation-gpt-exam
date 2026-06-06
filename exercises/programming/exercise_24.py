import string

def contar_frecuencias(texto):

    texto = texto.lower()

    for signo in string.punctuation + "¡¿":
        texto = texto.replace(signo, "")
    
    texto = texto.split()

    dictperron = dict()

    for i in texto:
        dictperron[i] = dictperron.get(i,0) + 1

    return dictperron

texto = "Hola mundo, hola Python. ¡Mundo es genial!"
print(contar_frecuencias(texto))