from pathlib import Path
import csv

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# enumerate 方法用于获取每个元素的索引和值
for index, column_header in enumerate(header_row):
    print(index, column_header)
# print(header_row)
