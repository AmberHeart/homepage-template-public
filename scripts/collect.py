# 生成一个all.md文件，将各个include片段合并为一个完整的Markdown文件

# 各个需要合并的片段文件
includes = [
    '_pages/includes/intro.md',
    '_pages/includes/news.md',
    '_pages/includes/pub.md',
    '_pages/includes/honors.md',
    '_pages/includes/talks.md',
    '_pages/includes/services.md',
    '_pages/includes/others.md'
]

# 开头的YAML front matter
yaml_header = '''---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---
'''

output_lines = [yaml_header, '']  # front matter和空行

# 依次读取片段内容并追加
for path in includes:
    with open(path, 'r', encoding='utf-8') as f:
        output_lines.append(f.read())
        output_lines.append('')  # 分隔空行

# 写入all.md
with open('all.temp', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines).lstrip('\n'))  # 去除多余起始空行

print("all.temp文件已根据各include片段合成")