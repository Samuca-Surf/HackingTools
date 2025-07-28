# 📁 brsub.py

Script Python para bruteforce de subdomínios realizando requisições HTTP e identificando subdomínios válidos.

---

## 🔧 Uso

```bash
python3 brsub.py <dominio> <wordlist>
````

### Exemplo:

```bash
python3 brsub.py exemplo.com subdomains.txt
```

---

## 📌 Descrição

O script `brsub.py` realiza um bruteforce de subdomínios a partir de uma wordlist fornecida, tentando acessar via HTTP cada subdomínio formado e exibindo aqueles que retornam um código HTTP diferente de 404.

### Parâmetros:

* `<dominio>`: o domínio base para teste (ex: google.com)
* `<wordlist>`: arquivo texto contendo uma lista de subdomínios, um por linha

---

## 📄 Wordlist

A wordlist deve conter subdomínios, por exemplo:

```
www
mail
blog
ftp
```

---

## ✅ Funcionamento

* Tenta acessar `http://<subdominio>.<dominio>` para cada subdomínio na lista.
* Se o servidor responder com um código diferente de 404, exibe o URL e o código HTTP.
* Timeout padrão da requisição: 3 segundos.
* Erros de conexão são ignorados silenciosamente.

---

## ⚠️ Observações

* Subdomínios que retornam erro 404 ou falham na conexão são ignorados.
* Não possui suporte a multithreading (varredura sequencial).
* Pode ser necessário rodar com Python 3 e ter o módulo `requests` instalado (`pip install requests`).

---

## 🔎 Exemplo de Saída:

```
http://mail.exemplo.com  >  200
http://blog.exemplo.com  >  301
```

---

## 🧠 Sugestões

* Use uma wordlist personalizada para melhorar a eficácia.
* Combine com outras ferramentas para reconhecimento mais completo.

---

**Ferramenta parte do pacote HackingTools**

