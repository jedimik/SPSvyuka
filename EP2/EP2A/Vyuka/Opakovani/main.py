from matplotlib.cbook import delete_masked_points


def vypis_pole(pole):
    for i in range(0,len(pole),1):
        for j in range(0,len(pole[i]),1):
            print(" {} ".format(pole[i][j]),end="")
        print()

def vytvor_2dlist(a,str1):
    list2d=[]
    for i in range(0,a,1):
        radek=[]
        for j in range(0,a,1):
            radek.append(str1)
        list2d.append(radek)
    return list2d

def vytiskni_ahoj():
    print("ahoj")

def vytiskni_co_ti_reknu(slovo):
    print("Chces po mne napsat: "+slovo)
    
def vrat_mi_dvojku():
    return 2
   
#Vytvorte fci pro soucet 2 cisel
def soucet(a,b):
    value=a+b
    return value # return a+b

def odecet(a,b):
    return a-b 

def nasobit(a,b):
    return a*b

def delit(a,b):
    return a/b

if __name__=="__main__":
    # (5+3)-9
    vysledek=odecet(soucet(5,3),9)
    print(vysledek)
    # (5+3)-(9-12)
    vysledek=odecet(soucet(5,3),odecet(9,12))
    print(vysledek)
    # ((5+3)-(9-12))/2
    vysledek=delit(odecet(soucet(5,3),odecet(9,12)),2)
    print(vysledek)
    # ( (5 + 3) - (9 - 12) ) / (4 * 2) + 5
    vysledek=delit(odecet(soucet(5,3),odecet(9,12)),soucet(nasobit(4,2),5))
    print(vysledek)
    # vytiskni_ahoj()
    # vytiskni_co_ti_reknu("Ahoj svete")
    # print(vrat_mi_dvojku())
    # print(vrat_mi_dvojku()+5)
    # mojepromenna=vrat_mi_dvojku()
    # print(mojepromenna)
    
    # print("Ahoj")
    # a=int(input("Zadej mi integer"))
    # str1=input("Zadej mi string")
    # print("V promenne A mam :{} a je typu:{}".format(a,type(a)))
    # print("V promenne str1 mam :{} a je typu:{}".format(str1,type(str1)))
    
    # list2d=vytvor_2dlist(a,str1)
    # list2d1=vytvor_2dlist(4,"*")
    # list2d2=vytvor_2dlist(6,"ahoj")
    # vypis_pole(list2d)
    # vypis_pole(list2d1)
    # vypis_pole(list2d2)
    # Inicializace
    # for i in range(0,a,1):
    #     radek=[]
    #     for j in range(0,a,1):
    #         radek.append(str1)
    #     list2d.append(radek)
    # Vypsani
    # for i in range(0,len(list2d),1):
    #     for j in range(0,len(list2d[i]),1):
    #         print(" {} ".format(list2d[i][j]),end="")
    #     print()
    # vypis_pole(list2d)
    # vypis_pole(list2d)
    # vypis_pole(list2d)