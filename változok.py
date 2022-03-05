nev = "Kruppa Bence"
kedvenc = "Csák Patrik lába"
print("sziasztok " + nev + " vagyok!")
print("a kedvencem a " + kedvenc + "!")
kedvenc = "Gragas segge"
print("megodnoltam magam inkább a " + kedvenc + "-t szeretem jobban")

# kiszámolom a téglalap területétt
print("téglalap területe")
a = 5
b = 10
print("a = ", end="")
print(a)
print("b = ", end="")
print(b)
print("terület:", end="")
print(a * b, end="")
print("cm^2")

# kiszámolom a kör kerületétt
print("Kör területe")
pi = 3.14
r = 16
print("pi = ", end="")
print(pi)
print("r = ", end="")
print(r)
print("terület:", end="")
print(pi * r, end="")
print("cm^2")

# egy pizára átvátottuk és kiszámoltuk a szélét

print("pizza szélének a területe:")
pizzat = pi*r
kpizzat = pi*(r-2)
print("kissebb pizza terülüte:", end="")
print(pizzat - kpizzat, end="")
print("cm^2")

print((pi*r) - (pi*(r-2)))  # változok nélkül számitottam ugyan azt ki

print("patrik kedvenc pizzájának levágja a szélét majd megfelezi mekkora igy a pizza?")
kispizza = pizzat-kpizzat
print(kispizza/2, end="")
print("cm^2")

print("balázs vesz két pizzát mekkora igy 2 pizza területe")
print(pizzat*2, end="")
print("cm^2")

print()  # sorkihagyás

x = 100
y = 7
print(x, end=" / ")
print(y, end=" = ")
print(round(x/y))  # patrik fekete mágijája a round fügvény () plus belekerül a printbe
print("maradék: ", end="")
print(x % y)
