from ..restauracie.plznicka import plznicka
from ..restauracie.blackdog import blackdog
from ..restauracie.radnicna import radnicna
from ..restauracie.makalu import makalu

def spusti(func, nazov_restauracie, stats):
    stats[1] += 1
    print(f"\n{nazov_restauracie} loading...")
    try:
        func(False)
        print(f"{nazov_restauracie} DONE.")
        stats[0] += 1
    except:
        print(f"Aktualizácia reštaurácie '{nazov_restauracie}' zlyhala. :(")
        return False

def main():
    stats = [0, 0] # 0 -> počet úspešných, 1 -> počet všetkých
    spusti(plznicka.main, "Plznička", stats)
    spusti(blackdog.main, "Blackdog", stats)
    spusti(radnicna.main, "Radničná", stats)
    spusti(makalu.main, "Makalu", stats)
    uspesnost = stats[0] / stats[1] * 100
    print(f"\n\nÚspešnosť: {uspesnost}% - {stats[0]}/{stats[1]}\n")

if __name__ == "__main__":
   main()
   
    













    