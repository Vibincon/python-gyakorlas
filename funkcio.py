from ctypes.wintypes import PINT
import math
from tkinter import Y


def cigany_vagy(tipus, hanyszor):
    for i in range(0, hanyszor):
        print(tipus + " CIGÁNY VAGY!")


cigany_vagy("BUTA RETKES KOSZOS OSTOBA GECI ROHADÉK", 3)


def szam(x, y):
    for i in range(x, y):
        print(i, end=", ")
    print(y)


print(math.sqrt(4))

szam(1, 30+1)

# téglalap kerülete, területe
# formátum:
# teglalap(10, 10)
# x = 10cm y = 10cm
# K = 40cm
# T = 100cm
# kör területe, kerülete
# pitagorasz tétel
# két pont közötti távolság


def teglalap(x, y):
    print("x " + "= " + str(x) + "cm", end=" ")
    print("y " + "= " + str(y) + "cm")
    print("K " + "= " + str(y*4) + "cm^2")
    print("T " + "= " + str(x*y) + "cm^2")

def teglalap_f(x,y):
    print(f"x = {x}cm y = {y}cm")
    print(f"K = {x*4}cm^2")
    print(f"T = {x*y}cm^2")
    


def kor(r):
    print(f"r = {r}cm")
    print(f"K = {3.14*(r*r)}cm^2")
    print(f"T = {2*(3.14*r)}cm^2")

def pitagorasz(x,y):
    print(f"a^2 + b^2 = c^2")
    print(f"a = {x}")
    print(f"b = {y}")
    print(f"c = {math.sqrt((x*x) + (y*y)) }")

def ketponttavolsaga(x,y,v,u):
    print(f"elsö pont elsö kordinátája = {x}")
    print(f"elsö pont második kordinátája = {y}")
    print(f"második pont elsö kordinátája = {v}")
    print(f"második pont második kordinátája = {u}")
    xv = {x-v}
    print(f"ezek távolsága(d) = {math.sqrt((x-v)*(x-v))+math.sqrt((y-u)*(y-u))}")


teglalap(10, 10)
teglalap_f(10, 11)
print("EZ MÁR A KÖRE VONATKOZIK")
kor(5)
print("EZ MÁR A PITAGORASTÉTELRE VONATKOZIK")
pitagorasz(3,4)
print("EZ MÁR A KÉT PONT TÁVOLSÁGÁRA VONATKOZIK")
ketponttavolsaga(1,1,3,4)
