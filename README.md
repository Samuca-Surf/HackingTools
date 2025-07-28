![Logo do Projeto](img/HackingToolsImage.png)
---

# 🛠️ HackingTools – Ferramentas de Análise e Testes em Redes

Este repositório reúne scripts simples e diretos, feitos em **Python** e **Bash**, para auxiliar em atividades de análise de rede, reconhecimento e testes básicos de segurança.

---

## 📂 Ferramentas incluídas

### 🔎 `portScanner.py`

Scanner de portas TCP completo (1–65535), com tentativa de captura de banner nos serviços abertos.
📄 [Manual](docs/portScanner.md)

### 🌐 `dnsResolver.py`

Resolve o IP de um domínio informado.
📄 [Manual](docs/dnsResolver.md)

### 🕸️ `domainHunt.sh`

Coleta todos os domínios presentes nos links de uma página HTML e resolve seus respectivos IPs.
📄 [Manual](docs/domainHunt.md)

### 📶 `pingTool.sh`

Envia um único pacote de ping para um IP ou domínio e exibe a resposta.
📄 [Manual](docs/pingTool.md)

### 📁 `finder.py`

Faz fuzzing de diretórios com base em uma wordlist local (`listy.txt`). Exibe caminhos que retornam o status HTTP desejado.
📄 [Manual](docs/finder.md)

### 📁 `subfinder.sh`

Script Bash que faz bruteforce de subdomínios com consulta DNS por tipo de registro.
📄 [Manual](docs/bfdomain.md)

### 📁 `brsub.py`

Script Python para bruteforce de subdomínios realizando requisições HTTP e identificando subdomínios válidos.
📄 [Manual](docs/brsub.md)

### 📁 `ipfinder.sh`

Script Bash para identificar hosts ativos em uma sub-rede utilizando ping sequencial.
📄[Manual](docs/ipfinder.md)

---

## ▶️ Como usar

### Requisitos

* **Python 3.x**
* Biblioteca `requests` (`pip install requests`)
* Ferramentas Linux padrão (para scripts `.sh`): `bash`, `ping`, `wget`, `grep`, `host`, `cut`, `sort`

### Execução rápida

```bash
python3 portScanner.py <IP>
python3 dnsResolve.py <domínio>
bash domainHunt.sh <URL>
bash pingTool.sh <IP ou domínio>
python3 finder.py <URL> [STATUS_CODE]
```
---
## 💸 Apoie o Projeto

Se este projeto te ajudou ou você quer apoiar o desenvolvimento:

- **Bitcoin (BTC):** `bc1q3hyrqzvvrlqrc94lpaa3jyqyvtakehq50zaks2`

Obrigado pelo apoio! 🙏



---

## ⚠️ Aviso legal

Este projeto tem fins **educacionais**.
**Não use essas ferramentas para atacar ou interferir em sistemas que você não tem autorização expressa para testar.**

Você é responsável pelo uso das ferramentas aqui disponibilizadas.

---
