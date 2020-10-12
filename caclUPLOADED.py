import matplotlib.pyplot as plt
import numpy as np


def f(x):
    # function
    return x**3-5*x**2+200


sequence = [-4.5718, -4.5716, -4.5714, -4.5712, -4.571]
for i in sequence:
    print(i, " ", f(i))

x = np.linspace(-4.571, -4.572, num=100)
y = f(x)
plt.plot(x, y, linewidth=1)
plt.show()
