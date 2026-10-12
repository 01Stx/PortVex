
import os
import platform
import getpass


def diagnostico_sistema():
    print("\n===== DIAGNOSTICO DO SISTEMA =====")
    print(f"Computador: {platform.node()}")
    print(f"Usuario: {getpass.getuser()}")
    print(f"Sistema: {platform.system()}")
    print(f"Versao: {platform.version()}")
    print(f"Arquitetura: {platform.architecture()[0]}")
    print(f"Diretorio atual: {os.getcwd()}")