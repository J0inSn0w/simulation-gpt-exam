"""

Algoritmo ValidarContrasena

Entrada: contrasena

Si longitud(contrasena) < 8 entonces
    Mostrar "Contraseña inválida"
    Terminar
Fin Si

tieneMayuscula ← Falso
tieneNumero ← Falso

Para cada caracter en contrasena hacer
    Si caracter es una letra mayúscula entonces
        tieneMayuscula ← Verdadero
    Fin Si

    Si caracter es un número entonces
        tieneNumero ← Verdadero
    Fin Si
Fin Para

Si tieneMayuscula Y tieneNumero entonces
    Mostrar "Contraseña válida"
Sino
    Mostrar "Contraseña inválida"
Fin Si

Fin Algoritmo

"""