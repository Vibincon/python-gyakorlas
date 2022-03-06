print("Ez még az if előtt van")

if 10 > 20:
    print("Ez az if-ben van")
    print("a 10 nagyobb mint 5")
    print("asd")
    x = 24
    print(x)
else:
    print("Ez akkor fut le, ha az if feltétele hamis")

print("Ez már az if után van")

print()

kor = int(input("Hány éves vagy?: "))

if kor > 100:
    print("anyádal szorakozz")
elif kor > 18:
    print("ihat alkoholt")
elif kor == 18:
    print("éppenhogy")
elif kor < 0:
    print("még nem is élsz")
elif kor == 0:
    print("üdv az életben")
elif kor < 18:
    print("nem ihat alkoholt")

marka = input("milyen autod van (márka)?: ")
szin = input("milyen szinü?: ")

faj = ""

if marka == "suzuki" or szin == "fos":
    print("csoró vagy")
if marka == "ferrari" and szin == "piros":
    print("gazdag vagy")
if marka == "lada" and szin == "fehér":
    print("öreg vagy")
if marka == "audi" and (szin == "fehér" or szin == "fekete"):
    print("kocsis vagy")
if marka == "mercedes" and (szin == "fehér" or szin == "fekete"):
    faj = "cigány"
    print("akkor cigány vagy")
if marka == "subaru" and (szin == "kék" or szin == "piros"):
    print("tatakae")

if faj == "":
    faj = input("add meg a fajod?: ")

if faj == "fehér":
    print("jó ember vagy")
elif faj == "ukrán":
    print("menekülj")
elif faj == "cigány":
    if input("a szüleid rokonok?: ") == "igen":
        print("teljesen cigány vagy")
