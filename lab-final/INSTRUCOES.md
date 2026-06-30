# Lab Final — Desafio Completo 🏁

## 🎯 Objetivo

Juntar tudo que você praticou nos labs 1 a 6 em um único cenário, simulando um projeto real de automação de rede do início ao fim.

> 💡 Este lab é **mais aberto** que os anteriores — menos passo a passo, mais "resolva você mesmo". Use os labs anteriores como referência sempre que precisar.

---

## 🗺️ Cenário

Você é o engenheiro de automação responsável por configurar o controle de versão de um novo projeto de **backup e auditoria de configurações de rede** para uma filial. Os arquivos iniciais já existem nesta pasta (`lab-final/`) — seu trabalho é versioná-los corretamente, do zero até o GitHub, com um fluxo de branches incluso.

```
lab-final/
├── inventario.yml
├── playbook_backup.yml
├── playbook_auditoria.yml
├── switch_sw1.cfg
├── router_r1.cfg
├── credenciais.env      ← NUNCA pode ir para o GitHub!
└── docs/
    └── topologia.md
```

---

## ✅ Missões

Resolva cada missão por conta própria. Se travar, volte ao lab correspondente entre parênteses.

### Missão 1 — Configuração e início *(labs 1 e 2)*
- [ ] Configure seu `user.name` e `user.email` (se ainda não fez)
- [ ] Copie os arquivos desta pasta para uma pasta de trabalho `lab-final-trabalho`
- [ ] Inicialize o Git

### Missão 2 — Proteja as credenciais *(lab 3)*
- [ ] Crie um `.gitignore` que impeça `credenciais.env` de ser versionado
- [ ] Confirme com `git status` que ele nunca aparece como rastreável

### Missão 3 — Primeiros commits *(labs 3 e 4)*
- [ ] Faça o primeiro commit com `inventario.yml` e `docs/topologia.md`
- [ ] Faça um segundo commit com os dois playbooks
- [ ] Faça um terceiro commit com as configs (`switch_sw1.cfg` e `router_r1.cfg`)
- [ ] Use mensagens de commit claras
- [ ] Confirme o histórico com `git log --oneline`

### Missão 4 — Suba para o GitHub *(lab 5)*
- [ ] Crie um repositório vazio no GitHub chamado `lab-final-automation`
- [ ] Conecte com `git remote add origin ...`
- [ ] Envie tudo com `git push -u origin main`
- [ ] Confirme no navegador que `credenciais.env` **NÃO** está lá

### Missão 5 — Nova funcionalidade em branch *(lab 6)*
- [ ] Crie a branch `auditoria-vlan`
- [ ] No `playbook_auditoria.yml`, adicione uma nova task (pode ser fictícia, ex: checar VLANs)
- [ ] Faça commit dessa mudança **na branch**
- [ ] Volte para `main` e confirme que a mudança não está lá
- [ ] Faça o merge de `auditoria-vlan` em `main`
- [ ] Delete a branch após o merge

### Missão 6 — Resolva um conflito *(lab 6)*
- [ ] Crie duas branches a partir da `main`: `equipe-a` e `equipe-b`
- [ ] Em cada uma, edite a mesma linha do `router_r1.cfg` (ex: o hostname) com valores diferentes
- [ ] Faça merge das duas na `main`, gerando um conflito de propósito
- [ ] Resolva o conflito manualmente e finalize o commit de merge
- [ ] Suba tudo para o GitHub (`git push`)

### Missão 7 — Simule um colega *(lab 5)*
- [ ] Em outra pasta, clone o repositório (`git clone`)
- [ ] Confirme que todo o histórico (`git log`) veio junto
- [ ] Edite o `docs/topologia.md` nessa pasta "do colega", commit e `push`
- [ ] Volte para sua pasta original e rode `git pull` para receber a mudança

---

## 🏆 Critérios de conclusão

Você completou o Lab Final se conseguir responder "sim" para tudo:

- [ ] O repositório está no GitHub, com histórico de commits organizado
- [ ] `credenciais.env` nunca apareceu no repositório remoto
- [ ] Existe pelo menos um merge de branch sem conflito
- [ ] Existe pelo menos um merge de branch **com** conflito resolvido manualmente
- [ ] Você testou `clone`, `push` e `pull` em um cenário de "dois colaboradores"

---

## 🎓 Por que isso conecta com o CCNA Automation

Esse fluxo — versionar inventários, playbooks e configs, proteger credenciais, trabalhar em branches paralelas e resolver conflitos — é exatamente o dia a dia de quem automatiza redes com Ansible/Python em equipe. Dominar isso é tão importante quanto saber escrever o playbook em si.

**Parabéns por chegar até aqui! 🎉**
