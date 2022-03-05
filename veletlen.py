import random

print(random.randrange(1, 22))

penz = random.randrange(1, 1000000+1)
print(str(penz) + "Ft" + " enyi pénze van patriknak" )
if penz > 800000:
    print("zsiros zsebbélelö zseton")
elif penz > 600000:
    print("van della")
elif penz > 400000:
    print("megélhetös lesz a honap")
elif penz > 200000:
    print("necces lesz a honap")
elif penz > 100000:
    print("ebböl nem lesz vacsora")
elif penz == 35000:
    print("fater utalt")
elif penz < 100000:
    print("csoro")