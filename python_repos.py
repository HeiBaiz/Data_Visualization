import requests

# 执行 API 调用并查看响应
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# 将响应转换为字典
response_dict = r.json()

# 处理结果
print(response_dict.keys())