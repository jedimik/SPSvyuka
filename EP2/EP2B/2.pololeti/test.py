def soucet(a,b):
    return a+b
def rozdil(a,b):
    return a-b
def nasobit(a,b):
    return a*b
def deleni(a,b):
    return a/b
a=4
b=3
c=2

vysledek=deleni(soucet(nasobit(b,a),deleni(rozdil(a,c),5)),rozdil(nasobit(b,4),nasobit(soucet(b,c),6)))
vysledek2=deleni(rozdil(deleni(b,a),nasobit(soucet(4,c),soucet(b,5))),soucet(nasobit(b,a),deleni(b,c)))
print(vysledek)
print(vysledek2)