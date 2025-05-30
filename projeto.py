import tkinter as tk

page= tk.Tk()
page.title("Calculadora")
page.geometry("400x600")
page.resizable(False, False)

botoes= [
    ["Calculadora"]    
]
for line in botoes:
    lineframe=tk.Frame(page)
    lineframe.pack(expand=True, fill="x")
    for botao in line:
        botao=tk.Button(
            lineframe, text=botao, font=("arial", 12)
        )
    botao.pack(expand=True, fill="both")
page.mainloop()