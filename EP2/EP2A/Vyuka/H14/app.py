class Svicka():
    def __init__(self,barva,vune,cena,doba_horeni):
        self.__barva=barva
        self.__vune=vune
        self.__cena=cena
        self.__doba_horeni=doba_horeni
    def get_barva(self):
        return self.__barva
    def get_vune(self):
        return self.__vune
    def get_cena(self):
        return self.__cena
    def get_doba_horeni(self):
        return self.__doba_horeni
    def zkratHoreni(self,value):
        self.__doba_horeni+=value
    def set_doba_horeni(self,value):
        self.__doba_horeni=value
    def set_cena(self,value):
        self.__cena=value
    def toString(self):
        print(f"Svicka barvy:{self.__barva} ma vuni po:{self.__vune} jeji cena je:{self.__cena} a hori po dobu:{self.__doba_horeni} min")
    
class SpravaSvicek():
    def __init__(self,svicky:list):
        self.__svicky=svicky
        
    def get_mean_cena(self):
        suma=0
        for i in self.__svicky:
            suma+=i.get_cena()
        return suma/len(self.__svicky)
    
    def set_cena_vsem(self,value):
        for i in self.__svicky:
            i.set_cena(value)
    
    
if __name__=="__main__":
    listik=[]
    listik.append(Svicka("modra","fialkach",150,180))
    listik.append(Svicka("cervena","bazalce",180,120))
    listik.append(Svicka("zluta","medu",130,170))
    listik.append(Svicka("bezova","medunce",120,140))
    listik.append(Svicka("fialova","ruzich",190,170))
    
    sprava_svicek=SpravaSvicek(listik)
    print(sprava_svicek.get_mean_cena())
    
    
