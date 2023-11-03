from pathlib import Path
import json

# 将数据转换为字符串读取并转换为Python对象
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# 将数据文件转换为更容易阅读的版本
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# 查看数据集中的所有地震
all_eq_dicts = all_eq_data['features']
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
# 打印前十次地震的震级
print(mags[:10])
