import re, sys

with open('puffy-main.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Remove base64 data URIs first
content_clean = re.sub(r'data:image/[^;]+;base64,[A-Za-z0-9+/=]{50,}', '[IMG]', content)

# Find lifestyle-mosaic section in HTML body
all_positions = [m.start() for m in re.finditer(r'lifestyle-mosaic', content_clean)]
print("All positions:", all_positions)

# The CSS section ends around position 37000 based on </style> tag
style_end = content_clean.find('</style>')
print(f"Style ends at: {style_end}")

# Find HTML occurrence after style section
for pos in all_positions:
    if pos > style_end:
        print(f"\nHTML occurrence at: {pos}")
        snippet = content_clean[pos-300:pos+4000]
        # Write to file for easier reading
        with open('mosaic_snippet.txt', 'w', encoding='utf-8') as out:
            out.write(snippet)
        print("Written to mosaic_snippet.txt")
        break
