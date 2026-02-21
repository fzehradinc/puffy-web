import re

with open('puffy-main.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Extract CSS block related to lifestyle-mosaic
# We saw earlier it started around line 771 in unminified or a specific index in minified
pattern = r'\.lifestyle-mosaic\s*\{[^}]+\}.*?\.lm-tall\s*\{[^}]+\}.*?\.lm-wide\s*\{[^}]+\}'
# Let's just find everything between .lifestyle-mosaic and the end of the style tag or 2000 chars
start_idx = content.find('.lifestyle-mosaic')
if start_idx != -1:
    css_snippet = content[start_idx : start_idx + 2000]
    print("CSS Snippet:")
    print(css_snippet)
else:
    print("Could not find .lifestyle-mosaic in CSS")
