with open('README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if 'SYSTEM ONLINE  ·  AI AGENT STACK INITIALIZED  ·  BUILDING...' in line:
        pass
    elif 'do the work  ·  trust the process  ·  ship' in line:
        pass
    elif '◈━━━━' in line:
        pass
    else:
        new_lines.append(line)

# Now we need to manually insert the blockquote strings in place of the empty tags.
final_lines = []
for line in new_lines:
    if line.strip() == '\\\':
        continue # Drop all remaining codeblock strings meant for those ascii boxes
    final_lines.append(line)

with open('README.md', 'w', encoding='utf-8') as f:
    f.writelines(final_lines)
