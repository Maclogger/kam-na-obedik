import plznicka
import blackdog
import radnicna

def spusti(func, nazov_restauracie, stats):
    stats[1] += 1
    print(f"{nazov_restauracie} loading...")
    try:
        func(False)
        print(f"{nazov_restauracie} DONE. :D")
        stats[0] += 1
    except:
        print(f"Aktualizácia reštaurácie '{nazov_restauracie}' zlyhala. :(")
        return False

def main():
    stats = [0, 0] # 0 -> počet úspešných, 1 -> počet všetkých
    spusti(plznicka.main, "Plznička", stats)
    spusti(blackdog.main, "Blackdog", stats)
    spusti(radnicna.main, "Radničná", stats)
    uspesnost = stats[0] / stats[1] * 100
    print(f"Úspešnosť: {uspesnost}% - {stats[0]}/{stats[1]}")

if __name__ == "__main__":
   main()
    
    













    