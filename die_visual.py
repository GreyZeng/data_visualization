from die import Die

die = Die()

results = []

for roll_num in range(100):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
pass_results = range(1, die.num_sides + 1)
for value in pass_results:
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)
