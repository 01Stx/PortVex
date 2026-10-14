from sys import platform
from calculator import calcular
from system import diagnostico_sistema # type: ignore
from network import (
    mostrar_ip_local,
    mostrar_configuracao_rede,
    verificar_porta,
    consultar_host)
import network
print("Arquivo network carregado:", network.__file__)
print("Função registrar_log existe:", hasattr(network, "registrar_log"))
import platform
import os
import subprocess
import re 
import getpass
import socket
from datetime import datetime

os.system("cls")

def gerar_relatorio():
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    computador = platform.node()
    sistema = platform.system()
    versao = platform.version()
    arquitetura = platform.architecture()[0]

    try:
        ip_local = socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        ip_local = "Não foi possível identificar"

    print("\n---- Diagnóstico do sistema ----")
    print("Verificando conectividade...")

    resultado = os.system(
        "ping -n 1 -w 2000 8.8.8.8 > nul"
        if platform.system() == "Windows"
        else "ping -c 1 -W 2 8.8.8.8 > /dev/null 2>&1"
    )

    conexao = "Conectividade confirmada" if resultado == 0 else "Falha no teste de conectividade"

    relatorio = f"""
========================================
       PortVex - RELATÓRIO
========================================

Data e hora: {horario}
Computador: {computador}
Sistema operacional: {sistema}
Versão do sistema: {versao}
Arquitetura: {arquitetura}
IP local: {ip_local}
Conectividade: {conexao}

========================================
"""

    print(relatorio)

    caminho = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "relatorio_PortVex.txt"
    )

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(relatorio)

    print(f"Relatório salvo em: {caminho}")
    registrar_log("Relatório de diagnóstico gerado")

def testar_ping():
    print("\n===== TESTE DE PING =====")

    destino = input("Digite um IP ou dominio: ").strip()

    if not destino or not re.fullmatch(
        r"[a-zA-Z0-9.-]+", destino
    ):
        print("Endereco invalido.")
        return

    try:
        resultado = subprocess.run(
            ["ping", "-n", "4", "-w", "2000", destino],
            capture_output=True,
            text=True,
            encoding="oem",
            errors="replace",
            timeout=12
        )

        print("\n===== RESULTADO =====")
        print(resultado.stdout)

        if resultado.returncode == 0:
            print("Destino respondeu ao ping.")
        else:
            print("Nenhuma resposta valida recebida.")

    except subprocess.TimeoutExpired:
        print("O teste demorou demais e foi interrompido.")
    except OSError as erro:
        print(f"Erro ao executar o ping: {erro}")    

def informacoes_rede():
    print ("\n===== INFORMAÇÕES DE REDE =====\n")

    try:
        resultado = subprocess.run(
            ["ipconfig", "/all"],
            capture_output=True,
            text=True,
            encoding="oem",
            errors="replace"
        )

        print(resultado.stdout)
    except OSError as erro:
        print(f"Erro ao consultar rede: {erro}")

def calculadora():
    print("\n===== CALCULADORA =====")

    try:
        numero1 = float(input("Digite o primeiro número: ").replace(",", "."))
        operador = input("Digite a operação (+, -, *, /): ").strip()
        numero2 = float(input("Digite o segundo número: ").replace(",", "."))

        resultado = calcular(numero1, operador, numero2)
        print(f"\nResultado: {resultado:g}")

    except ValueError as erro:
        print(f"\nEntrada ou operação inválida: {erro}")

    except ZeroDivisionError:
        print("\nNão é possível dividir por zero!")


def registrar_log(mensagem):
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("portscan.log", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{horario}] {mensagem}\n")

def mostrar_logs():
    caminho = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 
        "portscan.log"
    )
    print("\n---- HISTÓRICO DE LOGS ----\n")

    if not os.path.exists(caminho):
        print("Nenhum arquivo de logs encontrado.")
        return

    with open(caminho, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    if not linhas:
        print("O histórico está vazio.")
        return
    print("Últimos registros:\n")
    for linha in linhas[-10:]:
        print(linha.strip())

while True:
    print("\nWelcome to PortVex!")
    print("------------------")
    print("    PortVex    ")
    print("------------------\n")

    print("[1] Informações do computador")
    print("[2] Verificar conexão")
    print("[3] Calculadora")
    print("[4] Informações de rede")
    print("[5] Testar ping")
    print("[6] Diagnóstico do sistema")
    print("[7] Consultar IP local")
    print("[8] Configuração completa de rede")
    print("[9] consultar histórico de logs")
    print("[10] Gerar relatório de diagnóstico")
    print("[11] Verificar porta TCP")
    print("[12] Consultar domínio ou IP")
    print("[13] Sair ")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
        print("\n---- Informações do computador ----")
        print("Sistema operacional:", platform.system())
        print("Versão:", platform.version())
        print("Arquitetura:", platform.architecture()[0])
        print("Processador:", platform.processor())
        print("Nome do computador:", platform.node())

        registrar_log("Informações do computador consultadas")

    elif opcao == "2":
        print("\n---- Teste de conexão ----")
        resultado = os.system("ping -n 1 8.8.8.8")

        if resultado == 0:
            print("\nInternet funcionando!")
            registrar_log("Teste de conectividade: sucesso")
        else:
            print("\nNão foi possível alcançar o endereço.")
            registrar_log("Teste de conectividade: falha")

    elif opcao == "3":
        calculadora()
        registrar_log("Calculadora utilizada")

    elif opcao == "4":
        informacoes_rede()
        registrar_log("Informações de rede consultadas")

    elif opcao == "5":
        testar_ping()
        registrar_log("Teste de ping executado")

    elif opcao == "6":
        diagnostico_sistema()
        registrar_log("Diagnóstico do sistema executado")

    elif opcao == "7":
        mostrar_ip_local()
        registrar_log("Consulta de IP local executada")

    elif opcao == "8":
        mostrar_configuracao_rede()
        registrar_log("Configuração de rede consultada")

    elif opcao == "9":
        mostrar_logs()
        registrar_log("Histórico de logs consultado")

    elif opcao == "10":
        gerar_relatorio()
        registrar_log("Relatório de diagnóstico gerado")

    elif opcao == "11":
        verificar_porta()

    elif opcao == "12":
        consultar_host()    

    elif opcao == "13":
        registrar_log("Programa encerrado")
        print("\nEncerrando o PortVex...")
        break

    else:
        print("\nOpção inválida!")
        registrar_log(f"Opção inválida informada: {opcao}")

    if opcao != "9" and opcao != "13":
        input("\nPressione Enter para voltar ao menu...")