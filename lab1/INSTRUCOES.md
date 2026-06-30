# Lab 1 — Configurando usuário e email no Git

## 🎯 Objetivo

Configurar sua identidade no Git, para que todo commit que você fizer fique assinado com seu nome e email.

---

## 📋 Passo a passo

### 1. Verifique se já existe alguma configuração

```bash
git config --list
```

Se aparecer `user.name` e `user.email`, alguém já configurou antes (ou é outra pessoa).

### 2. Configure seu nome

```bash
git config --global user.name "Seu Nome Completo"
```

### 3. Configure seu email

> 💡 Use o mesmo email da sua conta GitHub — assim os commits ficam vinculados ao seu perfil.

```bash
git config --global user.email "seuemail@exemplo.com"
```

### 4. Confirme a configuração

```bash
git config --global user.name
git config --global user.email
```

Saída esperada:

```
Seu Nome Completo
seuemail@exemplo.com
```

---

## 🧪 Mão na massa — Cenário CCNA Automation

Imagine que você é o engenheiro responsável por automatizar a configuração de switches de um laboratório. Antes de começar a versionar qualquer script, configure sua identidade:

```bash
git config --global user.name "Tech NetAutomation"
git config --global user.email "tech.netautomation@lab.com"
```

---

## 📝 Exercício

1. Configure seu `user.name` e `user.email` globalmente
2. Rode `git config --list` e tire um print (ou copie a saída) mostrando as duas linhas configuradas
3. **Desafio extra:** configure um `user.email` **diferente** apenas para este repositório (sem `--global`), simulando que você usa um email pessoal no GitHub mas um corporativo no trabalho:

```bash
git config user.email "trabalho@empresa.com"
```

4. Rode `git config user.email` (sem `--global`) e depois `git config --global user.email`. Compare os dois resultados — qual vence dentro do repositório?

---

## ✅ Checklist de conclusão

- [ ] `user.name` configurado globalmente
- [ ] `user.email` configurado globalmente
- [ ] Entendi a diferença entre config `--global` e config local do repositório

---

➡️ Próximo: **lab2** (`git init`)
