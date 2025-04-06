import tkinter as tk
import random
import string

def gerar_senha():
    tamanho = int(entry_tamanho.get())
    nivel = var_nivel.get()

    if nivel == 'fraca':
        caracteres = string.ascii_lowercase
    elif nivel == 'media':
        caracteres = string.ascii_letters + string.digits
    else:
        caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    resultado.config(text=senha)

    with open('senhas_salvas.txt', 'a') as arquivo:
        arquivo.write(senha + '\n')

# Interface gráfica
janela = tk.Tk()
janela.title("Gerador de Senhas")

tk.Label(janela, text="Tamanho da senha:").pack()
entry_tamanho = tk.Entry(janela)
entry_tamanho.insert(0, "12")
entry_tamanho.pack()

tk.Label(janela, text="Nível de segurança:").pack()
var_nivel = tk.StringVar(value="forte")
tk.Radiobutton(janela, text="Fraca", variable=var_nivel, value="fraca").pack()
tk.Radiobutton(janela, text="Média", variable=var_nivel, value="media").pack()
tk.Radiobutton(janela, text="Forte", variable=var_nivel, value="forte").pack()

tk.Button(janela, text="Gerar Senha", command=gerar_senha).pack(pady=10)
resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()
