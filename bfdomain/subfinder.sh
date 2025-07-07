#!/bin/bash

# Verificação de parâmetros
if [[ $# -lt 2 ]]; then
    echo "Uso: $0 <dominio> <tipo_de_registro>"
    echo "Exemplo: $0 exemplo.com A"
    exit 1
fi

dominio="$1"
tipo="$2"
wordlist="/home/Samuca/bin/bfdomain/subdomains.txt"

# Validação opcional (lista de tipos válidos)
tipos_validos="SOA CNAME A AAAA NS MX PTR TXT HINFO"

if ! grep -qw "$tipo" <<< "$tipos_validos"; then
    echo "[!] Tipo de registro inválido: $tipo"
    echo "Tipos válidos: $tipos_validos"
    exit 1
fi

# Handler para Ctrl+C
trap 'echo -e "\n[!] Interrompido pelo usuário. Saindo..."; exit 1' SIGINT

# Loop de consulta
while IFS= read -r sub
do
    fqdn="${sub}.${dominio}"
    result=$(host -t "$tipo" "$fqdn" 2>/dev/null)

    # Filtro: só mostrar se NÃO contiver "has no", "NXDOMAIN" ou "not found"
    if [[ -n "$result" ]] && ! grep -qiE 'has no|NXDOMAIN|not found' <<< "$result"; then
        echo "$result"
    fi

done < "$wordlist"

