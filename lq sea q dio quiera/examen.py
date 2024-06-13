vector =[5,7,7,3,2,5,8,3]
print("vector", vector)
n=3

count = 0
for element in vector:
    if element == n:
        count += 1
print("el numero", n,  "se repite", count, "veces en el vector.")