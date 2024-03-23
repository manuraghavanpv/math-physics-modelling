import matplotlib.pyplot as plt
import numpy as np

# Setting limits
lowlim = 0
uplim = 25
x = [0]
fun = [0]
nfun = []

# Iteration variable
i = 0

n = 50
u = 0
area = 0
dx = (uplim - lowlim) / n

# Running a while loop
while i < n:
    midx = ((2 * i + 1) * dx) / 2
    x.append(midx)
    i = i + 1

i = 1
for t in x:
    if 5 <= t <= 10:
        a = 5
        fun.append(fun[i - 1] + a * dx)
        i = i + 1
    elif 15 <= t <= 20:
        a = -5
        fun.append(fun[i - 1] + a * dx)
        i = i + 1
    elif 0 < t < 5 or 10 < t < 15 or 20 < t < 25:
        a = 0
        fun.append(fun[i - 1] + a * dx)
        i = i + 1

plt.plot(x, fun)

i = 0
for v in x:
    if i < 51:
        area = area + dx * 0.5 * (fun[i] + fun[i - 1])
        nfun.append(area)
        i = i + 1

    else:
        area = area + dx * 0.5 * (fun[i + 1])
        nfun.append(area)

print(area)

plt.plot(x, nfun)
plt.xlabel("time")
plt.ylabel("displacement")
plt.title("Roll no. 241: Using Trapezoid Method")
plt.show()