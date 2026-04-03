#  Python Log Analyzer Lab

Este é um laboratório prático desenvolvido em Python para simular e analisar logs de um servidor web. O projeto demonstra como processar dados brutos e transformá-los em informações úteis.

##  Objetivo do Projeto
Demonstrar habilidades em Python, como:
* Manipulação de arquivos (`open`, `read`, `write`).
* Estruturas de dados (Dicionários para contagem).
* Lógica de programação (Loops e condicionais).
* Tratamento de erros (`try/except`).

---

##  Como Funciona o Laboratório

O laboratório é dividido em duas etapas:

### 1. Geração de Dados (`gerador.py`)
Um script que cria um arquivo chamado `access.log` simulando acessos ao servidor, contendo IPs, caminhos de páginas e status HTTP (200, 404, 500).

### 2. Análise de Dados (`analisador.py`)
O motor principal que lê o arquivo gerado e extrai:
* **Total de Requisições:** Soma geral de acessos processados.
* **Relatório de Saúde:** Contagem detalhada de códigos de sucesso e erro.
* **Ranking de IPs:** Identificação dos endereços que mais acessaram o servidor.

---

##  Como Executar

### Passo a Passo
1. Execute o gerador para criar a base de dados:
   ```bash
   python gerador.py
