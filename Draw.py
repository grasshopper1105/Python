import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1, 2, 1)
x = np.linspace(0, 10, 100)
y1 = np.cos(x)
y2 = np.sin(x)
plt.plot(x, y1, linestyle='--', label='sinx')
plt.plot(x, y2, color='red', label='cosx')
plt.axis([-0.5, 10.5, -2, 2])
plt.xlabel('axis x')
plt.ylabel('axis y')  # y轴标签
plt.title('fuctions')  # 图片标题
plt.legend()  # 画出图示

plt.subplot(1, 2, 2)
X = np.random.normal(0, 1, 10000)
Y = np.random.normal(0, 1, 10000)
plt.xlabel('axis x1')
plt.ylabel('axis x2')
plt.scatter(X, Y, alpha=0.6, marker='x')  # alpha 为透明度 1 为不透明 0 为透明

plt.show()  # 画出之前所有图
