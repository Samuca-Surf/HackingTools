find_dir é uma ferramenta simples de fuzzing de diretórios para testar a presença de caminhos em sites e servidores. Ela utiliza uma wordlist(listy.txt) para fazer requisições HTTP e filtrar as respostas com base no código de status desejado.

Uso da ferramenta : python3 finder.py [STATUS_CODE]

Descrição: Ferramenta de fuzzing de diretórios que testa caminhos de um arquivo de wordlist e exibe apenas os que retornam o código de status HTTP especificado.

Argumentos: A URL alvo (ex: http://example.com) [STATUS_CODE] (Opcional) O código de status HTTP desejado (ex: 200, 403, 404). Se não for informado, mostrará todos os status.

Exemplo de uso: python3 finder.py http://example.com 200 # Mostra apenas status 200 python3 finder.py http://example.com # Mostra todos os status

Outros: -h, --help Mostra esta mensagem de ajuda e sai.
