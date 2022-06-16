import random as rnd
class Bojovnik():
    def __init__(self,name,atk,deff,hp):
        self.__name=name
        self.__atk=atk
        self.__deff=deff
        self.__hp=hp
    #Gettry
    def get_name(self):
        return self.__name
    def get_atk(self):
        return self.__atk
    def get_deff(self):
        return self.__deff
    def get_hp(self):
        return self.__hp
    #Changer
    def change_hp(self,value):
        self.__hp+=value
    #To string metoda
    def to_string(self):
        return f"Bojovnik {self.__name} ma: {self.__atk} attack, ma: {self.__deff} deffenzivu a ma: {self.__hp} hpcek"
    # Def generate dmg
    def attack(self):
        rnd_val = rnd.randint(1,self.__atk)
        if rnd_val < self.__atk/2:
            rnd_val+=int((self.__atk)/4)
        return rnd_val
    # Generate block
    def block(self):
        rnd_val=rnd.randint(1,self.__deff)
        return rnd_val
    # Je rozdil utoku nepritele a moji deffky
    def difference(self,atk,block):
        if atk<block:
            return 0
        else:
            return atk-block
        
    
    