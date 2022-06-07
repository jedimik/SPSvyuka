# Json a load configurace
# Configurace obsahuje staty bojovniku, pro kazdeho bojovnika
# Simulace Fightu
# Turnaj??
from bojovnik import Bojovnik as fighter
import random as rnd


class Fight():
    def __init__(self,boj1:fighter,boj2:fighter):
        self.__boj1:fighter=boj1
        self.__boj2:fighter=boj2
        
    def attack(self,boj_utocici:fighter,boj_branici:fighter):
        atk_power=boj_branici.difference(boj_utocici.attack(),boj_branici.block())
        boj_branici.change_hp(-atk_power)
        print(f"Bojovnik:{boj_branici.get_name()} to schytal od:{boj_utocici.get_name()} za:{atk_power} a zbyva mu:{boj_branici.get_hp()}")
        
    def who_attack(self,val):
        rnd_value = rnd.randint(0,val)
        if rnd_value<=int(val/2): # utoci bojovnik 1
            return self.attack(self.__boj1,self.__boj2)
        else:
            return self.attack(self.__boj2,self.__boj1)
        
    def process(self,val):
        while self.__boj1.get_hp()>0 and self.__boj2.get_hp()>0:
            self.who_attack(val)
        if self.__boj1.get_hp()<0:
            print(f"Vyhral bojovnik:{self.__boj2.get_name()}.")
        else:
            print(f"Vyhral bojovnik:{self.__boj1.get_name()}.")