import math

#proměnné
def parse(vstup):
    try:
        x_y, zkratka = vstup.strip().split(':')
        x, y = x_y.split(',')
        x = float(x)
        y = float(y)
        return (x, y, zkratka.strip())
    except ValueError:
        raise ValueError("ERROR.")

def vypocet_vzdalenosti(letadlo1, letadlo2):
    return math.sqrt((letadlo1[0] - letadlo2[0])**2 + (letadlo1[1] - letadlo2[1])**2)

def main():
    letadla = []
    
    print("Zadejte souřadnice a označení letadel ve formátu 'x,y:označení'.")
    print("Pro ukončení zadávání zadejte prosím prázdný řádek.")
    
    while True:
        vstup = input()
        if not vstup:
            break
        try:
            x, y, zkratka = parse(vstup)
            letadla.append((x, y, zkratka))
        except ValueError as e:
            print(e)
            return
        
    if len(letadla) < 2:
        print("ERROR.")
        return
    
    min_vzdal = float('inf')
    nejblizsi = []

#porovnání

    for i in range(len(letadla)):
        for j in range(i+1, len(letadla)):
            vzdalenost = vypocet_vzdalenosti(letadla[i], letadla[j])
            if vzdalenost < min_vzdal:
                min_vzdal = vzdalenost
                nejblizsi = [(letadla[i][2], letadla[j][2])]
            elif vzdalenost == min_vzdal:
                nejblizsi.append((letadla[i][2], letadla[j][2]))

# Výstup
    print("Vzdálenost nejbližších letadel:", min_vzdal)
    print("Počet nalezených dvojic:", len(nejblizsi))
    for par in nejblizsi:
        print(f"{par[0]} - {par[1]}")

if __name__ == "__main__":
    main()
