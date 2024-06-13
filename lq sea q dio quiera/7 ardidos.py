import random

n = 10

vector1 = [random.randint(1, 20)for _ in range(n)]
vector2 = [random.randint(20, 60)for _ in range(n)]
vector3 = [random.randint(60, 100)for _ in range(n)]

S = vector1 + vector2 + vector3

print("Vector A:", vector1)
print("Vector A:", vector1)
print(S)