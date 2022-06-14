from fight import Fight
from bojovnik import Bojovnik
from turnaj import Tournament
import json

class Game():
    def __init__(self,filepath):
        self.__config=self.load_conf(filepath)
        self.__bojovnici_conf=self.__config['bojovnici']
        self.__fight_rnd_max=self.__config['fight_rnd_max']
        self.__bojovnici=self.create_fighters()
        # self.start_fight()
        self.start_tournament()

    def load_conf(self,filepath):
        with open(filepath,"r") as f:
            return json.load(f)
    
    def create_fighters(self):
        listik=[]
        for i in self.__bojovnici_conf:
            listik.append(Bojovnik(i['name'],
                                   i['attack'],
                                   i['deff'],
                                   i['hp']))
        return listik
        
        
    def start_fight(self):
        souboj=Fight(self.__bojovnici[0],self.__bojovnici[1])
        souboj.process(self.__fight_rnd_max)
    
    def start_tournament(self):
        tournament=Tournament(self.__bojovnici,self.__fight_rnd_max)

    


if __name__=="__main__":
    Game("configs/config.json")
    # boj1=Bojovnik("Richard",20,8,100)
    # print(boj1.to_string())
    # boj2=Bojovnik("Kevin",12,15,80)
    # print(boj2.to_string())
    # souboj=Fight(boj1,boj2)
    # souboj.process(100)
    
    
    
    
        
        