from fight import Fight
from bojovnik import Bojovnik
import json

class Game():
    def __init__(self,filepath):
        self.__config=self.load_conf(filepath)
        self.__bojovnici_conf=self.__config['bojovnici']
        self.__fight_rnd_max=self.__config['fight_rnd_max']
        self.__bojovnici=self.create_fighters()
        self.start_fight()

    def load_conf(self,filepath):
        with open(filepath,"r") as f:
            return json.load(f)
    
    def create_fighters(self):
        listik=[]
        for i in self.__bojovnici_conf:
            listik.append(Bojovnik(self.__bojovnici_conf['name'],
                                   self.__bojovnici_conf['attack'],
                                   self.__bojovnici_conf['deff'],
                                   self.__bojovnici_conf['hp']))
        return listik
        
        
    def start_fight(self):
        souboj=Fight(self.__bojovnici[0],self.__bojovnici[1])
        souboj.process(self.__fight_rnd_max)

    


if __name__=="__main__":
    Game("configs/config.json")
    # boj1=Bojovnik("Richard",20,8,100)
    # print(boj1.to_string())
    # boj2=Bojovnik("Kevin",12,15,80)
    # print(boj2.to_string())
    # souboj=Fight(boj1,boj2)
    # souboj.process(100)
    
    
    
    
        
        