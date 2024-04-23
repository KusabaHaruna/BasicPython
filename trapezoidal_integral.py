from math import sin
from math import pi
# --example--
# print(sin(0))
# >>> 0
# -----------
a = 0
b = 0.5 * pi

N = 100
h = (b-a) / N
s = sum([sin(a + (i -1) * h) + sin(a +i *h)for i in range(1, N+1)])

print(h / 2 * s)
