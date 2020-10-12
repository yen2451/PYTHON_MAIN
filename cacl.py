import matplotlib.pyplot as plt
import numpy as np


def f(x):
    # function
    return x**3-5*x**2+200

sequence = [-4.5718, -4.5716, -4.5714, -4.5712, -4.571]
for i in sequence:
    print(i, " ", f(i))
# 顯示Ｘ座標標題
plt.xlabel("x")
# 顯示Ｙ座標標題
plt.ylabel("f(x)")
# 顯示圖表標題
plt.title("Figure of $x^{3}$-5*$x^{2}$+200")
# plot fuction's graph
x = np.linspace(-4.571, -4.572, num=100)
y = f(x)
plt.plot(x, y, linewidth=1, label="f(x)")
# plot y=0 graph
#plt.plot([-4.571, -4.572], [0, 0], c='b', linestyle='dashed', label="y=0")
# graph index
plt.legend(loc='upper left')
plt.show()
