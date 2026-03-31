with open('README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if 'SYSTEM ONLINE' in line or 'do the work' in line or '◈' in line:
        pass
    else:
        new_lines.append(line)

final_lines = []
for line in new_lines:
    if line.strip() == '`':
        continue 
    final_lines.append(line)

with open('README.md', 'w', encoding='utf-8') as f:
    f.writelines(final_lines)
