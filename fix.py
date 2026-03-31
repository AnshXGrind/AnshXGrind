import re

with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Emojis and characters to fix
rep = {
    'âš¡': '⚡',
    'Â·': '·',
    'ðŸ¤–': '🤖',
    'ðŸ’»': '💻',
    'ðŸš€': '🚀',
    'ðŸ“Š': '📊',
    'ðŸ†': '🏆',
    'ðŸ“ˆ': '📈',
    'â±ï¸': '⏱️',
    'âœï¸': '✍️',
    'ðŸŽ§': '🎧',
    'ðŸ”—': '🔗',
    'â—ˆ': '◈',
    'â”': '━',
}

for k, v in rep.items():
    text = text.replace(k, v)

# The problematic ones that contain strange bytes
text = re.sub(r'ðŸ§.', '🧠', text)
text = re.sub(r'ðŸ›.ï¸', '🛠️', text)
text = re.sub(r'ðŸ .CONTRIBUTION', '🐍 CONTRIBUTION', text)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)

