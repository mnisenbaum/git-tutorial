# Lab 5 — GitHub: remote, push, pull e clone

## 🎯 Objetivo

Conectar seu repositório local ao GitHub e aprender a enviar/baixar mudanças.

```
git push   →   Local ──────▶ GitHub   (envia)
git pull   →   Local ◀────── GitHub   (recebe)
git clone  →   GitHub ─────▶ cria pasta local nova
```

---

## 📋 Passo a passo

### 1. Crie um repositório vazio no GitHub

1. Acesse [github.com](https://github.com) → **New repository**
2. Nome sugerido: `lab5-automation`
3. **Não** marque "Add a README"
4. Clique em **Create repository**
5. Copie a URL HTTPS, algo como:
```
https://github.com/seu-usuario/lab5-automation.git
```

### 2. Prepare a pasta local

```bash
mkdir lab5-trabalho
cd lab5-trabalho
git init
```

Copie os arquivos desta pasta (`lab5/`) para dentro de `lab5-trabalho`.

```bash
git add .
git commit -m "Primeiro commit do laboratorio de automacao"
```

### 3. Conecte ao repositório remoto

```bash
git remote add origin https://github.com/seu-usuario/lab5-automation.git
```

Confirme a conexão:

```bash
git remote -v
```

```
origin  https://github.com/seu-usuario/lab5-automation.git (fetch)
origin  https://github.com/seu-usuario/lab5-automation.git (push)
```

### 4. Envie (push) para o GitHub

```bash
git branch -M main
git push -u origin main
```

> Atualize a página do repositório no GitHub — seus arquivos devem aparecer lá!

### 5. Simule uma mudança feita "na nuvem"

No site do GitHub, edite o arquivo `notas.md` diretamente (clique no lápis ✏️) e faça um commit pela interface web.

### 6. Baixe (pull) essa mudança

De volta ao terminal:

```bash
git pull origin main
```

Veja o arquivo `notas.md` atualizado na sua pasta local.

---

## 🧪 Bônus: `git clone`

Simule um colega de equipe que ainda não tem o projeto. Em **outra pasta**, qualquer uma:

```bash
cd ..
git clone https://github.com/seu-usuario/lab5-automation.git lab5-colega
cd lab5-colega
ls
```

Repare: ele já recebe **todo o histórico**, sem precisar de `git init` nem `remote add` — o `clone` faz tudo de uma vez.

```
git init + remote add + pull   ≈   git clone
```

---

## 🧪 Mão na massa — Cenário CCNA Automation

Você está documentando um laboratório de automação em equipe:

1. Suba o `playbook_inventario.yml` e o `README_lab.md` para o GitHub
2. Peça para um colega (ou simule você mesmo) clonar o repositório
3. Ele faz uma mudança e sobe (`push`)
4. Você baixa essa mudança (`pull`) antes de continuar trabalhando

> 💡 Esse vai-e-vem é exatamente o fluxo usado em equipes de NetDevOps.

---

## 📝 Exercício

1. Crie o repositório `lab5-automation` no GitHub
2. Suba os arquivos desta pasta com `push`
3. Edite algo pela interface web do GitHub
4. Baixe com `pull`
5. **Desafio extra:** clone o repositório numa pasta separada e confira se todo o histórico (`git log`) veio junto

---

## ✅ Checklist de conclusão

- [ ] Repositório criado no GitHub
- [ ] `git remote add origin` configurado
- [ ] `git push` funcionando
- [ ] `git pull` funcionando
- [ ] `git clone` testado em uma pasta separada

---

➡️ Próximo: **lab6** (Branches)
