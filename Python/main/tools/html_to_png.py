import os
import imgkit
from PIL import Image


def from_html_file_to_png(html_path, image_path, width=None, height=None):
    # Ensure the directory for the image exists
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    # Convert HTML to PNG
    try:
        options = {'quiet': ''}
        
        if width:
            options['width'] = width
        if height:
            options['height'] = height
            
        imgkit.from_file(html_path, image_path, options=options)
        #print(f"Successfully converted {html_path} to {image_path}")
    except Exception as e:
        print(f"Failed to convert {html_path} to {image_path}: {e}")

def combine_images(bg_image_path, fg_image_path, output_path, scale_factor=1):
    # Otvorenie obrázkov
    bg_image = Image.open(bg_image_path)  # Väčší obrázok (pozadie)
    fg_image = Image.open(fg_image_path)  # Menší obrázok (logo)

    # Získanie rozmerov obrázkov
    bg_width, bg_height = bg_image.size
    fg_width, fg_height = fg_image.size

    # Zväčšenie menšieho obrázku podľa zvoleného scale factoru
    new_fg_width = int(fg_width * scale_factor)
    new_fg_height = int(fg_height * scale_factor)
    fg_image = fg_image.resize((new_fg_width, new_fg_height), Image.LANCZOS)

    # Aktualizácia rozmerov loga po zmene veľkosti
    fg_width, fg_height = fg_image.size

    # Vytvorenie nového obrázka s výškou pozadia + výška zväčšeného loga
    new_height = bg_height + fg_height
    new_image = Image.new("RGB", (bg_width, new_height), (255, 255, 255))  # Biele pozadie

    # Umiestnenie loga hore na biele pozadie
    new_image.paste(fg_image, ((bg_width - fg_width) // 2, 0), fg_image)

    # Umiestnenie pozadia (väčšieho obrázku) pod logo
    new_image.paste(bg_image, (0, fg_height))

    # Uloženie výsledného obrázka
    new_image.save(output_path)

def main():
    combine_images("makalu/2024-08-15_00-03-37.png", "makalu/logo_makalu.png", "makalu/output.png", scale_factor=2.5)

    # Specify the input HTML file and output image file paths
    #from_html_file_to_png("makalu/makalu.html", "makalu/screenshot.png")

if __name__ == "__main__":
    main()
