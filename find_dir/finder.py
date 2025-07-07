#!/usr/bin/python3
import sys
import requests
import os

def mostrar_ajuda():
    print("""
Uso: python3 finder.py <URL> <WORDLIST> [STATUS_CODE]

Descrição:
  Ferramenta de fuzzing de diretórios que testa caminhos de uma wordlist
  e exibe apenas os que retornam o código de status HTTP especificado (ou todos).

Argumentos:
  <URL>          A URL alvo (ex: http://example.com)
  <WORDLIST>     Caminho do arquivo com os diretórios (ex: listy.txt)
  [STATUS_CODE]  (Opcional) Código de status HTTP desejado (ex: 200, 403).
                 Se omitido, exibe todos os status diferentes de 404.

Outros:
  -h, --help     Mostra esta mensagem de ajuda e sai.
""")
    sys.exit(0)

def mostrar_banner():
    banner = r"""
.___.__         .__                  __                
__| _/|__|______  |  |__  __ __  _____/  |_  ___________ 
/__ | |  \_  __ \ |  |  \|  |  \/    \   __\/ __ \_  __ \
/_/ | |  ||  | \/ |   Y  \  |  /   |  \  | \  ___/|  | \/
\____ | |__||__|    |___|  /____/|___|  /__|  \___  >__|   
     \/                  \/           \/          \/
"""
    print(banner)

# ========== INÍCIO ==========
mostrar_banner()

if len(sys.argv) < 3 or sys.argv[1] in ["-h", "--help"]:
    mostrar_ajuda()

# Corrigido: agora os argumentos são lidos corretamente
url_base = sys.argv[1].rstrip("/")
wordlist_path = os.path.expanduser(sys.argv[2])

try:
    status_filtrado = int(sys.argv[3]) if len(sys.argv) > 3 else None
except ValueError:
    print(f"[!] Código de status inválido: {sys.argv[3]}")
    sys.exit(1)

headers = {"User-Agent": "TAMO TESTANDO TEU SISTEMA MANO"}

# Processa a wordlist
try:
    with open(wordlist_path, "r") as arquivo:
        for linha in arquivo:
            caminho = linha.strip()
            url_completa = f"{url_base}/{caminho}"
            try:
                resposta = requests.get(url_completa, headers=headers)
                status = resposta.status_code

                if status_filtrado is not None:
                    if status == status_filtrado:
                        print(f"{url_completa} -> {status}")
                else:
                    if status != 404:
                        print(f"{url_completa} -> {status}")
            except requests.RequestException as erro:
                print(f"[!] Erro ao acessar {url_completa}: {erro}")
except FileNotFoundError:
    print(f"[!] Arquivo de wordlist '{wordlist_path}' não encontrado.")
    sys.exit(1)
