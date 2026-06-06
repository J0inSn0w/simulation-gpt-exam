nums = [1, 2, 2, 3, 3, 3, 4]


id = dict()

for i in nums:

    id[i] = id.get(i,0) + 1

print (id)