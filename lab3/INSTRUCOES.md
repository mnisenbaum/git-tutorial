# Lab 3 — `git add` e `.gitignore`

## 🎯 Objetivo

Aprender a colocar arquivos na "área de preparação" (staging area) e a ignorar arquivos que não devem ser versionados.

```
Arquivos no disco  →  git add  →  Staging Area  →  (próximo lab: git commit)
   (modificados)                  (preparados)
```

---

## 📋 Passo a passo

### 1. Prepare a pasta de trabalho

```bash
mkdir lab3-trabalho
cd lab3-trabalho
git init
```

### 2. Copie os arquivos de exemplo

Copie todos os arquivos desta pasta (`lab3/`) para dentro de `lab3-trabalho`:

```
lab3/
├── switch_sw1.cfg
├── router_r1.cfg
├── script_backup.py
├── senhas.env
└── .gitignore
```

### 3. Veja o status antes de adicionar nada

```bash
git status
```

Tudo deve aparecer como `Untracked files`.

### 4. Adicione um arquivo específico

```bash
git add switch_sw1.cfg
git status
```

Repare que `switch_sw1.cfg` agora está em verde (staged), os outros continuam não rastreados.

### 5. Adicione tudo de uma vez

```bash
git add .
git status
```

> ⚠️ Repare: o arquivo `senhas.env` **não foi adicionado**! Veja por quê no próximo passo.

### 6. Entenda o `.gitignore`

Abra o arquivo `.gitignore` desta pasta:

```
*.env
__pycache__/
*.log
```

Isso diz ao Git: "nunca rastreie arquivos `.env`, pastas `__pycache__` ou arquivos `.log`" — mesmo que alguém rode `git add .`.

> 💡 Isso é **essencial** em automação de redes: você nunca quer subir senhas (`.env`) ou credenciais para o GitHub.

---

## 🧪 Mão na massa — Cenário CCNA Automation

Você é responsável por versionar os backups de configuração de `SW1` e `R1`, além de um script Python de backup automático. Porém o arquivo `senhas.env` guarda credenciais reais dos dispositivos — ele **jamais** pode ir para o repositório.

1. Adicione `switch_sw1.cfg`, `router_r1.cfg` e `script_backup.py` ao staging
2. Confirme com `git status` que `senhas.env` continua de fora
3. Tente forçar a adição do arquivo ignorado (só para aprender):

```bash
git add -f senhas.env
```

4. Depois, **desfaça** isso, removendo do staging:

```bash
git reset senhas.env
```

---

## 📝 Exercício

1. Repita o passo a passo acima na sua própria pasta
2. Edite o `.gitignore` adicionando mais uma regra: ignorar qualquer arquivo `.bak`
3. Crie um arquivo vazio `teste.bak` e confirme que ele não aparece no `git add .`
4. **Desafio extra:** rode `git status` e depois `git restore --staged switch_sw1.cfg`. O que aconteceu com o arquivo? Ele saiu do projeto ou só saiu do staging?

---

## ✅ Checklist de conclusão

- [ ] Sei adicionar um arquivo específico com `git add`
- [ ] Sei adicionar tudo com `git add .`
- [ ] Entendi como o `.gitignore` protege arquivos sensíveis
- [ ] Sei remover algo do staging sem apagar o arquivo (`git reset` / `git restore --staged`)

---

➡️ Próximo: **lab4** (`git commit`)
