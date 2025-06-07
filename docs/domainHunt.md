# domainHunt.sh

## Descrição

Script em Bash para coletar domínios presentes em links de uma página web e resolver seus respectivos endereços IP.

---

## Como usar

### Requisitos

* Linux ou ambiente Unix com `bash`
* Ferramentas: `wget`, `grep`, `host`, `cut`, `sort`

### Comando para executar

```bash
bash domainHunt.sh <URL>
```

### Exemplo

```bash
bash domainHunt.sh https://www.example.com
```

---

## Funcionamento

1. Baixa o conteúdo da página especificada usando `wget` com um user-agent para simular navegador.
2. Extrai todos os links (href) e filtra para obter os domínios únicos.
3. Para cada domínio extraído, realiza uma resolução DNS para obter o IP associado.
4. Exibe no terminal uma lista com IP e domínio correspondentes.

---

## Exemplo de saída

```
====================
Analisando https://www.example.com
====================
93.184.216.34    www.example.com
151.101.1.69     example.com
```

---

## Observações

* O script salva temporariamente arquivos `index.html`, `saida`, e `dominios` no diretório atual.
* É recomendado rodar em um diretório temporário ou limpar esses arquivos depois do uso.
* Pode ser expandido para incluir subdomínios ou outros tipos de dados.

---
