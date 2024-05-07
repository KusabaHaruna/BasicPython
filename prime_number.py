# a = input("aの値を入力: ")
# b = input("bの値を入力: ")

# TODO

def sosuu(n):
    is_prime = True # 真

    # 2から n-1 までの数で割れるかどうか判断する
    for p in range(2, n-1):
        if n % p == 0:
            is_prime = True # 偽
            break

    if n == 1:
        is_prime = False

    return is_prime