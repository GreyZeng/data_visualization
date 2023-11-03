from die import Die
import plotly.express as px

die_1 = Die()
die_2 = Die(10)

results = []

for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
# install ploty, pandas 两个模块
title = "Results of Rolling a D6 and a D10 50,000 times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# 进一步定制图形
# 指定了x轴上刻度标记的间距
fig.update_layout(xaxis_dtick=1)

fig.show()
# 写入 html 文件中
# fig.write_html('dice_visual_d6d10.html')
