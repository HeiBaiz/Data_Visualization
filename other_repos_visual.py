import requests
import plotly.express as px

# 定义要查询的语言列表
languages = ["JavaScript", "Ruby", "C", "Java", "Perl", "Haskell", "Go"]

# 初始化一个字典来存储每种语言的前三个仓库信息
top_repos_dict = {language: [] for language in languages}

# 遍历每种语言进行 API 调用
for language in languages:
    # 构建 API 请求 URL
    url = f"https://api.github.com/search/repositories?q=language:{language}+sort:stars+stars:>10000"
    
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    print(f"Status code for {language}: {r.status_code}")

    # 将响应转换为字典
    response_dict = r.json()
    
    # 获取前三个仓库的信息
    for repo_dict in response_dict['items'][:3]:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        stars = repo_dict['stargazers_count']
        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        hover_text = f"{owner}<br />{description}"
        
        top_repos_dict[language].append({
            'repo_link': repo_link,
            'stars': stars,
            'hover_text': hover_text,
            'language': language
        })

# 将所有数据合并到一个列表中
all_repos = [repo for repos in top_repos_dict.values() for repo in repos]

# 提取数据
repo_links = [repo['repo_link'] for repo in all_repos]
stars = [repo['stars'] for repo in all_repos]
hover_texts = [repo['hover_text'] for repo in all_repos]
languages = [repo['language'] for repo in all_repos]

# 可视化
title = "Top 3 Projects for Each Language on GitHub"
labels = {'x': 'Repository', 'y': 'Stars', 'color': 'Language'}
fig = px.bar(x=repo_links, y=stars, color=languages, title=title, labels=labels,
             hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20, xaxis_tickangle=-45)

fig.update_traces(marker_opacity=0.6)

fig.show()