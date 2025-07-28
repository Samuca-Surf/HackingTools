# 📁 bfdomain

Script Bash para bruteforce de subdomínios com consulta DNS por tipo de registro.

---

## 🔧 Uso

```bash
bash bfdomain <dominio> <tipo_de_registro>
```

### Exemplo:

```bash
bash bfdomain exemplo.com A
```

---

## 📌 Descrição

O script `bfdomain` realiza bruteforce de subdomínios com base em uma wordlist e verifica os registros DNS de um tipo especificado (ex: A, MX, TXT).

### Parâmetros:
* Os parâmetros de registros podem ser encontrados em [exemplosdeparametros.txt](/bfdomain/exemplosdeparametros.txt)
* `<dominio>`: o nome base do domínio (ex: google.com)
* `<tipo_de_registro>`: tipo de consulta DNS (A, AAAA, CNAME, MX, etc)

---

## 📄 Wordlist

A wordlist utilizada para subdomínios está em:

```bash
HackingTools/bfdomain/subdomains.txt
```

---

## ✅ Tipos de registros suportados:

* SOA
* CNAME
* A
* AAAA
* NS
* MX
* PTR
* TXT
* HINFO

---

## ⚠️ Observações

* Subdomínios que não existem ou que retornam NXDOMAIN/não encontrados são ignorados.
* O script trata `Ctrl+C` graciosamente, exibindo uma mensagem de interrupção.

---

## 🔎 Exemplo de Saída:

```
mail.exemplo.com has address 192.0.2.5
webmail.exemplo.com has address 192.0.2.6
ftp.exemplo.com has address 192.0.2.7
```

---

## 🧠 Sugestões

* Personalize a wordlist para obter melhores resultados.
* Combine com outras ferramentas do repositório para reconhecimento mais completo.

---

**Ferramenta parte do pacote HackingTools**
