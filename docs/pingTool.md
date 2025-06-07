---

# pingTool.sh

## Descrição

Script simples em Bash para enviar um único pacote de ping para um IP ou domínio fornecido.

---

## Como usar

### Requisitos

* Sistema com `bash` e o comando `ping` disponível (Linux, macOS, WSL, etc.)

### Comando para executar

```bash
bash pingTool.sh <IP_ou_domínio>
```

### Exemplo

```bash
bash pingTool.sh 8.8.8.8
```

---

## Funcionamento

* Recebe um endereço IP ou domínio como argumento.
* Exibe no terminal a mensagem "pingando o IP X".
* Executa um único `ping` (`-c1`) ao destino e mostra o resultado padrão do sistema.

---

## Exemplo de saída

```
pingando o IP 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=12.4 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 12.429/12.429/12.429/0.000 ms
```

---

## Observações

* Para verificar múltiplos IPs, você pode usar esse script em conjunto com um loop em um arquivo `.txt`:

```bash
while read ip; do bash pingTool.sh $ip; done < lista.txt
```

* Em sistemas Windows com `Git Bash`, o comando `ping` pode ter opções diferentes (como `-n` ao invés de `-c`).

---
