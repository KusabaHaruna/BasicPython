a = int(input("aの値を入力してください: "))
b = int(input("bの値を入力してください: "))


def euclid(a, b) -> int:
    a, b = max(a, b), min(a, b)
    while b != 0:
        a, b = b, a % b
    return a
    
print(euclid(a, b))
    
def mutually_prime(a, b) :
    return euclid(a, b) == 1
print(mutually_prime(a, b))

import random
count = 0

for _ in range(100000) :
    x, y = random.randint(2, 100000), random.randint(2, 100000)
    if mutually_prime(x, y) :
        count += 1

print(count / 100000)

