# def soucet(prom):
#     return prom+8

#Fce pro odecet
def odecet(a,b):
    return a-b
#fce pro soucet
def soucet(a,b):
    return a+b
#fce pro deleni
def deleni(a,b):
    return a/b
#fce pro nasobeni
def nasobeni(a,b):
    return a*b

def fce1(a):
    for i in range(0,a,1):
        for j in range(0,a,1):
            if i%2==0:
                print(" / ",end="")
            else:
                print(" * ",end="")
        print()

def fce2(a):
    for i in range(0,a,1):
        for j in range(0,a,1):
            if i%2==0:
                print(j+1,end="")
            else:
                print(a-j,end="")
        print()

if __name__=="__main__":
    res=deleni(nasobeni(soucet(6,5),4),odecet(1,nasobeni(3,5)))
    print(res)
    res2=deleni(nasobeni(odecet(4,2),nasobeni(5,2)),odecet(odecet(1,3),nasobeni(-5,2)))
    print(res2)
    fce1(5)
    fce2(5)