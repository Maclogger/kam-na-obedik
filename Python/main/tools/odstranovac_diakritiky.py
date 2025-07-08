import unicodedata

def _strip_diacritics_char(ch: str) -> str:
    """
    Odstráni diakritiku z jedného znaku.
    """
    decomposed = unicodedata.normalize('NFD', ch)
    return ''.join(
        c for c in decomposed
        if not unicodedata.combining(c)
    )

def odstran_diakritiku(text: str) -> str:
    """
    Odstráni diakritiku z celého reťazca.
    """
    return ''.join(_strip_diacritics_char(ch) for ch in text)

if __name__ == "__main__":
    sample = "čšťľ Žůžo"
    print(odstran_diakritiku(sample))  # vypíše: cstl Zuzo