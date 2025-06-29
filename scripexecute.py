import subprocess
arquivo = "main.py"
with open("barrabola.txt", "r") as f:
    linhas = f.readlines()
for i, linha in enumerate(linhas):
    bola_str, barras_str, geradorligado = linha.strip().split()
    subprocess.run(["python3", arquivo, bola_str, barras_str, geradorligado]) #se nao achar o python troce o "python3" por python
