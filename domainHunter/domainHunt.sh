#!/bin/bash

url=$1

echo "===================="
echo "Analisando $url"
echo "===================="

# Baixa o conteúdo da página com user-agent e evita conteúdo binário
wget -q --user-agent="Mozilla/5.0" -O index.html $url

# Extrai domínios de links válidos ignorando avisos de binário
grep -a "href" index.html > saida
grep "http" saida | cut -d "/" -f 3 | grep "\." | grep -v " " | sort -u > dominios

# Resolve domínios para IPs
for domain in $(cat dominios); do
    ip=$(host $domain | grep "has address" | cut -d " " -f 4)
    if [[ ! -z "$ip" ]]; then
        echo "$ip    $domain"
    fi
done
