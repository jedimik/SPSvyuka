import json

def load_conf(filepath):
    with open(filepath,"r") as f:
        return json.load(f)

if __name__=="__main__":
    
    cnf=load_conf("configs/config.json")
    print()