a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

def euclid(a, b):
    if a > b:
        A = a
        B = b
    else:
        A = b
        B = A

    while B != 0:
        A, B = B, A % B
    return A

def yakusuu(n):

#A = euclid(a, b)
    if n == 1:
       return True
    else:
       return False
    
answer = yakusuu(euclid(a, b))
print(answer)

