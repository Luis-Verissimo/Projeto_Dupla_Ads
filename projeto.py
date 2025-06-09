import tkinter as tk

def clique_botao(valor):
    atual = display.get()
    display.set(atual + valor)

def limpar():
    display.set("")

def apagar():
    atual = display.get()
    display.set(atual[:-1])

def calcular():
    try:
        resultado = str(eval(display.get().replace("×", "*").replace("÷", "/")))
        display.set(resultado)
    except:
        display.set("Erro")

# interface
page = tk.Tk()
page.title("Calculadora")
page.geometry("400x600")
page.resizable(False, False)
page.configure(bg="#1e1e1e")

display = tk.StringVar()
display_calc = tk.Entry(
    page,
    textvariable=display,
    font=("Segoe UI", 28),
    borderwidth=0,
    bg="#1e1e1e",
    fg="#ffffff",
    justify="right",
    state="readonly",
    readonlybackground="#1e1e1e"
)
display_calc.pack(fill="both", ipadx=8, ipady=30, padx=10, pady=20)

# grade de botões
botoes = [
    ["C", "←", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

cores_botoes = {
    "C": "#d64d4d",
    "←": "#f29c2b",
    "=": "#4caf50",
    "+": "#555",
    "-": "#555",
    "×": "#555",
    "÷": "#555",
    "%": "#555"
}

# frame geral da grade
botoes_frame = tk.Frame(page, bg="#1e1e1e")
botoes_frame.pack(expand=True, fill="both", padx=10, pady=10)

for i, linha in enumerate(botoes):
    for j, caractere in enumerate(linha):
        if caractere == "":
            continue

        if caractere == "C":
            comando = limpar
        elif caractere == "←":
            comando = apagar
        elif caractere == "=":
            comando = calcular
        else:
            comando = lambda valor=caractere: clique_botao(valor)

        cor_fundo = cores_botoes.get(caractere, "#333")
        cor_ativa = "#777" if caractere not in cores_botoes else "#666"

        botao = tk.Button(
            botoes_frame,
            text=caractere,
            command=comando,
            font=("Segoe UI", 20),
            fg="white",
            bg=cor_fundo,
            activebackground=cor_ativa,
            bd=0,
            relief="flat"
        )
        botao.grid(row=i, column=j, sticky="nsew", padx=4, pady=4)


total_linhas = len(botoes)
total_colunas = 4  

for i in range(total_linhas):
    botoes_frame.rowconfigure(i, weight=1)

for j in range(total_colunas):
    botoes_frame.columnconfigure(j, weight=1)

page.mainloop()
