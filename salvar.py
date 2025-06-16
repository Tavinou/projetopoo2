def salvar(barras,qntbolas,tempo):
    with open ('simulacaos.txt', "a") as f:
        f.write('execucao')
        for i in barras:
            f.write(str(i) + " | ")
        f.write(str(f"\nquantidade de bolas:{qntbolas}\n"))
        f.write(str(f"tempo de execucao:{tempo}\n"))

            