# Lab 2 — Inicializando um repositório (`git init`)

## 🎯 Objetivo

Aprender a transformar uma pasta comum em um repositório Git, entendendo o que acontece "por baixo dos panos".

---

## 📋 Passo a passo

### 1. Crie uma pasta de trabalho

```bash
mkdir lab2-trabalho
cd lab2-trabalho
```

### 2. Inicialize o Git

```bash
git init
```

Saída esperada:

```
Initialized empty Git repository in .../lab2-trabalho/.git/
```

### 3. Veja a pasta oculta `.git`

```bash
ls -la
```

```
lab2-trabalho/
└── .git/   ← aqui mora TODO o histórico do projeto
```

> ⚠️ Nunca delete a pasta `.git` manualmente, a não ser que queira apagar todo o histórico do repositório.

### 4. Verifique o status

```bash
git status
```

Saída esperada:

```
On branch main
No commits yet
nothing to commit (create/copy files and use "git add" to track)
```

---

## 🧪 Mão na massa — Cenário CCNA Automation

Você vai começar um projeto de automação para inventário de dispositivos de rede. Use o arquivo de exemplo deste lab:

```
lab2/
└── inventario.yml
```

1. Copie o arquivo `inventario.yml` (fornecido nesta pasta) para dentro da sua pasta `lab2-trabalho`
2. Rode `git status` e observe que o Git já enxerga o arquivo, mas ainda como **não rastreado** (untracked)

```
Untracked files:
  inventario.yml
```

> Isso significa: o arquivo existe na pasta, mas o Git ainda não está "vigiando" ele. Isso é assunto do próximo lab (`git add`)!

---

## 📝 Exercício

1. Crie a pasta `lab2-trabalho` e rode `git init`
2. Copie `inventario.yml` para dentro dela
3. Rode `git status` e leia a saída com atenção
4. **Desafio extra:** rode `git init` de novo, dentro da mesma pasta. O que acontece? (Dica: não tem perigo, leia a mensagem)

---

## ✅ Checklist de conclusão

- [ ] Pasta `.git` criada com sucesso
- [ ] Entendi a diferença entre pasta comum e repositório Git
- [ ] `git status` mostrando arquivo "untracked"

---

➡️ Próximo: **lab3** (`git add`)
