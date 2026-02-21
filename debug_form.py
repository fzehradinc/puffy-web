import re

file_path = 'puffy-main.html'
with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

print("File loaded, searching for form...")

# Find the form HTML
form_match = re.search(r'<form[^>]*class="booking-form"[^>]*>', content)
if form_match:
    start = form_match.start()
    print('--- FORM HTML START ---')
    # Look for closing </form>
    form_end = content.find('</form>', start)
    if form_end != -1:
        print(content[start:form_end+7])
    else:
        print(content[start:start+2000])
else:
    print('Form tag with class "booking-form" not found')

# Find script related to form submission
# Searching for common patterns like event listeners on the form
script_match = re.search(r'document\.querySelector\("\.booking-form"\)', content)
if script_match:
    start = script_match.start()
    print('\n--- SCRIPT SNIPPET ---')
    print(content[start:start+4000])
else:
    # Try searching for fetch or spreadsheet related keywords
    script_match = re.search(r'fetch\(', content)
    if script_match:
        # Filter for scripts that look like they are sending data
        all_fetches = [m.start() for m in re.finditer(r'fetch\(', content)]
        for f_idx in all_fetches:
            snippet = content[f_idx:f_idx+500]
            if 'form' in snippet.lower() or 'google' in snippet.lower() or 'script' in snippet.lower():
                print(f'\n--- FETCH SCRIPT at {f_idx} ---')
                print(content[f_idx:f_idx+3000])
                break
    else:
        print('No submission script or fetch found')
