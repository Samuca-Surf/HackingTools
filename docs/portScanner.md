# portScanner.py

## Descrição

Script em Python para realizar **varredura completa de portas TCP** em um host/alvo especificado. Além de verificar quais portas estão abertas, o script tenta capturar o **banner do serviço** em execução, caso esteja disponível.

---

## Como usar

### Requisitos

* Python 3.x instalado

### Comando para executar

```bash
python3 portScanner.py <endereço_IP_ou_dominio>
```

### Exemplo

```bash
python3 portScanner.py 192.168.0.1
```

---

## Como funciona

* O script tenta conectar-se a todas as portas TCP entre 1 e 65535 no host informado.
* Para cada porta aberta, tenta ler até 1024 bytes do banner do serviço.
* Caso não consiga ler o banner, exibe "Não identificado".

---

## Exemplo de saída

```
22 SSH-2.0-OpenSSH_7.4
80 Apache/2.4.29 (Ubuntu)
443 nginx/1.14.0 (Ubuntu)
3306 Não identificado
```

---

## Observações

* O script usa timeout curto (0.5 segundos) para não demorar demais.
* Pode gerar erros se a conexão for recusada ou bloqueada.
