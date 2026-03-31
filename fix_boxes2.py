import re
with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace top block
text = re.sub(r'`[\s\S]*?SYSTEM ONLINE[\s\S]*?`', '> **SYSTEM ONLINE  ·  AI AGENT STACK INITIALIZED  ·  BUILDING...**', text, count=1)

# Replace bottom block
text = re.sub(r'`[\s\S]*?do the work[\s\S]*?`', '> **DO THE WORK  ·  TRUST THE PROCESS  ·  SHIP**', text, count=1)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)
