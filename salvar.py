from config import *
def salvar(listabarra,qntbolas,tempo):
    print("aa")
    with open ('simulacaos.txt', "a") as f:
        f.write(str(f"\n{tempo};{qntbolas};"))
        for i in listabarra:
            f.write(str(i))
        

            