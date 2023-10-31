import matplotlib.pyplot as plt

# 当你使用`matplotlib.pyplot`的`plot`方法，并且只传入一个数组时，这个数组被视为y轴的值，
# 而x轴的值默认为从0开始的整数序列，即[0, 1, 2, ..., n-1]，其中n是传入数组的长度。
# 也就是说，它会绘制一条线，连接所有点 (0, y[0]), (1, y[1]), ..., (n-1, y[n-1])。
#
# 下面是一个简单的例子来说明这个用法：
#
# ```python
# import matplotlib.pyplot as plt
#
# # 只传入一个数组，表示y轴的值
# plt.plot([2, 4, 6, 8])
#
# # 显示图形
# plt.show()
# ```
#
# 在这个例子中，我们只传入了一个数组`[2, 4, 6, 8]`。
# 所以，`plot`方法会默认使用`[0, 1, 2, 3]`作为x轴的值。
# 最终，这会在图表上绘制一条经过点 (0, 2), (1, 4), (2, 6), (3, 8) 的线。
squares = [1, 4, 9, 16, 25]
# 创建子图
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)
# 设置图题并给坐标加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# 设置刻度标记的样式
ax.tick_params(labelsize=14)
plt.show()
