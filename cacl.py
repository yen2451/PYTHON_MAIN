import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**3-5*x**2+200


sequence = [-4.572, -4.5718, -4.5716, -4.5714, -4.5712, -4.571]
for i in sequence:
    print(i, " ", f(i))


plt.xlabel("x")
plt.ylabel("y")
plt.title("Figure of $x^{3}$-5*$x^{2}$+200")
x = np.linspace(-4.572, -4.57, num=100)
y = f(x)

plt.plot(x, y)
plt.savefig('fig1.jpg')
plt.show()
