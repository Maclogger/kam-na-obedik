import os
import shutil
from glob import glob
from datetime import datetime
from bs4 import BeautifulSoup

def update_html_file(nazov_rest, timestamp):
    html_file_path = "Web/index.html"
    
    # Načítanie a parsovanie HTML súboru
    with open(html_file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Nájdeme príslušný <p> element podľa ID a aktualizujeme jeho text
    p_element = soup.find("p", id=f"{nazov_rest}_update")
    if p_element:
        p_element.string = f"Aktualizované: {timestamp}"
    else:
        print(f"Varovanie: ID '{nazov_rest}_update' nebolo nájdené v HTML súbore.")

    # Uloženie zmien do HTML súboru
    with open(html_file_path, "w", encoding="utf-8") as file:
        file.write(str(soup))
    print(f"HTML súbor bol aktualizovaný pre '{nazov_rest}' s časovou značkou {timestamp}.")

def najdi_najnovsi_a_prekopiruj(nazov_rest, pripona):
    input_dir = f"Python/restauracie/{nazov_rest}/output/"
    output_dir = f"Web/data/{nazov_rest}/"
    output_filename = f"{nazov_rest}.{pripona}"

    # Získanie všetkých súborov s danou príponou v input_dir
    files = glob(os.path.join(input_dir, f"*.{pripona}"))

    if not files:
        print(f"Nebol nájdený žiaden súbor: [{nazov_rest}] [.{pripona}]")
        return
    
    latest_file = max(files, key=os.path.getctime)

    # Cieľová cesta pre súbor
    destination = os.path.join(output_dir, output_filename)

    # Skopírovanie súboru do nového umiestnenia
    shutil.copy2(latest_file, destination)
    print(f"Súbor {latest_file} bol skopírovaný do {destination}.")

    # Získanie aktuálneho času vo formáte DD.MM.YYYY - HH:MM
    timestamp = datetime.now().strftime("%d.%m.%Y - %H:%M")

    # Aktualizácia HTML súboru
    update_html_file(nazov_rest, timestamp)
    

def main():
    najdi_najnovsi_a_prekopiruj("plznicka", "png")
    najdi_najnovsi_a_prekopiruj("plznicka", "pdf")
    
    najdi_najnovsi_a_prekopiruj("blackdog", "png")
    najdi_najnovsi_a_prekopiruj("blackdog", "pdf")
    
    najdi_najnovsi_a_prekopiruj("radnicna", "png")
    najdi_najnovsi_a_prekopiruj("radnicna", "pdf")
    
    najdi_najnovsi_a_prekopiruj("makalu", "png")

if __name__ == "__main__":
    main()
