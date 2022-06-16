from bojovnik import Bojovnik as fighter
import random as rnd


class Fight():
    def __init__(self,boj1:fighter,boj2:fighter):
        self.__boj1:fighter=boj1
        self.__boj2:fighter=boj2
        
    # Samotny vypocet attacku
    def attack(self,boj_utocici:fighter,boj_branici:fighter):
        atk_power=boj_branici.difference(boj_utocici.attack(),boj_branici.block())
        boj_branici.change_hp(-atk_power)
        print(f"Bojovnik:{boj_branici.get_name()} to schytal od:{boj_utocici.get_name()} za:{atk_power} a zbyva mu:{boj_branici.get_hp()}")
        
    # Metoda pro generování, který bojovník bude bojovat. Aktuálně je to random z val.
    def who_attack(self,val):
        rnd_value = rnd.randint(0,val)
        if rnd_value<=int(val/2): # utoci bojovnik 1
            return self.attack(self.__boj1,self.__boj2)
        else:
            return self.attack(self.__boj2,self.__boj1)
    # metoda pro simulaci celeho zapasu a vyhodnoceni. vraci vitezneho bojovnika
    def process(self,val):
        while self.__boj1.get_hp()>0 and self.__boj2.get_hp()>0:
            self.who_attack(val)
        if self.__boj1.get_hp()<0:
            print(f"Vyhral bojovnik:{self.__boj2.get_name()}.")
            return self.__boj2
        else:
            print(f"Vyhral bojovnik:{self.__boj1.get_name()}.")
            return self.__boj1

    def to_string(self):
        return f"Bojovnik:{self.__boj1.get_name()}_vs_Bojovnik:{self.__boj2.get_name()}"
