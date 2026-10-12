
import socket
import os
import subprocess
from datetime import datetime


def porta_valida(porta):
    return isinstance(porta, int) and 1 <= porta <= 65535

def registrar_log(mensagem):
    caminho = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "portscan.log"
    )

    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{horario}] {mensagem}\n")

    print(f"[LOG] Registro salvo: {mensagem}")

def mostrar_ip_local():
    print("\n---- Consulta de IP local ----")

    try:
        nome = socket.gethostname()
        ip = socket.gethostbyname(nome)

        print("Nome do computador:", nome)
        print("IP local:", ip)
        registrar_log(f"Consulta de IP local: {ip}")

    except OSError as erro:
        print("Erro ao consultar IP:", erro)
        registrar_log(f"Erro na consulta de IP: {erro}")

def mostrar_configuracao_rede():
    print("\n---- Configuração de rede ----")

    try:
        resultado = subprocess.run(
            ["ipconfig"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"
        )

        print(resultado.stdout)
        registrar_log("Configuração de rede consultada")

    except OSError as erro:
        print("Erro ao consultar a rede:", erro)
        registrar_log(f"Erro na configuração de rede: {erro}")

def verificar_porta():
    print("\n---- Verificador de portas TCP ----")

    host = input("Digite o host ou IP: ").strip()

    try:
        porta = int(input("Digite a porta TCP: ").strip())

        if not porta_valida(porta):
            print("A porta deve estar entre 1 e 65535.")
            return

    except ValueError:
        print("Digite um número de porta válido.")
        return

    try:
        with socket.create_connection((host, porta), timeout=3):
            print(f"\n[ABERTA] A porta {porta} está acessível em {host}.")
            registrar_log(f"Porta TCP acessível: {host}:{porta}")

    except socket.timeout:
        print(f"\n[TEMPO ESGOTADO] {host}:{porta}")
        registrar_log(f"Tempo esgotado: {host}:{porta}")

    except OSError as erro:
        print(f"\n[SEM CONEXÃO] {erro}")
        registrar_log(f"Falha de conexão TCP: {host}:{porta} - {erro}")

def consultar_host():

    print("\n---- Consulta de host ----")

    host = input("Digite um domínio ou IP: ").strip()

    if not host:
        print("Você precisa informar um domínio ou IP.")
        return

    try:
        ip = socket.gethostbyname(host)

        print("\nHost informado:", host)
        print("Endereço IP resolvido:", ip)

        registrar_log(f"Consulta de host: {host} -> {ip}")

    except socket.gaierror:
        print("\nNão foi possível resolver o domínio ou endereço informado.")
        registrar_log(f"Falha ao resolver host: {host}")

