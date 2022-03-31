# # Muzeme nacitat vetsinu souboru pomoci importovanych knihoven
# # My budeme pouzivat defaultni pythonacky pro nacitani csv, txt nebo binary souboru
# # Soubor se vzdy pro operaci musi otevrit a zavrit - Python obsahuje featuru, ktera vzdy po dokonceni skriptu soubor zavre.
# # Soubor muzeme otevirat ve ctyrech rezimech - R, W, A, X

def zapis_do_souboru_txt(filename,data):
    with open(filename+".txt",'w') as f:
        f.write(data)
        
def pridani_do_souboru_txt(filename,data):
    with open(filename+".txt",'a') as f:
        f.write(data)
        
def cti_ze_souboru_txt(filename):
    with open(filename+".txt",'r') as f:
        data=f.readlines()
        for i in range(len(data)):
            print(data[i],end="")
        

if __name__=="__main__":
    data="Toto je moje zkusebni."
    cti_ze_souboru_txt("textfile1")
    # zapis_do_souboru_txt("textfile1",data)
    # pridani_do_souboru_txt("textfile1","\n"+data)
    
# # ZAPISOVANI
    #1. zpusob
    # soubor = open("mujnovysoubor.txt",'w')
    # soubor.write("Ahoj svete\n")
    # soubor.close()

#     #2. zpusob
    # with open("mujnovysoubor2.txt",'w') as f:
    #     f.write("Ahoj svete2\n")
    #     #dalsi prikazy jsou odsazene ve with

#  # CTENI
    # soubor = open("mujnovysoubor.txt",'r')
    # print(type(soubor))
    # for line in soubor:
    #     print(line)
    # soubor.close()

#     #2. zpusob
    # with open("mujnovytextsoubor.txt",'r') as f:
    #     print(f.readline())
    #     #nebo
    #     line=f.readline()
    #     print(line)
    #     #co se stane kdyz necham obe moznosti?
# # APPEND
    #1. zpusob
    # soubor = open("mujnovysoubor.txt",'a')
    # soubor.write("Ahoj sveteNew\n")
    # soubor.close()

    #2. zpusob
    # with open("mujnovysoubor2.txt",'a') as f:
    #     f.write("Ahoj sveteNew2\n")
    #     #dalsi prikazy jsou odsazene ve with
# CTENI
    # with open("mujnovysoubor.txt",'r') as f:
    #     # for line in f:
    #     #     print(line,end="")
    #     line=f.readlines()
    #     print(line)

    # soubor = open("mujnovysoubor2.txt",'r')
    # for line in soubor:
    #     print(line,end="")
    # soubor.close()
    
    # Vytvorte funkci, ktera prijima nazev souboru, a data, ktera do souboru zapise
    # soubor otevirejte jako W
    # Data pro zavolani funkce, nactete z inputu
    
    

