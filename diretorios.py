import os
import asyncio
import requests

arquivos = []
pastas = []
subPastas = []



async def main():
    w = "C:/Users/Administrador/Downloads" 
    diretorio = os.listdir(w)
    for d in diretorio:
        if os.path.isdir(w + "/" + d):
            pastas.append(d) 
        else:
            arquivos.append(d)
    for p in pastas:
        subPastas.append(os.listdir(w + "/" + p))
        await asyncio.sleep(1)
        for s in subPastas:
            for k in s:
                if os.path.isdir(w + "/" + p + "/" + k):
                    pastas.append(p + "/" +k)
                else:
                    arquivos.append(k)            
asyncio.run(main())

print(arquivos)

