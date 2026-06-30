# Lab 4 — `git commit`

## 🎯 Objetivo

Aprender a "tirar fotos" do projeto (commits), escrever boas mensagens e navegar pelo histórico.

```
git add  →  Staging Area  →  git commit  →  Histórico (permanente)
```

---

## 📋 Passo a passo

### 1. Prepare a pasta de trabalho

```bash
mkdir lab4-trabalho
cd lab4-trabalho
git init
```

Copie os arquivos desta pasta (`lab4/`) para dentro de `lab4-trabalho`.

### 2. Primeiro commit

```bash
git add inventario.yml
git commit -m "Adiciona inventario inicial de dispositivos"
```

### 3. Veja o histórico

```bash
git log
```

```
commit a1b2c3d4...
Author: Seu Nome <seuemail@exemplo.com>
Date:   ...

    Adiciona inventario inicial de dispositivos
```

Versão resumida:

```bash
git log --oneline
```

```
a1b2c3d Adiciona inventario inicial de dispositivos
```

### 4. Faça mais alterações e mais commits

Edite o arquivo `playbook_backup.yml` (adicione qualquer comentário), depois:

```bash
git add playbook_backup.yml
git commit -m "Adiciona playbook de backup das configuracoes"
```

Edite `topologia.md`, depois:

```bash
git add topologia.md
git commit -m "Documenta topologia da rede do laboratorio"
```

### 5. Veja o histórico crescer

```bash
git log --oneline
```

```
c3d4e5f Documenta topologia da rede do laboratorio
b2c3d4e Adiciona playbook de backup das configuracoes
a1b2c3d Adiciona inventario inicial de dispositivos
```

```
●───────●───────●
a1b2c3d b2c3d4e c3d4e5f
(inventário) (playbook) (topologia)
```

---

## ✍️ Boas práticas de mensagem de commit

| ❌ Ruim | ✅ Bom |
|---|---|
| "mudanças" | "Corrige IP da interface Gi0/1 no R1" |
| "fix" | "Corrige erro de sintaxe no playbook de backup" |
| "final final v2" | "Adiciona VLAN de voz na configuração do SW1" |

**Regra de ouro:** a mensagem deve completar a frase *"Este commit vai..."*

---

## 🧪 Mão na massa — Cenário CCNA Automation

Você está documentando e versionando, passo a passo, a criação de um laboratório de automação:

1. Commit 1: inventário de dispositivos
2. Commit 2: playbook de backup
3. Commit 3: documentação da topologia
4. Commit 4: **você decide!** Adicione algo novo (ex: um arquivo `variaveis.yml`) e faça seu próprio commit com mensagem clara

---

## 📝 Exercício

1. Siga os passos acima e gere pelo menos 4 commits
2. Rode `git log --oneline` e copie a saída
3. **Desafio extra:** rode `git log -p -1` (mostra o que mudou no último commit, no formato "diff"). Tente entender as linhas com `+` e `-`

---

## ✅ Checklist de conclusão

- [ ] Fiz múltiplos commits com mensagens claras
- [ ] Sei usar `git log` e `git log --oneline`
- [ ] Entendo que cada commit é um "ponto de restauração" do projeto

---

➡️ Próximo: **lab5** (GitHub: remoto, push, pull, clone)
