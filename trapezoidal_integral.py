from math import sin
from math import pi
import math

# --example--
# print(sin(0))
# >>> 0
# -----------

def trapezoidal_integral(f, a = 0, b = 1, N = 100):
    h = (b - a) / N
    S = 0

    for i in range(1, N + 1):
        S += (h / 2) * (f(a + (i - 1) * h) + f(a + i * h))
    
    return S

def q2_function(x: float) -> float:
    return 4/(1 + x * x)

def q3_function(x: float) -> float:
    return ((math.pi) ** (1/2))  * (math.exp(-x ** 2))

q1 = trapezoidal_integral(sin, 0, (1/2) * (math.pi), 50)
q2 = trapezoidal_integral(q2_function, 0, 1, 100)
q3 = trapezoidal_integral(q3_function, -100, 100, 1000)

result = [q1, q2, q3]
for i in range(3):
    print(f"関数のq{i+1}における積分の値は、{result[i]}です。")

 #　30行目の " "　は　' ' にしても大丈夫ですか？   
 # 最終
