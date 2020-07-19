# Texty pro analyzu
text1 = ("Situated about 10 miles west of Kemmerer, "
         "Fossil Butte is a ruggedly impressive "
         "topographic feature that rises sharply "
         "some 1000 feet above Twin Creek Valley "
         "to an elevation of more than 7500 feet "
         "above sea level. The butte is located just "
         "north of US 30N and the Union Pacific Railroad, "
         "which traverse the valley.")
text2 = ("At the base of Fossil Butte are the bright "
         "red, purple, yellow and gray beds of the Wasatch "
         "Formation. Eroded portions of these horizontal "
         "beds slope gradually upward from the valley floor "
         "and steepen abruptly. Overlying them and extending "
         "to the top of the butte are the much steeper "
         "buff-to-white beds of the Green River Formation, "
         "which are about 300 feet thick.")
text3 = ("The monument contains 8198 acres and protects "
         "a portion of the largest deposit of freshwater fish "
         "fossils in the world. The richest fossil fish deposits "
         "are found in multiple limestone layers, which lie some "
         "100 feet below the top of the butte. The fossils "
         "represent several varieties of perch, as well as "
         "other freshwater genera and herring similar to those "
         "in modern oceans. Other fish such as paddlefish, "
         "garpike and stingray are also present.")

# Jména a hesla
login = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

# Uvítání a zadani loginu
pomlka = ("-" * 40)
print(pomlka)
print("Welcome to the app. Please log in:")
jmeno = str(input("USERNAME: "))
heslo = str(input("PASSWORD: "))

# Overeni loginu
if login.get(jmeno) == heslo:
    print("Login successful")
else:
    print("Login unsuccessful")
    exit()
print(pomlka)

# Výběr textu
print("We have 3 texts to be analyzed.")
vyber = int(input("Enter a number btw. 1 and 3 to select: "))
print(pomlka)

# Prirazeni textu k vyberu
if vyber == 1:
    rozsekana_veta = text1.split()
elif vyber == 2:
    rozsekana_veta = text2.split()
elif vyber == 3:
    rozsekana_veta = text3.split()
else:
    print("Wrong text selected")

# Počítání jednotlivých případů
count1 = 0
count2 = 0
count3 = 0
count4 = 0

pocet_slov = len(rozsekana_veta)

for a in rozsekana_veta:
    if (a.istitle()) == True:
        count1 += 1
    elif (a.isupper()) == True:
        count2 += 1
    elif (a.islower()) == True:
        count3 += 1
    elif (a.isnumeric()) == True:
        count4 += 1

print("There are {} words in the selected text.".format(pocet_slov))
print("There are {} titlecase words".format(count1))
print("There are {} uppercase words".format(count2))
print("There are {} lowercase words".format(count3))
print("There are {} numeric strings".format(count4))
print(pomlka)

# Délky slov
delky = {}
for word in rozsekana_veta:
    delka = len(word)
    if delka not in delky:
        delky[delka] = 0
    delky[delka] += 1
sorted_dict = dict(sorted(delky.items()))
for delka, counter in sorted_dict.items():
    print(delka, ("*" * counter), counter)
print(pomlka)

# Suma cisel v textu
suma = 0
for a in rozsekana_veta:
    if (a.isnumeric()) == True:
        suma += int(a)
print("If we summed all the numbers in this text we would get: {}".format(suma))
print(pomlka)