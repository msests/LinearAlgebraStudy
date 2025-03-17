import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义x轴和y轴的范围
x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)

# 使用meshgrid生成坐标矩阵
X, Y = np.meshgrid(x, y)

print("X:\n", X)
print("Y:\n", Y)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X, Y, Z, alpha=0.5, color='lightblue', edgecolor='k')

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)

# 绘制带箭头的x轴，从-2到2
ax.quiver(-2, 0, 0, 4, 0, 0, color='r', label='$\mathbf{x}$', length=1, arrow_length_ratio=0.1)
# 绘制带箭头的y轴，从-2到2
ax.quiver(0, -2, 0, 0, 4, 0, color='b', label='$\mathbf{y}$', length=1, arrow_length_ratio=0.1)
# 绘制带箭头的z轴，从-2到2
ax.quiver(0, 0, -2, 0, 0, 4, color='g', label='$\mathbf{z}$', length=1, arrow_length_ratio=0.1)

ax.quiver(0, 0, 0, 0.5, 1, 0.2, color='orange', label='$\mathbf{u}$', length=1, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0.1, 0.8, 0.4, color='orange', label='$\mathbf{v}$', length=1, arrow_length_ratio=0.1)

# 定义两个向量
u = np.array([0.5, 1, 0.2])
v = np.array([0.1, 0.8, 0.4])

# 创建网格数据
x, y = np.meshgrid(np.linspace(-2, 2, 10), np.linspace(-2, 2, 10))
z = (-(u[1]*v[2] - u[2]*v[1])*x + (u[0]*v[2] - u[2]*v[0])*y) / (u[0]*v[1] - u[1]*v[0])

ax.plot_surface(x, y, z, alpha=0.5, color='lightblue', edgecolor='k')

ax.set_xlabel('u (X-axis)', fontsize=12)
ax.set_ylabel('v (Y-axis)', fontsize=12)
ax.set_zlabel('Z-axis', fontsize=12)
ax.set_title('Parametric Plane $\\mathbf{r}(u, v) = u\\mathbf{i} + v\\mathbf{j}$', fontsize=14)
ax.legend()
ax.set_box_aspect([1, 1, 1])  # 保持坐标轴比例一致
plt.show()