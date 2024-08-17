from pdf2image import convert_from_path
from PIL import Image
import os
import numpy as np

def convert_pdf_to_image(pdf_file_path, output_image_path="output_image.png"):
    """
    Prevod PDF súboru na jeden obrázok (PNG).

    Args:
        pdf_file_path (str): Cesta k PDF súboru.
        output_image_path (str, optional): Cesta a názov pre výsledný obrázok. Default je 'output_image.png'.
        poppler_path (str, optional): Cesta k priečinku, kde je nainštalovaný Poppler.
    """

    # Overenie, či PDF súbor existuje
    if not os.path.exists(pdf_file_path):
        print(f"Súbor {pdf_file_path} neexistuje. :(")
        return
    
    try:
        # Konvertovanie PDF na obrázky
        images = convert_from_path(pdf_file_path)
        
        # Spojenie obrázkov do jedného (vertikálne)
        result_image = Image.fromarray(
            np.vstack([np.asarray(image) for image in images])
        )

        # Uloženie výsledného obrázku
        result_image.save(output_image_path)
        #print(f"Výsledný obrázok bol uložený ako {output_image_path}")
        
    except Exception as e:
        print(f"Nastala chyba pri konverzii: {e} :(")

if __name__ == "__main__":
    convert_pdf_to_image("radnicna\\2024-08-13_21-18-01.pdf", "obrazok.png")




# Príklad použitia:
# convert_pdf_to_image("cesta_k_tvojmu_pdf.pdf", "vysledny_obrazok.png")
