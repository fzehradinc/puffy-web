file_path = 'puffy-main.html'
old_text = "const SHEETS_WEBHOOK_URL='YOUR_APPS_SCRIPT_WEB_APP_URL_HERE';"
new_text = "const SHEETS_WEBHOOK_URL='https://script.google.com/macros/s/AKfycbzChhFL1cWRn02WbK-gdObAhN5o85FBd1f2IJeWR1zs7VxnHK1JjAFiXIVy1OfFtk7YAQ/exec';"

with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

if old_text in content:
    content = content.replace(old_text, new_text)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated SHEETS_WEBHOOK_URL in puffy-main.html")
else:
    # Try a more flexible match if exact match fails
    import re
    new_content = re.sub(r"const SHEETS_WEBHOOK_URL\s*=\s*'[^']*'", new_text, content)
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated SHEETS_WEBHOOK_URL using regex")
    else:
        print("Could not find SHEETS_WEBHOOK_URL placeholder")
