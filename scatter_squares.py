import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# 绘制点图，x取值，y取值，绘制颜色，点绘制的大小

# 绘制颜色也可以使用color=(0, 0, 0)
# 值越接近 0，指定的颜色越深；值越接近 1，指定的颜色越浅。
#ax.scatter(x_values, y_values, color='red', s=10)

# 颜色映射 c=y_values, cmap=plt.cm.Blues
# 从起始颜色渐变到结束颜色的颜色序列
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置每个坐标轴的取值范围
# ax.axis([xmin, xmax, ymin, ymax])
ax.axis([0, 1100, 0, 1_100_000])

# 确保y轴上的刻度标签使用普通格式(即不使用科学计数法)
#ax.ticklabel_format(style='plain')

# 设置刻度标记的样式
ax.tick_params(labelsize=14)

# 将绘图保存到文件中
# plt.savefig('文件名', bbox_inches='tight')
# 第二个实参指定将绘图多余的空白区域裁剪掉
plt.savefig('squares_plot.png', bbox_inches='tight')

# 在 Matplotlib 查看器中显示绘图
plt.show()