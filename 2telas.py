import tkinter as tk

root = tk.Tk()

def mudar_tela():
    tela1.grid_forget()
    tela2.grid(row=0, column=0, padx=50, pady=50)

tela1 = tk.Frame(root)
tela1.grid(row=0, column=0, padx=50, pady=50)

botao = tk.Button(tela1, text="Mudar de tela", command=mudar_tela)
botao.grid(row=0, column=0)

tela2 = tk.Frame(root)
label = tk.Label(tela2, text="Esta é a tela 2")
label.grid(row=0, column=0)

root.mainloop()
