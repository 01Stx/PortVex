import os
import platform
import getpass


def diagnostico_sistema():
    """Exibe informações básicas do sistema operacional."""
    print("\n===== DIAGNÓSTICO DO SISTEMA =====")
    print(f"Computador: {platform.node()}")
    print(f"Usuário: {getpass.getuser()}")
    print(f"Sistema operacional: {platform.system()}")
    print(f"Versão do sistema: {platform.version()}")
    print(f"Arquitetura: {platform.architecture()[0]}")
    print(f"Diretório atual: {os.getcwd()}")
