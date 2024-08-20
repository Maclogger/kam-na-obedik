from datetime import datetime
import re
from ...main.tools.requester import *
from ...main.tools.pdf_parser import *
from ...main.tools.html_to_png import *
from ...main.tools.template_parser import *
from bs4 import BeautifulSoup

url = "https://www.zilinskakozlovna.sk/sk/menu/obedove-menu"
core = "Python/restauracie/kozlovna"
save_dir = f"{core}/output"
print_enabled = True

def main(v_print_enabled=True):
    global print_enabled
    print_enabled = v_print_enabled
    
    pic_path = f"{save_dir}/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png"


    req = SimpleRequest(base_url=url)
    html_content = req.get("/")
    soup = req.parse_html(html_content)
    
    # Nájdeme prvý <div> s triedou "MenuHead"
    main_element = soup.find('main')
    hladany_div = find_div_with_most_text(main_element)
    
    html_path = f"{core}/assets/temp.html"
    insert_div_into_template(f"{core}/assets/template.html", html_path, str(hladany_div))
    
    pic_path = f"{save_dir}/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png"
    
    from_html_file_to_png(html_path, pic_path, width=620)
    

if __name__ == "__main__":
    main()