import speedtest

# cria uma instância do objeto speedtest
st = speedtest.Speedtest()

# executa um teste de velocidade de download
download_speed = st.download()

# executa um teste de velocidade de upload
upload_speed = st.upload()

# obtém a melhor latência disponível para jogos online
best_server = st.get_best_server()
latency = best_server['latency']

# imprime os resultados dos testes de velocidade e latência
print(f"Velocidade de download: {download_speed:.2f} Mbps")
print(f"Velocidade de upload: {upload_speed:.2f} Mbps")
print(f"Melhor latência para jogos online: {latency:.2f} ms")
