"""
Script de exemplo - Backup de configurações de rede
Laboratório CCNA Automation
"""

import datetime

DISPOSITIVOS = ["SW1", "R1"]


def fazer_backup(dispositivo: str) -> str:
    """Simula o backup da configuração de um dispositivo de rede."""
    data = datetime.date.today().isoformat()
    nome_arquivo = f"{dispositivo}_backup_{data}.cfg"
    print(f"Backup de {dispositivo} salvo em {nome_arquivo}")
    return nome_arquivo


if __name__ == "__main__":
    for dispositivo in DISPOSITIVOS:
        fazer_backup(dispositivo)
