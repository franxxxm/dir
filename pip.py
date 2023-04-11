import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QComboBox, QLabel, QMessageBox
import os
import io
import subprocess

class Janela1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 500, 150)
        self.setWindowTitle("Encontrar Arquivos")

        self.pesquisa = QLineEdit(self)
        self.pesquisa.setFixedWidth(280)
        fonte = self.pesquisa.font()
        fonte.setPointSize(12)
        self.pesquisa.setFont(fonte)
        self.pesquisa.move(60,50)

        option = ['Imagem', 'Documento', 'Mídia']
        self.select = QComboBox(self)
        self.select.addItems(option)
        self.select.move(350, 50)

        button = QPushButton("Buscar", self)
        button.clicked.connect(self.pesquisar)
        button.setFixedWidth(140)
        button.move(140,85)

        self.config = QPushButton("Config Diretorio", self)
        self.config.clicked.connect(self.abrir_janela2)
        self.config.setFixedWidth(100)
        self.config.move(350,10)

        self.caixa = QLabel(self)
        self.caixa.move(140, 10)

        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("Arquivo não encontrado")
        self.msg.setWindowTitle("Erro")
        self.msg.setStandardButtons(QMessageBox.Ok)

    def abrir_janela2(self):
        self.janela2 = Janela2()
        self.janela2.show()

    def pesquisar(self):
        encontrado = 0
        caminho_bat = os.path.join(os.getcwd(), 'abrir.bat')
        midia = ['mp3', 'mp4']
        imagens = ['png', 'jpg', 'gif','jpeg','jfif']
        doc = ['docx', 'txt', 'pdf', 'pptx', 'xlsx']
        extensao = self.select.currentText()

        with open('config.txt', 'r') as configs:
            diretorio = configs.read()
     
        if os.path.exists("abrir.bat"):
            bat = open("abrir.bat")
            conteudo = '@echo off \n'
        else:
            bat = open('abrir.bat', 'w')
            conteudo = '@echo off \n'
        
        for pasta_raiz, _, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                caminho_completo = os.path.join(pasta_raiz, arquivo)
                if self.pesquisa.text() == arquivo.split(".")[0]:
                    if(extensao == 'Imagem'):
                        final = arquivo.split(".")[1]
                        for tipos in imagens:
                            if tipos == final:
                                encontrado = 1
                                conteudo += 'start '+ caminho_completo + '\n'
                                with open('abrir.bat', 'w', newline='\r\n') as pontoBAT:
                                    pontoBAT.write(conteudo)
                                return subprocess.call([caminho_bat])

                    if(extensao == 'Documento'):
                        final = arquivo.split(".")[1]
                        for tipos in doc:
                            if tipos == final:
                                encontrado = 1
                                conteudo += 'start '+ caminho_completo + '\n'
                                with open('abrir.bat', 'w', newline='\r\n') as pontoBAT:
                                    pontoBAT.write(conteudo)
                                return subprocess.call([caminho_bat])
                                
                    if(extensao == 'Mídia'):
                        final = arquivo.split(".")[1]
                        for tipos in midia:
                            if tipos == final:
                                encontrado = 1
                                conteudo += 'start '+ caminho_completo + '\n'
                                with open('abrir.bat', 'w', newline='\r\n') as pontoBAT:
                                    pontoBAT.write(conteudo)
                                return subprocess.call([caminho_bat])
        if encontrado == 0:
            self.msg.exec_()
        
                       



class Janela2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 500, 150)
        self.setWindowTitle("Configurações")

        with open('config.txt', 'r') as configs:
            diretorio = configs.read()
        
        self.pesquisa = QLineEdit(self)
        self.pesquisa.setFixedWidth(280)
        fonte = self.pesquisa.font()
        fonte.setPointSize(12)
        self.pesquisa.setFont(fonte)
        self.pesquisa.move(100,50)
        self.pesquisa.setText(diretorio)

        self.button = QPushButton("Confirmar", self)
        self.button.clicked.connect(self.mudarDir)
        self.button.setFixedWidth(140)
        self.button.move(140,85)

    def mudarDir(self):
        diretorio = self.pesquisa.text()

        if os.path.exists("config.txt"):
            txt = open("config.txt")
            conteudo =  diretorio 
            with open('config.txt', 'w') as arquivos:
                arquivos.write(conteudo)
        else:
            txt = open('config.txt', 'w')
            conteudo = diretorio + '\n'
            with open('config.txt', 'w') as arquivos:
                arquivos.write(conteudo)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela1 = Janela1()
    janela1.show()
    sys.exit(app.exec_())
