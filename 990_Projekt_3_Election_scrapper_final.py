from bs4 import BeautifulSoup as bs
import requests
import sys
import csv

def get_nazvy_stran(soup):
    tables = soup.find_all("table")
    strany = []
    for j in range(1, len(tables)):
        rows = tables[j].find_all("tr")
        for i in range(2, len(rows)):
            cells = rows[i].find_all("td")
            strana = cells[1].contents[0]
            strany.append(strana)
    return strany

def get_vysledky_stran(soup):
    tables = soup.find_all("table")
    hlasy = []
    for j in range(1, len(tables)):
        rows = tables[j].find_all("tr")
        for i in range(2, len(rows)):
            cells = rows[i].find_all("td")
            hlasu = cells[2].contents[0]
            hlasy.append(hlasu)
    return hlasy

def statistika_new(soup):
    statistika = []
    volicu = soup.find('td', {'headers': 'sa2'})
    vyd_obalky = soup.find('td', {'headers': 'sa3'})
    platne = soup.find('td', {'headers': 'sa6'})
    if volicu is not None and vyd_obalky is not None and platne is not None:
        statistika.extend((volicu.text, vyd_obalky.text, platne.text))
    return statistika

def get_kod_obce(soup):
    headry = []
    headry += soup.select('td[headers="t1sa1 t1sb1"]')
    headry += soup.select('td[headers="t2sa1 t2sb1"]')
    headry += soup.select('td[headers="t3sa1 t3sb1"]')
    kody = []
    for h in headry:
        if h.find('a'):
            cislo_obce = h.find('a')
            kody.append(cislo_obce.text)
    return kody

def get_nazev_obce(soup):
    headry = []
    headry += soup.select('td[headers="t1sa1 t1sb2"]')
    headry += soup.select('td[headers="t2sa1 t2sb2"]')
    headry += soup.select('td[headers="t3sa1 t3sb2"]')
    nazvy_obci = []
    for header in headry:
        if header.text != '-':
            nazvy_obci.append(header.text)
        else:
            continue
    return nazvy_obci

def get_vysledky_obce(soup):
    vysledky = statistika_new(soup) + get_vysledky_stran(soup)
    return vysledky

def get_soup(adresa):
    try:
        r = requests.get(adresa)
    except:
        print("Chyba s vlozenim odkazu, zkontrolujte vlozeny odkaz! Nebo server nedostupný, opakujte!")
        sys.exit()
    return bs(r.text, "html.parser")

def vytvor_zahlavi(soup):
    prefix = ['Kod obce', 'Nazev obce', 'Registrovanych volicu', 'Vydano obalek', 'Platnych hlasu']
    nazvy = get_nazvy_stran(soup)
    zahlavi = prefix + nazvy
    return zahlavi

def get_odkazy_obci(soup_default):
    adresy = []
    for city_path in soup_default.find_all(["a"]):
        if "obec" in str(city_path):
            adresy.append("http://volby.cz/pls/ps2017nss/" + str(city_path["href"]))
        else:
            pass
    adresy = list(dict.fromkeys(adresy))
    return adresy

def vytvor_balik_dat(odkaz_okresu):
    lokalni_soup = get_soup(odkaz_okresu)
    kody_obci = get_kod_obce(lokalni_soup)
    nazvy_obci = get_nazev_obce(lokalni_soup)
    odkazy_obci = get_odkazy_obci(lokalni_soup)

    return list(zip(kody_obci, nazvy_obci, odkazy_obci))

def vytvor_csv_soubor(balik_dat):
    nazev_souboru = "vystup"
    odkaz_pro_zahlavi = balik_dat[0][2]
    soup_zahlavi = get_soup(odkaz_pro_zahlavi)
    zahlavi = vytvor_zahlavi(soup_zahlavi)
    with open('{}.csv'.format(nazev_souboru), 'w', newline='') as soubor:
        writer = csv.writer(soubor)
        writer.writerow(zahlavi)
        for obec in balik_dat:
            print('Zpracovavam obec {}.'.format(obec[1]))
            current_odkaz = obec[2]
            current_soup = get_soup(current_odkaz)
            vysledky = get_vysledky_obce(current_soup)
            writer.writerow([obec[0], obec[1]] + vysledky)
    soubor.close()
    print("Soubor dokoncen.")

def main():
    odkaz_okresu = input(
        "Vlozte odkaz: ").strip()
    balik_dat = vytvor_balik_dat(odkaz_okresu)
    vytvor_csv_soubor(balik_dat)

if __name__ == "__main__":
    main()
