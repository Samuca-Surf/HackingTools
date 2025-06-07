---

# 🛠️ WebH – Ferramentas de Análise e Testes em Redes

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

---

## ▶️ Como usar

### Requisitos

* **Python 3.x**
* Ferramentas Linux padrão (para scripts `.sh`): `bash`, `ping`, `wget`, `grep`, `host`, `cut`, `sort`

### Execução rápida

```bash
python3 portScanner.py <IP>
python3 dnsResolve.py <domínio>
bash domainHunt.sh <URL>
bash pingTool.sh <IP ou domínio>
```

---

## ⚠️ Aviso legal

Este projeto tem fins **educacionais**.
**Não use essas ferramentas para atacar ou interferir em sistemas que você não tem autorização expressa para testar.**

Você é responsável pelo uso das ferramentas aqui disponibilizadas.

---
