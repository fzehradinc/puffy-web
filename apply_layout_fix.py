import re

file_path = 'puffy-main.html'

with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# 1. Fix broken comments (universal replacement)
# We already did some, but let's ensure all < !-- are <!--
content = content.replace('< !--', '<!--')

# 2. Hardening the CSS grid
# Current .lm-tall { grid-row: span 3; }
# New .lm-tall { grid-column: 1; grid-row: 1 / span 3; }
content = re.sub(
    r'\.lm-tall\s*\{\s*grid-row:\s*span 3;\s*\}', 
    '.lm-tall { grid-column: 1; grid-row: 1 / span 3; }', 
    content
)

# Current .lm-wide { grid-column: span 2; }
# New .lm-wide { grid-column: 2 / span 2; grid-row: 3; }
content = re.sub(
    r'\.lm-wide\s*\{\s*grid-column:\s*span 2;\s*\}', 
    '.lm-wide { grid-column: 2 / span 2; grid-row: 3; }', 
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied HTML comment fixes and explicit CSS grid positioning.")
