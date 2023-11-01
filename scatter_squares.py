import matplotlib.pyplot as plt

"""绘制散点图"""
# 通过这句话查看散点图样式有哪些
# print(plt.style.available)
# 设置散点图样式
plt.style.use("seaborn-v0_8")
# 创建子图
fig, ax = plt.subplots()
# 设置单个散点坐标
ax.scatter(2, 4, s=200)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# 设置刻度标记的样式
ax.tick_params(labelsize=14)
plt.show()
