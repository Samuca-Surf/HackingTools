import requests
import sys

def mostrar_ajuda():
    print("""
Uso: python3 finder.py <URL> [STATUS_CODE]

Descrição:
  Ferramenta de fuzzing de diretórios que testa caminhos de um arquivo de wordlist
  e exibe apenas os que retornam o código de status HTTP especificado.

Argumentos:
  <URL>          A URL alvo (ex: http://example.com)
  [STATUS_CODE]  (Opcional) O código de status HTTP desejado (ex: 200, 403, 404).
                 Se não for informado, mostrará todos os status.

Exemplo de uso:
  python3 finder.py http://example.com 200  # Mostra apenas status 200
  python3 finder.py http://example.com      # Mostra todos os status

Outros:
  -h, --help     Mostra esta mensagem de ajuda e sai.
""")
    sys.exit(0)

# Verifica se o usuário pediu ajuda ou não passou argumentos
if len(sys.argv) < 2:
    print("Erro: argumentos insuficientes. Use -h para ajuda.")
    sys.exit(1)

if sys.argv[1] in ["-h", "--help"]:
    mostrar_ajuda()

# Pega a URL
url = sys.argv[1]

# Verifica se um status code foi passado, senão exibe todos
status_code_desejado = int(sys.argv[2]) if len(sys.argv) > 2 else None

# Abre a lista de diretórios
try:
    with open("listy.txt", "r") as lista:
        for linha in lista:
            url_go = f"{url}/{linha.strip()}"  # Remove espaços e quebras de linha
            try:
                req = requests.get(url_go)
                if status_code_desejado is None or req.status_code == status_code_desejado:
                    print(f"{url_go} -> {req.status_code}")
            except requests.RequestException as e:
                print(f"Erro ao acessar {url_go}: {e}")
except FileNotFoundError:
    print("Erro: arquivo 'listy.txt' não encontrado.")
    sys.exit(1)
