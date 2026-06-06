limite = 2000000
criba = [True] * (limite + 1)

criba[0] = False
criba[1] = False

for i in range (2,len(criba)):
    if criba[i]:
        for n in range (i*2, limite+1,i):
            criba[n] = False

resultado = sum(i for i in range(limite + 1) if criba[i])

print(resultado)