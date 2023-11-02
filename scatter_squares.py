import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
"""绘制散点图"""
# 通过这句话查看散点图样式有哪些
# print(plt.style.available)
# 设置散点图样式
plt.style.use("seaborn-v0_8")
# 创建子图
fig, ax = plt.subplots()
# 设置单个散点坐标
# ax.scatter(2, 4, s=200)
# 批量设置散点

ax.scatter(x_values, y_values, s=50)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# 设置刻度标记的样式
ax.tick_params(labelsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1_100_000])
plt.show()
