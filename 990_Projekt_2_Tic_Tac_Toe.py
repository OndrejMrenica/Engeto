def vygeneruj_matici(nradku, nsloupcu):
    matrix = [[0]*nsloupcu for i in range(nradku)]
    return matrix

def vykresli_matici(matice, znak1, znak2):
    for radek in matice:
        text = ""
        for symbol in radek:
            if symbol == 0:
                text += " |"
            elif symbol == 1:
                text += znak1
            elif symbol == 2:
                text += znak2
            else:
                text+= "?|"
        print(text[:-1])
        radek = "-"*len(matice[0]*2)
        print(radek[:-1])

def vitezstvi_radku(matice, hrac):
    for radek in matice:
        vitezstvi = True
        for symbol in radek:
            if symbol != hrac:
                vitezstvi = False
        if vitezstvi:
            return True
    return False

def vitezstvi_sloucu(matice, hrac):
    nradku = len(matice)
    nsloupcu = len(matice[0])
    for jsloupec in range(nsloupcu):
        vitezstvi = True
        for iradek in range(nradku):
            if matice[iradek][jsloupec] != hrac:
                vitezstvi = False
        if vitezstvi:
            return True
    return False

def vitezstvi_diagonal_1(matice, hrac):
    rozmer = len(matice[0])
    vitezstvi = True
    for i in range(rozmer):
        if matice[i][i] != hrac:
            vitezstvi = False
    if vitezstvi:
            return True
    return False

def vitezstvi_diagonal_2(matice, hrac):
    rozmer = len(matice[0])
    vitezstvi = True
    for i in range(rozmer):
        if matice[i][(rozmer-1)-i] != hrac:
            vitezstvi = False
    if vitezstvi:
            return True
    return False

def preved_na_pozici(cislo,nsloupcu):
    cislo -= 1
    radek = cislo//nsloupcu
    sloupec = cislo % nsloupcu
    return radek, sloupec

def pocitani_tahu(tah):
    if tah % 2 == 0:
        ihrac = "Hráč 2"
    else:
        ihrac = "Hráč 1"
    return ihrac

def main():
    oddelovac = ("-"*80)
    print(oddelovac)
    print("Vítej ve hře piškvorky, zadávej čísla v rozsahu od 1 do 9 pro určení pole:")
    print(oddelovac)
    znak1 = input("Hráč 1 - vyber si libovolný znak: ")+("|")
    znak2 = input("Hráč 2 - vyber si libovolný znak: ")+("|")

    piskvorky = vygeneruj_matici(3,3)
    game_on = True
    tah = 1
    zvolene_tahy = []
    while game_on:
        print(oddelovac)
        print(pocitani_tahu(tah))
        cislo = input("Zadej pozici 1-9: ")

#Kontrola jiných než číselných vstupů
        if not cislo.isdigit():
            print("Zadal si neplatný vstup!")
            continue

#Kontrola rozsahu čísel
        cislo = int(cislo)
        if cislo not in range(1,10):
            print("Zadal si neplatný rozsah čísel!")
            continue

#Prepisovani tahu
        if cislo not in zvolene_tahy:
            zvolene_tahy.append(cislo)
        else:
            print("Na toto pole již nelze zapisovat!")
            continue

        radek, sloupec = preved_na_pozici(cislo,3)
        symbol = 2 if tah % 2 == 0 else 1
        piskvorky[radek][sloupec] = symbol
        vykresli_matici(piskvorky,znak1,znak2)

#Vyhodnoceni remizy
        if tah == 9:
            print("GAME OVER - Remíza")
            game_on = False

#Vyhodnoceni_vyhry
        if vitezstvi_sloucu(piskvorky,symbol) or vitezstvi_radku(piskvorky,symbol) or vitezstvi_diagonal_1(piskvorky,symbol) or vitezstvi_diagonal_2(piskvorky,symbol):
            print("Vitezstvi", pocitani_tahu(tah))
            game_on = False
        tah += 1

if __name__ == "__main__":
    main()
