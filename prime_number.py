# a = input("aの値を入力: ")
# b = input("bの値を入力: ")

# TODO

import math

def is_prime_number(n: int) -> bool: #素数判定　関数
      if n <= 1:
            return False
      for i in range(2, math.isqrt(n)+1):
               if n % i == 0:
                  return False
      else:
            return True


def natural_number() -> int: #自然数を入力するまで入力を求める　関数 
      while True:
            try:
                  n = int(input("自然数を入力してください :"))
                  if n >= 0:
                        break
                  else:
                        print("正しい形式で自然数を入力したください :")
            except ValueError:
                  print ("ValueErroが生じています。int型での入力でお願いします")

      return n

n = natural_number()
result = is_prime_number(n) 
print(f"{n}は{'素数です' if result else '素数ではありません'}")
