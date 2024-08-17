from datetime import datetime
import re
from requester import *
from pdf_parser import *
from html_to_png import *

url = "https://restauracie-makalu.sk/weekly"
save_dir = "makalu"
print_enabled = True

def insert_div_into_template(template_path, output_path, div_content):
    # Načítanie templatu
    with open(template_path, 'r', encoding='utf-8') as file:
        template_html = file.read()

    # Nahradenie markeru "__INSERT_HERE__" obsahom divu
    new_html = re.sub(r'<div id="__INSERT_HERE__"></div>', div_content, template_html)

    # Uloženie výsledného HTML do nového súboru
    with open(output_path, 'w', encoding='utf-8') as new_file:
        new_file.write(new_html)

    print(f"Nový súbor bol úspešne vytvorený: {output_path}")


def main():
    req = SimpleRequest(base_url=url)
    html_content = req.get("/")
    soup = req.parse_html(html_content)
    
    # Nájdeme prvý <div> s triedou "MenuHead"
    menu_head_div = soup.find('div', class_='MenuHead')
    
        
    # Nájdeme prvého rodiča, ktorý má triedu "pageWidth"
    div = menu_head_div.find_parent(class_='pageWidth')
    
    html_path = f"{save_dir}/temp.html"
    insert_div_into_template(f"{save_dir}/template.html", html_path, str(div))
    
    pic_path = f"{save_dir}/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png"
    
    from_html_file_to_png(html_path, pic_path, width=900)

    combine_images(pic_path, f"{save_dir}/logo_makalu.png", pic_path, scale_factor=2.5)

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    