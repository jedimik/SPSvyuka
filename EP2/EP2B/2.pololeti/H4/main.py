import random as rnd
import time 
def generuj_1dpole(a,b,n):
    policko=[]
    for i in range(0,n,1):
        policko.append(rnd.randint(a,b))
    return policko

def min_max_mean(pole):
    return min(pole),max(pole),sum(pole)/len(pole)

def lin_prohled(pole,prvek):
    for i in range(len(pole)):
        if pole[i]==prvek:
            print("prvek: {} se nachazi v poli na pozici: {}".format(prvek,i))
            return i
    print("Prvek: {} se v poli nenachazi".format(prvek))
    
def generuj_pin():
    return rnd.randint(0,9),rnd.randint(0,9),rnd.randint(0,9),rnd.randint(0,9)

def zjisti_pin(a,b,c,d):
    for i in range(0,9):
        if a==i:
            for j in range(0,9):
                if b==j:
                    for k in range(0,9):
                        if c==k:
                            for l in range(0,9):
                                if d==l:
                                    print("Pin byl:{}".format(str(i)+str(j)+str(k)+str(l)))
                                    return i,j,k,l
                                else:
                                    continue
                        else:
                            continue
                else:
                    continue   
        else:
            continue
    
if __name__=="__main__":
    # policko=generuj_1dpole(-50,100,15)
    # print(policko)
    # min,max,mean=min_max_mean(policko)
    # print("Min:{} Max:{} Prumer:{}".format(min,max,round(mean,3)))
    # x=lin_prohled(policko,89)
    # print(x)
    a,b,c,d=generuj_pin()
    t = time.time()
    zjisti_pin(a,b,c,d)
    elapsed = time.time() - t
    print("puvodni pin vygenerovany byl:{} a muj vypocet trval:{}".format(str(a)+str(b)+str(c)+str(d),elapsed))