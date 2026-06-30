# Topologia do Laboratório

```
        +--------+          +--------+
        |   R1   |----------|  SW1   |
        +--------+          +--------+
        192.168.10.1        192.168.10.11
```

## Dispositivos

| Nome | Tipo | IP de Gerência |
|---|---|---|
| R1 | Router | 192.168.10.1 |
| SW1 | Switch | 192.168.10.11 |

## Objetivo do laboratório

Demonstrar backup automatizado de configurações via Ansible, com versionamento de todo o histórico de mudanças usando Git.
