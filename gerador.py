import random
import time

# Onde o log será criado
caminho_final = r"C:\Users\David\Desktop\access.log"

ips = ["192.168.1.1", "10.0.0.5", "172.16.0.10", "200.150.10.1"]
paginas = ["/home", "/login", "/admin", "/api/data"]
status_codes = ["200", "404", "500"]

print(f"Criando log em: {caminho_final}")

# Aqui é onde o nome 'f' ou 'arquivo' é definido
with open(caminho_final, "w") as arquivo:
    for _ in range(100):
        ip = random.choice(ips)
        pag = random.choice(paginas)
        st = random.choice(status_codes)
        data = time.strftime("%d/%b/%Y:%H:%M:%S")
        linha = f'{ip} - - [{data}] "GET {pag} HTTP/1.1" {st}\n'
        arquivo.write(linha)

print("Sucesso! O arquivo 'access.log' apareceu no seu Desktop.")
