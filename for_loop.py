gyumolcsok = ["alma", "banán", "szőlő", "kivi"]


for x in gyumolcsok:
    print(x)

for i in range(0, len(gyumolcsok)):
    print(str(i + 1) + ": " + gyumolcsok[i])

szamok = []
for i in range(1, 23+1):
    szamok.append(i)
print(szamok)


negyzetek = []
for i in range(1, 10+1):
    negyzetek.append(i*i)
print(negyzetek)

print("amongus"[3])

print()

for c in "sus":
    print(c)

print()

for x in gyumolcsok:
    for c in x:
        if c != "a":
            print(c, end="")
    print()
