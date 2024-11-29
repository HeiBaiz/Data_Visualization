import requests

# 定义要查询的语言列表
languages = ["JavaScript", "Ruby", "C", "Java", "Perl", "Haskell", "Go"]

# 初始化一个列表来存储所有仓库的信息
all_repo_dicts = []

# 遍历每种语言进行 API 调用
for language in languages:
    # 构建 API 请求 URL
    url = f"https://api.github.com/search/repositories?q=language:{language}+sort:stars+stars:>10000"
    
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    print(f"Status code for {language}: {r.status_code}")

    # 将响应转换为字典
    response_dict = r.json()
    
    # 将当前语言的仓库信息添加到总列表中
    all_repo_dicts.extend(response_dict['items'])

# 打印总的仓库数量
print(f"Total repositories: {len(all_repo_dicts)}")

# 研究有关仓库的信息
print("\nSelected information about each repository:")
for repo_dict in all_repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")
    print(f"Language: {repo_dict['language']}")
    print("\n")