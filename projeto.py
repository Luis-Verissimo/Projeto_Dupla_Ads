import tkinter as tk

page= tk.Tk()
page.title("Calculadora")
page.geometry("400x600")
page.resizable(False, False)

display= tk.StringVar()
display_calc= tk.Entry(
    page,
    textvariable=display,
    borderwidth= 10,
    font= ("Arial", 24),
    relief= "sunken",
    justify= "right",
    state= "readonly")
botoes= [
    ["C", "←", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]
for line in botoes:
    line_frame= tk.Frame(page)
    line_frame.pack(expand=True, fill="both")
    for caractere in line:
        if caractere == "":
            tk.Label(line_frame).pack(side= "left",
            expand= True,
            fill= "both")

        tk.Button(
        line_frame,
        text= caractere,
        ).pack(side= "left",
        expand= True,
        fill= "both")

page.mainloop()