import re

with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace top block
top_pattern = re.compile(r'`\n[^]*SYSTEM ONLINE.*?`\n', re.DOTALL)
top_replacement = """> **SYSTEM ONLINE · AI AGENT STACK INITIALIZED · BUILDING...**\n"""
text = top_pattern.sub(top_replacement, text)

# Replace bottom block
bottom_pattern = re.compile(r'`\n[^]*do the work.*?`\n', re.DOTALL)
bottom_replacement = """> **DO THE WORK · TRUST THE PROCESS · SHIP**\n"""
text = bottom_pattern.sub(bottom_replacement, text)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)
