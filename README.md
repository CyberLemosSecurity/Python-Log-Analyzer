# 🛡️ Lab: Python Log Analyzer (Infrastructure Monitoring)

## 1. Project Objective
The goal of this lab is to develop an automated Python tool for processing web server log files. The focus is on extracting critical availability and security metrics, enabling the identification of access patterns and systemic failures without relying on heavy external monitoring tools.

---

## 2. Methodology & Development
The environment was structured into two layers to simulate a real-world data lifecycle:

### A. Data Generation (`gerador.py`)
I developed a script to create a synthetic database in the standard Apache/Nginx server format.
* **Generated Data:** IP addresses, Timestamps, HTTP Methods, URL paths, and Status Codes (200, 404, 500).

### B. Analysis Engine (`analisador.py`)
The analysis script was built using pure Python (no external libraries) to ensure maximum portability between Windows and Linux environments.

**Key Logic Implemented:**
* **Parsing Logic:** String slicing and index mapping.
* **Counting Structure:** Utilization of Dictionaries (Hash Maps) to ensure $O(n)$ performance when processing large volumes.
* **Exception Handling:** Implementation of `try-except` blocks to handle missing files or system permission issues.

```python
# Analysis Logic Example
caminho_log = r"C:\Users\David\Desktop\access.log"
contagem_status = {}
contagem_ips = {}
total_geral = 0 

print("--- Iniciando Análise de Logs do David ---")

try:
    with open(caminho_log, "r") as arquivo:
        for linha in arquivo:
            partes = linha.split()
            if len(partes) < 5:
                continue
            
            total_geral += 1  # Global counter for metrics
            
            ip = partes[0]
            status = partes[-1]
            
            # Counting Status and IPs using Hash Maps
            contagem_status[status] = contagem_status.get(status, 0) + 1
            contagem_ips[ip] = contagem_ips.get(ip, 0) + 1

    # Output Results
    print("\n[ RELATÓRIO DE SAÚDE DO SERVIDOR ]")
    for cod, total in contagem_status.items():
        if cod == "200":
            print(f"✅ Sucesso (200): {total} acessos")
        elif cod == "404":
            print(f"❌ Erro Não Encontrado (404): {total} acessos")
        else:
            print(f"⚠️ Outros Status ({cod}): {total} acessos")

    print(f"\n📊 TOTAL DE REQUISIÇÕES PROCESSADAS: {total_geral}") 
    print("-" * 40)

    print("\n[ RANKING DE ACESSOS (TOP IPs) ]")
    for ip, total in sorted(contagem_ips.items(), key=lambda item: item[1], reverse=True):
        print(f"IP: {ip} ----> {total} vezes")

except FileNotFoundError:
    print(f"ERRO: Arquivo não encontrado em: {caminho_log}")
```

3. Analysis & Results
By running the analyzer over the generated traffic, the following technical insights were obtained:

Server Health: Immediate identification of the ratio between 5xx (Server Error) and 4xx (Client Error) versus successful requests (200).

Network Vigilance: The IP ranking allows for the detection of brute-force attempts or automated scans on sensitive pages like /admin.

Volumetrics: Monitoring the total number of processed requests to calculate error rate percentages accurately.

4. Conclusion
The project proved to be a lightweight and efficient alternative for basic log monitoring. The primary advantage observed was the vertical scalability of the line-by-line reading logic, which prevents excessive RAM consumption in resource-constrained production environments.

Roadmap for Future Improvements:
Implementation of Regular Expressions (Regex) for higher parsing precision.

Creation of Automated Alerts (via Email or Telegram) when 500 error rates exceed a defined threshold.

👨‍💻 Developed by David Environment: Windows 11 | Python 3.14
