# Onde o log que você acabou de gerar está guardado
caminho_log = r"C:\Users\David\Desktop\access.log"

# Dicionários para guardar as contagens
contagem_status = {}
contagem_ips = {}

print("--- Iniciando Análise de Logs do David ---")

try:
    # Abrimos o arquivo para leitura ('r') e damos o nome de 'arquivo'
    with open(caminho_log, "r") as arquivo:
        for linha in arquivo:
            # O split divide a linha em pedaços baseados nos espaços
            partes = linha.split()
            
            # Se a linha for muito curta (erro de geração), ignoramos
            if len(partes) < 5:
                continue
            
            ip = partes[0]      # O primeiro item é o IP
            status = partes[-1] # O último item é o código (200, 404, etc)
            
            # Contagem dos Status
            contagem_status[status] = contagem_status.get(status, 0) + 1
            
            # Contagem dos IPs
            contagem_ips[ip] = contagem_ips.get(ip, 0) + 1

    # --- EXIBIÇÃO DOS RESULTADOS ---
    print("\n[ RELATÓRIO DE SAÚDE DO SERVIDOR ]")
    for cod, total in contagem_status.items():
        if cod == "200":
            print(f"✅ Sucesso (200): {total} acessos")
        elif cod == "404":
            print(f"❌ Erro Não Encontrado (404): {total} acessos")
        else:
            print(f"⚠️ Outros Status ({cod}): {total} acessos")

    print("\n[ RANKING DE ACESSOS (QUEM MAIS ENTROU) ]")
    # Ordenar do maior para o menor
    for ip, total in sorted(contagem_ips.items(), key=lambda item: item[1], reverse=True):
        print(f"IP: {ip} ----> {total} vezes")

except FileNotFoundError:
    print(f"ERRO: Não encontrei o arquivo em: {caminho_log}")

caminho_log = r"C:\Users\David\Desktop\access.log"

contagem_status = {}
contagem_ips = {}
total_geral = 0  # <--- NOVO: Começamos o contador em zero

print("--- Iniciando Análise de Logs do David ---")

try:
    with open(caminho_log, "r") as arquivo:
        for linha in arquivo:
            partes = linha.split()
            if len(partes) < 5:
                continue
            
            total_geral += 1  # <--- NOVO: Toda linha lida soma 1 aqui
            
            ip = partes[0]
            status = partes[-1]
            
            contagem_status[status] = contagem_status.get(status, 0) + 1
            contagem_ips[ip] = contagem_ips.get(ip, 0) + 1

    # --- EXIBIÇÃO DOS RESULTADOS ---
    print("\n[ RELATÓRIO DE SAÚDE DO SERVIDOR ]")
    # ... (mantenha o código dos status que já funciona) ...
    for cod, total in contagem_status.items():
        if cod == "200":
            print(f"✅ Sucesso (200): {total} acessos")
        elif cod == "404":
            print(f"❌ Erro Não Encontrado (404): {total} acessos")
        else:
            print(f"⚠️ Outros Status ({cod}): {total} acessos")

    # NOVO: Mostra o total acumulado antes do ranking de IPs
    print(f"\n📊 TOTAL DE REQUISIÇÕES PROCESSADAS: {total_geral}") 
    print("-" * 40)

    print("\n[ RANKING DE ACESSOS (QUEM MAIS ENTROU) ]")
    for ip, total in sorted(contagem_ips.items(), key=lambda item: item[1], reverse=True):
        print(f"IP: {ip} ----> {total} vezes")

except FileNotFoundError:
    print(f"ERRO: Não encontrei o arquivo em: {caminho_log}")
