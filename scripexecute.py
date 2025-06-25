import subprocess

arquivo = "main.py"
n = 10  # quantas vezes quer executar

for _ in range(n):
    subprocess.run(["python3", arquivo])
