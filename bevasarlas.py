# ezek a termékek árai
kenyer_ar = 400
tej_ar = 210
cukor_ar = 250

# ennyinek kell otthon lennie
kenyer_k = 2
tej_k = 3
cukor_k = 5

kenyer = input("Menyi kenyér van otthon?: ")
tej = input("Menyi tej van otthon?: ")
cukor = input("Menyi cukor van otthon?: ")

x = kenyer.split(" ")
y = tej.split(" ")
z = cukor.split(" ")

kenyer_m = float(x[0])
tej_m = float(y[0])
cukor_m = float(z[0])

print("Bevásárlási lista:")

if kenyer_m < kenyer_k:
    print(str(kenyer_k - kenyer_m) + "kg" + " kenyér")
if tej_m < tej_k:
    print(str(tej_k - tej_m) + "l" + " tej")
if cukor_m < cukor_k:
    print(str(cukor_k - cukor_m) + "kg" + " cukor")

osszeg = 0
osszeg = osszeg + (kenyer_k - kenyer_m) * kenyer_ar
osszeg = osszeg + (tej_k - tej_m) * tej_ar
osszeg = osszeg + (cukor_k - cukor_m) * cukor_ar

print("Összeg: " + str(osszeg) + "Ft")
