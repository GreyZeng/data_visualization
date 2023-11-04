import requests

# Github不稳定，下述代码运行可能也会不稳定
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status Code : {r.status_code}")

# 将响应文本转换成字典
response_dict = r.json()
# 处理结果
print(response_dict.keys())
