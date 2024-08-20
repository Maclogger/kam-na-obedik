import re

def find_div_with_most_text(main_element):
    max_text_div = None
    max_text_length = 0

    for div in main_element.find_all('div'):
        div_text = div.get_text(strip=True)
        div_text_length = len(div_text)

        if div_text_length > max_text_length:
            max_text_length = div_text_length
            max_text_div = div

    return max_text_div

def insert_div_into_template(template_path, output_path, div_content, print_enabled=False):
    # Načítanie templatu
    with open(template_path, 'r', encoding='utf-8') as file:
        template_html = file.read()

    # Nahradenie markeru "__INSERT_HERE__" obsahom divu
    new_html = re.sub(r'<div id="__INSERT_HERE__"></div>', div_content, template_html)

    # Uloženie výsledného HTML do nového súboru
    with open(output_path, 'w', encoding='utf-8') as new_file:
        new_file.write(new_html)

    if print_enabled:
        print(f"Nový súbor bol úspešne vytvorený: {output_path}")
