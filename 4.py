#proměnné
def find(sekvence):
    n = len(sekvence)
    intervaly = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            if j - i >= 2:
                interval = sekvence[i:j]
                intervaly.append((i, j, sum(interval)))
    return intervaly

def cnt_rovno(intervaly):
    rovno = {}
    for i in range(len(intervaly)):
        for j in range(i + 1, len(intervaly)):
            if intervaly[i][2] == intervaly[j][2]:
                par = (intervaly[i][:2], intervaly[j][:2])
                rovno[par] = intervaly[i][2]
    return rovno

#main
def main():
    sekvence = []
    try:
        while True:
            cis = input("Zadej číslo: ")
            if cis == "":
                if len(sekvence) == 0:
                    print("Vstupní posloupnost je prázdná.")
                break
            sekvence.append(int(cis))
            print("Číslo", cis, "bylo úspěšně přijato.")
    except EOFError:
        pass
    if len(sekvence) > 2000:
        print("Vstupní posloupnost je příliš dlouhá (přes 2000 čísel).")
        return
    intervaly = find(sekvence)
    if len(intervaly) == 0:
        print("Vstupní posloupnost je prázdná.")
        return
    rovno = cnt_rovno(intervaly)
    print("Počet nalezených dvojic intervalů se stejným součtem:", len(rovno))


if __name__ == "__main__":
    main()