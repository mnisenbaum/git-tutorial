# Lab 6 — Branches (criar, navegar, merge, delete)

## 🎯 Objetivo

Aprender a trabalhar com branches para testar mudanças sem afetar a versão principal do projeto — e resolver um conflito básico de merge.

```
main:        A───B───C───────────F
                  \             /
nova-feature:      D───E───────
```

---

## 📋 Passo a passo

### 1. Prepare a pasta de trabalho

```bash
mkdir lab6-trabalho
cd lab6-trabalho
git init
```

Copie os arquivos desta pasta (`lab6/`) para dentro de `lab6-trabalho`, depois:

```bash
git add .
git commit -m "Configuracao inicial do laboratorio"
```

### 2. Crie uma branch

```bash
git branch vlan-voz
```

### 3. Veja as branches existentes

```bash
git branch
```

```
* main
  vlan-voz
```

(o `*` indica em qual branch você está)

### 4. Navegue até a nova branch

```bash
git checkout vlan-voz
# ou
git switch vlan-voz
```

> 💡 Atalho para criar **e** entrar de uma vez: `git checkout -b vlan-voz`

### 5. Faça uma mudança só nessa branch

Edite `switch_sw1.cfg` e adicione a VLAN de voz (exemplo já comentado no arquivo). Depois:

```bash
git add switch_sw1.cfg
git commit -m "Adiciona VLAN de voz no SW1"
```

### 6. Volte para a `main` e veja que ela NÃO tem essa mudança

```bash
git checkout main
cat switch_sw1.cfg
```

> A VLAN de voz não está aqui — ela só existe na branch `vlan-voz`. Isso é o poder das branches!

### 7. Faça o merge

```bash
git merge vlan-voz
```

```
Antes:                    Depois:
main:    A───B             main:    A───B───────F
              \                          \      /
vlan-voz:      D───E       vlan-voz:      D────E
```

### 8. Delete a branch (já não precisa mais dela)

```bash
git branch -d vlan-voz
```

---

## ⚠️ Conflito de merge — na prática

### 1. Crie duas branches que mexem na mesma linha

```bash
git checkout -b time-rio
```

Edite a linha `# HOSTNAME: ...` em `router_r1.cfg` para `# HOSTNAME: R1-RIO`. Commit:

```bash
git add router_r1.cfg
git commit -m "Define hostname como R1-RIO"
```

Volte para `main` e crie outra branch:

```bash
git checkout main
git checkout -b time-sp
```

Edite a **mesma linha** `# HOSTNAME: ...` para `# HOSTNAME: R1-SP`. Commit:

```bash
git add router_r1.cfg
git commit -m "Define hostname como R1-SP"
```

### 2. Gere o conflito

```bash
git checkout main
git merge time-rio        # ok, sem conflito ainda
git merge time-sp         # CONFLITO!
```

Você verá algo como:

```
CONFLICT (content): Merge conflict in router_r1.cfg
Automatic merge failed; fix conflicts and then commit the result.
```

### 3. Abra o arquivo e resolva

```
<<<<<<< HEAD
# HOSTNAME: R1-RIO
=======
# HOSTNAME: R1-SP
>>>>>>> time-sp
```

Decida (ou combine os dois), apague as marcações, salve e:

```bash
git add router_r1.cfg
git commit -m "Resolve conflito de hostname entre RIO e SP"
```

### 4. Limpe as branches usadas

```bash
git branch -d time-rio
git branch -d time-sp
```

---

## 🧪 Mão na massa — Cenário CCNA Automation

Times distribuídos (RIO e SP) configurando o mesmo roteador em paralelo, cada um em sua branch — é exatamente assim que equipes reais de NetDevOps evitam pisar no trabalho uma da outra, resolvendo divergências apenas no merge.

---

## 📝 Exercício

1. Crie a branch `vlan-voz`, faça a mudança, dê merge e delete a branch
2. Reproduza o cenário de conflito (`time-rio` x `time-sp`) e resolva manualmente
3. **Desafio extra:** depois de resolver o conflito, rode `git log --oneline --graph --all`. Você consegue visualizar as duas branches se encontrando?

---

## ✅ Checklist de conclusão

- [ ] Criei e naveguei entre branches
- [ ] Fiz merge sem conflito
- [ ] Reproduzi e resolvi um conflito de merge manualmente
- [ ] Deletei branches já mescladas

---

➡️ Próximo: **lab-final** (desafio que junta tudo)
