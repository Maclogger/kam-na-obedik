from datetime import datetime
import re
from ...main.tools.requester import *
from ...main.tools.pdf_parser import *
from ...main.tools.odstranovac_diakritiky import *

url = "https://plznicka.sk/denne-menu/"
save_dir = "Python/restauracie/plznicka/output"
print_enabled = True

def black_list_check(link):
    black_list = ["jedalny", "vikend", "napoj"]
    for black_list_word in black_list:
        if black_list_word in link:
            return False
    return True

def white_list_check(link) -> int:
    # All white list words has to be present!
    white_list = ["abc"]
    white_list_count = 0
    for white_list_word in white_list:
        if white_list_word in link:
            white_list_count += 1
    return white_list_count

class Link:
    def __init__(self, link_url):
        self.link_url = link_url
        self.link_cisty = odstran_diakritiku(self.link_url)
        self.link_cisty = self.link_cisty.lower()
        self.white_list_count = white_list_check(self.link_cisty)

def find_hladany_link_podla_white_filtru(links: []):
    linksObjects = []
    for link in links:
        linksObjects.append(Link(link))

    linksObjects.sort(reverse=True, key=lambda x: x.white_list_count)
    return linksObjects[0].link_url

def get_hladany_url_na_pdf(req):
    html_content = req.get("/")
    
    if html_content:
        # Regulárny výraz na vyhľadanie všetkých href odkazov končiacich na .pdf
        pdf_links = re.findall(r'href="(.*?\.pdf)\s*"', html_content)


        filtered_links = []
        for link in pdf_links:
            link_cisty = odstran_diakritiku(link)
            link_cisty = link_cisty.lower()
            if print_enabled:
                print(f"Nájdený link na menu: {link}")

            if not black_list_check(link_cisty):
                continue

            filtered_links.append(link)


        hladany_link = find_hladany_link_podla_white_filtru(filtered_links)

        if print_enabled:
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
    
    
    

















