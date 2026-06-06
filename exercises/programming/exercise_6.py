"""

Este es un problema de indices FOR recorre valor por valor en este caso empieza con el [0] entonces remueve el indice [0] de nums
y queda una lista [2,3] ahora va por el indice [1] pero casualmente ahora 3 esta en el indice 1 entonces lo elimina y queda solo [2]
como no hay indice [2] ahi se cierra el ciclo y devuelve [2] 

"""


nums = [1, 2, 3]

for n in nums:
    nums.remove(n)

print(nums)