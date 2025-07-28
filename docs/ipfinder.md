# 📄 **Conteúdo do arquivo `ipfinder.md`**

# 📁 ipfinder.sh

Script Bash para identificar hosts ativos em uma sub-rede utilizando ping sequencial.

## 🔧 Uso

```bash
bash ipfinder.sh <prefixo_da_rede>
```

### Exemplo

```bash
bash ipfinder.sh 192.168.0
```

## 📌 Descrição

O script `ipfinder.sh` testa todos os endereços IP dentro de uma rede `/24` (de 1 a 255 no último octeto), enviando um único pacote ICMP (ping) para cada um.
Se houver resposta positiva, o IP é exibido como ativo.

## Parâmetros

* `<prefixo_da_rede>`: Os três primeiros octetos do endereço IP da rede (ex: `192.168.0`, `10.0.0`, etc).

## ✅ Funcionamento

* Utiliza o comando `ping` com:

  * `-c1`: envia apenas 1 pacote
  * `-w1`: espera no máximo 1 segundo por resposta
* Utiliza `grep` e `cut` para filtrar e extrair os IPs que responderam com sucesso.
* Itera de 1 até 255 para cobrir a faixa comum de redes /24.

## ⚠️ Observações

* Necessário ter permissão para enviar pacotes ICMP (ping) — pode exigir `sudo` em alguns sistemas.
* O script ignora IPs que não respondem dentro de 1 segundo.
* Não detecta máquinas com ICMP desabilitado (como firewalls).

## 🔎 Exemplo de Saída

```plaintext
Testando rede 192.168.0.*
192.168.0.1:
192.168.0.100:
192.168.0.103:
```

## 🧠 Sugestões

* Combine com `nmap` para escaneamento mais profundo após identificar IPs ativos.
* Use múltiplos processos em paralelo para aumentar a velocidade (ex: com `xargs -P`).
* Modifique para salvar resultados em arquivo ou exportar como JSON.

---

**Ferramenta parte do pacote HackingTools**
