"""

Nos piden saber los valores de a y b 

Cuando hagamos el prin de a realmente tendremos una lista de [1, 2, 3] y b regresará "None" 
debido a que esta funcion no va a copiar una lista. Para eso tendriamos que hacer un .copy() 

"""
a = [1, 2]
b = a.append(3)

print(a)
print(b)