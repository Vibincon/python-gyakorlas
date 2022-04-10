i = 0

while i < 5:
    print("Amonger")
    print(i)
    i = i + 1
print("Kész")

gyumolcsok = ["alma", "körte", "barack", "szölö", "banán"]
i = 0
while i < len(gyumolcsok):
    print(gyumolcsok[i])
    i = i + 1

baratok = ["Patrik", "Balázs", "Márk", "Lippai", "Keszthelyi", "Réti", "Pista"]
napok = ["hétfö", "kedd", "szerda", "csütörtök",
         "péntek", "szombat", "vasárnap"]
i = 0

while i < len(baratok):
    print(baratok[i])
    i = i + 1

for nap in napok:
    print(nap)

i = 0
j = 0
while i < 5:
    while j < i + 1:
        print("*", end="")
        j = j + 1
    print()
    j = 0
    i = i + 1

while i > 0:
    while j < i-1:
        print("*", end="")
        j = j+1
    print()
    j = 0
    i = i-1


