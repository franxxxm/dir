from tkinter import *
import tkinter
import requests
import os
import tkinter as tk




class Tela1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        def pesquisar():
                print(self.opcoes_selecionada.get())

        self.texto = Label(self, text="Buscar arquivos")
        self.texto.grid(column=0, row=0, padx=10, pady=10)

        self.opcoes = ['imagem', 'texto', 'docuemnto']
        self.opcoes_selecionada = tkinter.StringVar(self)
        self.opcoes_selecionada.set(self.opcoes[0]) 

        self.select = OptionMenu(self, self.opcoes_selecionada, *self.opcoes)
        self.select.grid(column=3, row=1, padx=10, pady=10)

        self.pesquisa = Entry(self, text='Pesquisar', font=18, width=50)
        self.pesquisa.grid(column=0, row=1, padx=10, pady=10)

        self.botao = Button(self, text="Buscar", width=30, command=pesquisar)
        self.botao.grid(column=0, row=2, padx=10, pady=10, )

        self.bind('<Return>', lambda event: self.botao.invoke())

        self.btn_mudar_tela = Button(self, text="Mudar para Tela 2", command=self.mudar_tela)
        self.btn_mudar_tela.grid(column=0,row=4, padx=10, pady=10)

    def mudar_tela(self):
        self.master.frame2.lift()


class Tela2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.btn_voltar_tela = Button(self, text="Voltar para Tela 1", command=self.voltar_tela)
        self.btn_voltar_tela.grid(column=0, row=1, padx=10, pady=10)

    def voltar_tela(self):
        self.master.frame1.lift()

root = tk.Tk()
root.geometry("400x300")

frame1 = Tela1(root)
frame2 = Tela2(root)

root.title("Busca de arquivos")
root.frame1 = frame1
root.frame2 = frame2

frame1.lift()

root.mainloop()