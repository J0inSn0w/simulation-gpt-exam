"""
Algoritmo EncontrarHorasValidas

Entrada: d1, d2, d3, d4

digitos ← [d1, d2, d3, d4]

Para cada permutacion de digitos hacer

    hora ← permutacion[0] * 10 + permutacion[1]
    minuto ← permutacion[2] * 10 + permutacion[3]

    Si hora >= 0 Y hora <= 23 Y minuto >= 0 Y minuto <= 59 entonces
        Mostrar hora : minuto
    Fin Si

Fin Para

Fin Algoritmo

"""