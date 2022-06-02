class Sklenice():
    def __init__(self,material,vyska,objem,teplo_bool):
        self.__material=material
        self.__vyska=vyska
        self.__objem=objem
        self.__teplo_bool=teplo_bool
    
    def get_material(self):
        return self.__material
    def get_vyska(self):
        return self.__vyska
    def get_objem(self):
        return self.__objem
    def get_teplo(self):
        return self.__teplo_bool
    
    def vypis(self): # budu volat do printu 
        if self.__teplo_bool:
            vhodnost="je vhodna pro teple napoje"
        else:
            vhodnost="neni vhodna pro teple napoje"
        return f'Sklenice z {self.__material} je vysoka: {self.__vyska} mm a jeji objem je: {self.__objem} a {vhodnost}'
    
    def vypis2(self): # toto budu volat jako metodu na instanci tridy
        if self.__teplo_bool:
            vhodnost="je vhodna pro teple napoje"
        else:
            vhodnost="neni vhodna pro teple napoje"
        print(f'Sklenice z {self.__material} je vysoka: {self.__vyska} mm a jeji objem je: {self.__objem} a {vhodnost}')
    
    def change_objem(self,value):
        self.__objem+=value
        
    def change_teplo(self):
        if self.__teplo_bool:
            self.__teplo_bool=False
        else:
            self.__teplo_bool=True

class Spravce_sklenic():
    def __init__(self,listik):
        self.__listik=listik
        
    def vypis_list(self):
        for i in self.__listik:
            i.vypis2()
    
    def pridej_do_listu(self,sklenice):
        self.__listik.append(sklenice)
            
if __name__=="__main__":
    listik=[Sklenice("Plech",150,350,True),
            Sklenice("Dreva",140,330,True),
            Sklenice("Skla",145,335,True),
            Sklenice("Nerez",155,500,True),
            Sklenice("Plast",125,350,True)]
    
    bla=Spravce_sklenic(listik=listik)
    bla.vypis_list()
    # Vytvorit instanci spravce, dat do nej list, vypsat ho, vytvorit novou sklenici
    # a tuto sklenici pridat do instance spravce a opet vypsat cely list
    
    
    
    # for i in listik:
    #     print(i.vypis())
    
    # for i in listik[-2:]:
    #     i.change_teplo()
    #     i.change_objem(-100)
    # print()  
    # for i in listik:
    #     i.vypis2()
        