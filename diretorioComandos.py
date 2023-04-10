import os
import requests


ar = []

def listar_arquivos(diretorio):
    for pasta_raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho_completo = os.path.join(pasta_raiz, arquivo)
            ar.append(arquivo)
            print(len(ar))


listar_arquivos("Y:/")


