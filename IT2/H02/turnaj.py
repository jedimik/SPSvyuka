from fight import Fight
class Tournament():
    def __init__(self,list_bojovniku,val):
        if len(list_bojovniku) % 4 !=0:
            raise ValueError("Blabla")
        self.__list=list_bojovniku
        self.__val=val
        self.__list_zapasu=[]
        self.__list_vitezu=[]
        self.__dict_zapasu={}
        self.vytvor_turnaj()
    
    # Metoda pro vytvoreni dvojic
    def vytvor_zapasy(self,list_boj):
        for i in range(0,len(list_boj),2):
            self.__list_zapasu.append(Fight(list_boj[i],list_boj[i+1]))
        
    # Metoda pro turnaj handling
    def vytvor_turnaj(self):
        self.vytvor_zapasy(self.__list)
        index=0
        cislo=0
        while True:
            self.__list_vitezu.append(self.__list_zapasu[index].process(self.__val))
            self.__dict_zapasu[self.__list_zapasu[index].to_string()]=self.__list_vitezu[-1].get_name()
            self.__list_zapasu.pop(index)
            cislo+=1
            if len(self.__list_zapasu)==0 and len(self.__list_vitezu)!=1:
                self.vytvor_zapasy(self.__list_vitezu)
                self.__list_vitezu=[]
            elif len(self.__list_zapasu)==0 and len(self.__list_vitezu)==1:
                for key,value in self.__dict_zapasu.items():
                    print(f"Zapas mezi{key} vyhral:{value}")
                print(f"Celkovym vitezem je: {self.__list_vitezu[-1].get_name()}")
                break
        return
