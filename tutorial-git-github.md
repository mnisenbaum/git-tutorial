# Tutorial Git & GitHub para Iniciantes

---

## 1) O que é Git?

Git é um **sistema de controle de versão**. Ele tira "fotos" (commits) do seu projeto ao longo do tempo, permitindo voltar atrás, comparar mudanças e trabalhar em equipe sem sobrescrever o trabalho dos outros.

```
Sem Git:                        Com Git:
projeto_final.zip                projeto/ ──commit1──commit2──commit3──▶
projeto_final_v2.zip                              \
projeto_final_v2_USAR.zip                          branch-experimento
```

**Git** = ferramenta que roda no seu computador.
**GitHub** = site que hospeda repositórios Git na nuvem (backup + colaboração).

---

## 2) Configurando usuário e email

Antes de tudo, diga ao Git quem você é (aparece em cada commit):

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
```

Conferir:

```bash
git config --list
```

> Faça isso **uma única vez** por computador.

---

## 3) Inicializando o Git em uma pasta

```bash
cd minha-pasta
git init
```

```
minha-pasta/
└── .git/   ← pasta oculta criada (aqui mora todo o histórico)
```

Conferir se deu certo:

```bash
git status
```

---

## 4) `git add`

Diz ao Git **quais arquivos** você quer incluir no próximo commit (área de "staging").

```
Arquivos no disco  →  git add  →  Staging Area  →  git commit  →  Histórico
(modificados)                     (preparados)                   (salvo)
```

```bash
git add arquivo.txt        # um arquivo específico
git add pasta/             # uma pasta inteira
git add .                  # tudo que mudou
```

Ver o que está na "staging area":

```bash
git status
```

### Bônus: `.gitignore`

Arquivo que diz ao Git o que **nunca** adicionar (senhas, dependências, lixo).

Crie um arquivo chamado `.gitignore` na raiz do projeto:

```
node_modules/
.env
*.log
.DS_Store
```

---

## 5) `git commit`

"Tira a foto" do que está na staging area, com uma mensagem explicando o que mudou.

```bash
git commit -m "Adiciona tela de login"
```

Fluxo completo:

```bash
git add .
git commit -m "Mensagem clara e curta"
```

Ver o histórico de commits:

```bash
git log
git log --oneline    # versão resumida
```

```
* a1b2c3d Adiciona tela de login
* 9f8e7d6 Corrige bug no cadastro
* 1234abc Primeiro commit
```

### 📝 Exercício 1
1. Crie uma pasta `teste-git`
2. Rode `git init`
3. Crie um arquivo `oi.txt` com o texto "Olá Git!"
4. Faça `git add` e `git commit`
5. Rode `git log` e veja seu commit aparecer

---

## 6) Criando um repositório vazio no GitHub

1. Acesse [github.com](https://github.com) e faça login
2. Clique em **New repository** (botão verde)
3. Dê um nome (ex: `meu-projeto`)
4. **NÃO** marque "Add a README" (para não dar conflito depois)
5. Clique em **Create repository**

Você verá uma tela com uma URL parecida com:

```
https://github.com/seu-usuario/meu-projeto.git
```

Guarde essa URL — você vai usar no próximo passo.

---

## 7) Sincronizando Git com GitHub

### Conectar pasta local ao repositório remoto

```bash
git remote add origin https://github.com/seu-usuario/meu-projeto.git
```

```
Seu computador (local)  ⇄  remote "origin"  ⇄  GitHub (nuvem)
```

### Enviar (push) seus commits para o GitHub

```bash
git branch -M main
git push -u origin main
```

> `-u` salva essa conexão, então da próxima vez basta `git push`

### Baixar (pull) mudanças do GitHub

```bash
git pull origin main
```

### Clonar um repositório que já existe no GitHub

Quando o repositório já existe e você quer **baixar tudo** pela primeira vez:

```bash
git clone https://github.com/usuario/repositorio.git
```

```
git push   →   Local ──────▶ GitHub   (envia)
git pull   →   Local ◀────── GitHub   (recebe)
git clone  →   GitHub ─────▶ Cria pasta local nova
```

### 📝 Exercício 2
1. Crie um repositório vazio no GitHub
2. Conecte sua pasta `teste-git` a ele (`git remote add origin ...`)
3. Faça `git push -u origin main`
4. Atualize a página do repositório no GitHub e veja seu arquivo lá

---

## 8) Trabalhando com Branches

Branch = uma "linha do tempo paralela" do projeto, para testar coisas sem bagunçar a principal (`main`).

```
main:        A───B───C───────────F
                  \             /
nova-feature:      D───E───────
```

### Criar uma branch

```bash
git branch nova-feature
```

### Navegar entre branches

```bash
git checkout nova-feature
# ou (forma mais nova)
git switch nova-feature
```

Criar e já entrar na branch em um único comando:

```bash
git checkout -b nova-feature
```

Ver em qual branch você está / quais existem:

```bash
git branch
```
```
* nova-feature
  main
```
(o `*` mostra a branch atual)

### Fazer merge (juntar branches)

Volte para a `main` e traga as mudanças da outra branch:

```bash
git checkout main
git merge nova-feature
```

```
Antes do merge:          Depois do merge:
main:    A───B            main:    A───B───────F
              \                         \      /
feature:       D───E       feature:      D────E
```

### ⚠️ Conflito de merge (básico)

Acontece quando duas branches mudam a **mesma linha** do mesmo arquivo.

O Git marca o arquivo assim:

```
<<<<<<< HEAD
Esta é a versão da branch main
=======
Esta é a versão da branch nova-feature
>>>>>>> nova-feature
```

**Como resolver:**
1. Abra o arquivo
2. Apague as marcações (`<<<<<<<`, `=======`, `>>>>>>>`) e decida o que fica
3. Salve, depois:
```bash
git add arquivo-com-conflito.txt
git commit -m "Resolve conflito de merge"
```

### Deletar uma branch

```bash
git branch -d nova-feature      # deleta se já teve merge
git branch -D nova-feature      # força deletar (mesmo sem merge)
```

### 📝 Exercício 3
1. No repositório `teste-git`, rode `git checkout -b cor-favorita`
2. Edite `oi.txt` adicionando uma linha
3. `git add` + `git commit`
4. Volte para `main`: `git checkout main`
5. `git merge cor-favorita`
6. Delete a branch: `git branch -d cor-favorita`

---

## 🎯 Resumo dos comandos essenciais

| Comando | O que faz |
|---|---|
| `git init` | Inicia um repositório |
| `git status` | Mostra o estado atual |
| `git add .` | Prepara arquivos para commit |
| `git commit -m "msg"` | Salva uma versão |
| `git log --oneline` | Histórico resumido |
| `git remote add origin <url>` | Conecta ao GitHub |
| `git push` | Envia commits para o GitHub |
| `git pull` | Baixa commits do GitHub |
| `git clone <url>` | Baixa um repositório inteiro |
| `git branch` | Lista branches |
| `git checkout -b nome` | Cria e entra numa branch |
| `git merge nome` | Junta uma branch na atual |
| `git branch -d nome` | Deleta uma branch |

---

## 🗺️ Fluxo completo (do zero ao GitHub)

```
git init
   ↓
git add .
   ↓
git commit -m "primeiro commit"
   ↓
git remote add origin <url>
   ↓
git push -u origin main
   ↓
(no dia a dia)
   ↓
git checkout -b nova-feature → trabalha → add → commit → checkout main → merge → push
```
