import re

with open('puffy-main.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

def find_class_css(class_name):
    pattern = rf'\.{class_name}\s*\{{[^}}]*\}}'
    match = re.search(pattern, content)
    if match:
        return match.group(0)
    return f"Class {class_name} not found"

print(find_class_css('lifestyle-mosaic'))
print(find_class_css('lm-tall'))
print(find_class_css('lm-wide'))
