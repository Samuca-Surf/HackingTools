
# dnsResolver.py

## Descrição

Script simples em Python para resolver o endereço IP de um domínio fornecido como argumento.

---

## Como usar

### Requisitos

* Python 3.x

### Comando para executar

```bash
python3 dnsResolver.py <domínio>
```

### Exemplo

```bash
python3 dnsResolver.py google.com
```

---

## Funcionamento

* Recebe o domínio pelo argumento de linha de comando.
* Utiliza a função `socket.gethostbyname()` para obter o IP correspondente.
* Exibe o endereço IP no terminal.

---

## Exemplo de saída

```
142.250.190.78
```
---
