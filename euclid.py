a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a, b = map(int, (a,b))
def gcd(a, b):
    r = a % b

    while r != 0:
        a, b = b, r
        r = a % b

    return b

if __name__ == '__main__':
    num1 = a
    num2 = b

    GCD = gcd(num1, num2)

    print(f"({num1}, {num2}) → gcd: {GCD}")
