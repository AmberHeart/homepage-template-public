# 将all.md文件分割为各个include片段
import os

# 需要和collect.py中的includes顺序/路径保持一致
includes = [
    '_pages/includes/intro.md',
    '_pages/includes/news.md',
    '_pages/includes/pub.md',
    '_pages/includes/honors.md',
    '_pages/includes/talks.md',
    '_pages/includes/services.md',
    '_pages/includes/others.md'
]

# 读取all.md文件
with open('all.md', 'r', encoding='utf-8') as file:
    content = file.read()

# 跳过YAML front matter（---到---）
lines = content.splitlines(keepends=True)
start_idx, end_idx = None, None
dash_count = 0
for i, line in enumerate(lines):
    if line.strip() == '---':
        dash_count += 1
        if dash_count == 1:
            start_idx = i
        elif dash_count == 2:
            end_idx = i
            break
if end_idx is not None and end_idx + 1 < len(lines):
    content_no_yaml = ''.join(lines[end_idx+1:]).lstrip('\n')
else:
    content_no_yaml = content

# 分割各部分。每个section之间假设是通过空行分隔的（收集时已加入空行）。
sections = [s.strip('\n') for s in content_no_yaml.split('\n\n') if s.strip()]

# 若数量对不上，简单做一下对齐
if len(sections) != len(includes):
    print(f"警告：实际片段（{len(sections)}）与模板数（{len(includes)}）不一致。")
    # 简单补齐/截断
    if len(sections) < len(includes):
        sections += [''] * (len(includes) - len(sections))
    else:
        sections = sections[:len(includes)]

# 写回各分片
for path, section in zip(includes, sections):
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(section.strip('\n') + '\n')
# 提示完成
print("all.md已按片段分割还原至includes。")