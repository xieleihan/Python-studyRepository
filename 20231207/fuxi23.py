"""
    敏感词过滤
"""

# 定义敏感词列表
not_words = ['fuck','shit', 'bitch', 'cunt', 'pussy', 'bastard', 'asshole', 'dick', 'boob', 'boobies', 'boobs', 'cock', 'cocks', 'nigger', 'niggers', 'nigga', 'niggas', 'penis', 'penises', 'fucking','shitting', 'bitching', 'cunting', 'pussying', 'bast']
content = input('请输入内容：')

# 过滤
def filter_content(words, string):
    for w in words:
        string = string.replace(w, '*' * len(w))
    return string

print(f"过滤前：{content}")
result = filter_content(not_words, content)
print(f"过滤后：{result}")