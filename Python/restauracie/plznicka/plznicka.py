from datetime import datetime
import re
from ...main.tools.requester import *
from ...main.tools.pdf_parser import *

url = "https://plznicka.sk/denne-menu/"
save_dir = "Python/restauracie/plznicka/output"
print_enabled = True

def get_hladany_url_na_pdf(req):
    html_content = req.get("/")
    
    if html_content:
        # Regulárny výraz na vyhľadanie všetkých href odkazov končiacich na .pdf
        pdf_links = re.findall(r'href="(.*?\.pdf)\s*"', html_content)
        
        hladany_link = ""
        for link in pdf_links:
            if (print_enabled):
                print(f"Nájdený link na menu: {link}")
            if "jedalny" not in link and "vikend" not in link and "víkend" not in link and "napoj" not in link and "nápoj":
                hladany_link = link
            
        if (print_enabled):
            print(f"\nHľadané menu: {hladany_link}")
        return hladany_link
    
def skus_ziskat_pdf():
    req = SimpleRequest(base_url=url)
    url_menu_pdf = get_hladany_url_na_pdf(req)
    
    if not url_menu_pdf:
        return None
    
    # Získame aktuálny dátum a čas
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Vytvoríme názov súboru s cestou
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    save_path = os.path.join(save_dir, f"{current_datetime}.pdf")
    
    # Stiahneme a uložíme PDF
    req.download_pdf(url_menu_pdf, save_path)
    
    return save_path

def main(v_print_enabled=True):
    global print_enabled
    print_enabled = v_print_enabled
    pdf_path = skus_ziskat_pdf()
    nazov = pdf_path[:-4]
    convert_pdf_to_image(pdf_path, f"{nazov}.png")
    return nazov
    
    
if __name__ == "__main__":
    main()
    
    
    

















