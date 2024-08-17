import pdfplumber


def get_text_from_pdf(pdf_path):
    # Otvorenie PDF súboru
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        # Prejdenie cez všetky stránky v PDF
        for page in pdf.pages:
            text += page.extract_text()
    return text



def main():
    text = get_text_from_pdf("blackdog/2024-08-13_22-40-19.pdf")
    print(text)
    text = get_text_from_pdf("plznicka/2024-08-13_22-40-16.pdf")
    print(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n{text}")
    text = get_text_from_pdf("radnicna/2024-08-13_22-40-20.pdf")
    print(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n{text}")

if __name__ == "__main__":
    main()
    
    
    