

def get_content(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
