def napis_ahoj():
    print("Ahoj")

def napis_co_ti_poslu(veta):
    print(veta)
    
# Funkci pro vypsani NxN hvezdicek.
def vypis_hvezdicky(pocet_radku,pocet_sloupecku):
    for i in range(0,pocet_radku,1):
        for j in range(0,pocet_sloupecku,1):
            print("*",end="")
        print()
        
def vrat_mi_dvojku():
    return 2

def soucet(a,b):
    return a+b

def deleni(a,b):
    return a/b

def odecet(a,b):
    return a-b

def nasobit(a,b):
    return a*b

if __name__=="__main__":
    a=5
    napis_ahoj()
    slovo="Ahoj svete ted pisu neco noveho"
    napis_co_ti_poslu(slovo)
    napis_co_ti_poslu("Ahoj tohle pisu ted jinym zpusobem")
    napis_co_ti_poslu(veta="Ahoj toto je dalsi zpusob")
    vypis_hvezdicky(5,5)
    vypis_hvezdicky(2,6)   
    b=vrat_mi_dvojku()
    print(b)
    print(vrat_mi_dvojku())
    vypis_hvezdicky(vrat_mi_dvojku(),vrat_mi_dvojku())
    print(soucet(5,10))
    b=soucet(10,4)
    b=soucet(b,6)
    print(b)
    vysledek=deleni(nasobit(soucet(6,5),3),2)
    print(vysledek)