from math import sin, pi

# --example--
# print(sin(0))
# >>> 0
# -----------

def f(a, b, N):
    h = (b - a) / N
    answer = 0

    for i in range(1, N + 1):
        answer += (h / 2) * (sin(a + (i - 1) * h) + sin(a + i * h))
    
    return answer

a = 0
b = 1
N = 100

result = f(a, b, N)
print(result)
