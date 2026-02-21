import re

file_path = 'puffy-main.html'
with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

print(f"File size: {len(content)}")

# Look for the script specifically handling the form submission
# Based on common patterns in these files:
# Usually there is an event listener on the form id or class
patterns = [
    r'document\.getElementById\("wholesaleLeadForm"\)',
    r'document\.querySelector\("\.booking-form"\)',
    r'\.addEventListener\("submit"',
    r'fetch\(',
    r'script\.google\.com'
]

for pattern in patterns:
    match = re.search(pattern, content)
    if match:
        start = max(0, match.start() - 500)
        end = min(len(content), match.end() + 5000)
        print(f"\n--- MATCH FOUND FOR: {pattern} at {match.start()} ---")
        print(content[start:end])
        # We only need the first good match for the logic
        if 'fetch' in pattern or 'google' in pattern:
            break

# Also check for input names in the form to see if they match expected headers
form_match = re.search(r'<form[^>]*class="booking-form"[^>]*>', content)
if form_match:
    f_start = form_match.start()
    f_end = content.find('</form>', f_start) + 7
    form_html = content[f_start:f_end]
    # Remove large blobs if any (like images)
    form_html_clean = re.sub(r'src="data:image/[^"]+"', 'src="[DATA]"', form_html)
    print("\n--- FORM HTML (CLEANED) ---")
    print(form_html_clean)
