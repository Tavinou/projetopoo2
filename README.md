# ProjetoPOO2

Projeto de Programação Orientada a Objetos.

**Objetivo:**  
Simular uma descida de bolas com obstáculos (barras) incluídos, determinando qual bola será a vencedora,feito em python.

A geração das barras, das bolas e o sistema de colisão foram implementados com o auxílio do **ChatGPT-4**.

**Link do projeto rodando:**  
[https://youtube.com/shorts/kHNcAH5uwW8?feature=share](https://youtube.com/shorts/kHNcAH5uwW8?feature=share)

---

## Como configurar

Para ajustar o tamanho da simulação:  
Abra o arquivo `config.py` e altere as variáveis `altura` e `largura`.

Para fazer a simulação, deve ser escrito no `barrabola.txt` a quantidade de bolas, barras e **True** ou **False**, para definir se deseja que sejam geradas bolas a cada 15 segundos ou não.

---

## Executar

Basta ter **Python** e **Pygame** instalados.

```bash
python3 scripexecute.py
```

Se o comando acima não funcionar, use:

```bash
python scripexecute.py
```

---

## Caso ocorra erro de execução

Se o script que executa as simulações múltiplas `scripexecute.py` tiver dando erro substitua o "python3" por "python":

```python
subprocess.run(["python3", arquivo, bola_str, barras_str, geradorligado])
```

Troque por:

```python
subprocess.run(["python", arquivo, bola_str, barras_str, geradorligado])
```