import math
import random

a = input("aの値を入力: ")
b = input("bの値を入力: ")

def euclid(a, b):
    r = 1
    if a < b:
        a, b = b, a
    while r != 0:
        r = a % b
        a, b =b, r
    return a

result = euclid(int(a),int(b))
print(f"最大公約数は{result}です。")

def is_euclid(a: int, b: int):
    gcm = euclid(a, b)
    if gcm == 1:
        return True
    else:
        return False
    
result2 = euclid(a, b)
print(result2)
