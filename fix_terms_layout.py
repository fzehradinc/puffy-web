import re

file_path = 'puffy-terms.html'

with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# 1. Fix broken comments
content = content.replace('< !--', '<!--')

# 2. Harden CSS for sidebar and content
# Update .terms-sidebar to include grid-column: 1; explicitly
content = re.sub(
    r'(\.terms-sidebar\s*\{[^}]*position:\s*sticky;)', 
    r'\1 grid-column: 1;', 
    content
)

# Update .terms-content to include grid-column: 2; explicitly
content = re.sub(
    r'(\.terms-content\s*\{[^}]*padding:\s*56px\s*0\s*56px\s*64px;)', 
    r'\1 grid-column: 2;', 
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied fixes to puffy-terms.html")
