from config import *
def salvar(listabarra,qntbolas,tempo,con):
    print("simulacao salva")
    with open ('simulacaos.txt', "a") as f:
        f.write(str(f"{con};{tempo};{qntbolas};"))
        for i in listabarra:
            f.write(str(i))
        f.write("\n")

            