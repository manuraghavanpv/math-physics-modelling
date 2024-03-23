import matplotlib.pyplot as plt

a = -2
b = 4
n = 100
dx = (b-a)/n
x = []
y = []
fx = []
Integration = 0
i = 0
while i < n:
    endpoint1 = (a + i*dx)
    endpoint2 = (a + (i+1)*dx)
    x.append(endpoint1)
    q1 = (endpoint1)**2 + 1
    q2 = (endpoint2)**2 + 1
    y.append(q1)
    Integration += dx*0.5*(q1 + q2)
    fx.append(Integration)
    i += 1

print("The given problem integrates as: ", round(Integration, 3))
plt.plot(x, y)
plt.plot(x, fx)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Roll. No. 241- Integration of 1a by Trapezoid method")

plt.show()