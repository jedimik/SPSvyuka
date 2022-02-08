a=int(input("Zadej hodnotu A: "))
b=int(input("Zadej hodnotu B: "))

list2D=[]
for i in range(0,a,1):
    radek=[]
    for j in range(0,b,1):
        radek.append(1)
    list2D.append(radek)
    
for i in range(0,len(list2D),1):
    for j in range(0,b,1):
        print(" {} ".format(list2D[i][j]),end="")
    print()
print("--------------")    
for i in range(0,len(list2D),1):
    for j in range(0,len(list2D[i]),1):
        if i%2==0 and j%2==0:
            list2D[i][j]*=3
        elif i%2==1:
            list2D[i][j]+=5
        else:
            list2D[i][j]*=2
            
for i in range(0,len(list2D),1):
    for j in range(0,b,1):
        print(" {} ".format(list2D[i][j]),end="")
    print()       
    
list1D=[]

for i in range(0,len(list2D),1):
    soucet=0
    for j in range(0,len(list2D[i]),1):
        soucet+=list2D[i][j]
    list1D.append(soucet)

for i in range(0,len(list1D),1):
    print("Soucet:{} radku je roven={} .".format(i,list1D[i]))