# Scan_System

Ferramenta de diagnóstico de computadores e redes desenvolvida em Python, com foco em aprendizado de programação, suporte técnico e fundamentos de redes.

## Funcionalidades

- **Informações do computador:** consulta do sistema operacional, arquitetura e processador.
- **Teste de conectividade:** verifica a comunicação com um endereço externo.
- **Calculadora:** operações matemáticas básicas.
- **Informações de rede:** consulta da configuração de rede.
- **Teste de ping:** verifica a resposta de um host.
- **Diagnóstico do sistema:** coleta informações básicas do ambiente.
- **Consulta de IP local:** identifica o nome do computador e resolve seu endereço IP.
- **Configuração de rede:** exibe informações retornadas pelo `ipconfig`.
- **Sistema de logs:** registra eventos e operações realizadas.
- **Relatório de diagnóstico:** gera um relatório de texto.
- **Verificador de portas TCP:** testa a conexão com uma porta de um host informado.
- **Consulta de host:** tenta resolver um domínio ou endereço para um IP.
- **Testes automatizados:** valida regras de entrada para portas TCP.

## Tecnologias utilizadas

- Python 3
- `socket`
- `platform`
- `subprocess`
- `unittest`

## Requisitos

- Python 3 instalado.
- Windows recomendado para as funções que utilizam `ipconfig` e `ping -n`.
- Conexão com a internet para testes externos de conectividade.

## Como executar

1. Clone ou baixe este repositório.
2. Abra a pasta do projeto no terminal.
3. Execute o programa principal:

   ```bash
   python main.py
   ```

4. Escolha uma opção no menu interativo.

## Executar os testes

Na pasta do projeto, execute:

```bash
python -m unittest -v test_network.py
```

## Estrutura do projeto

```text
Scan_System/
├── main.py
├── network.py
├── system.py
├── test_network.py
├── README.md
└── portscan.log
```

Os arquivos presentes podem variar conforme a evolução do projeto. O arquivo de log é gerado durante a execução.

## Segurança e limitações

- Utilize os testes de rede somente em sistemas próprios ou com autorização.
- Uma conexão TCP bem-sucedida indica que a porta está acessível a partir do ambiente de teste; não comprova a segurança do serviço.
- Uma falha de conexão não significa necessariamente que a porta esteja fechada.
- Os resultados dependem da rede, das regras de firewall e da disponibilidade do destino.

## Objetivo educacional

Projeto desenvolvido para praticar Python, modularização, diagnóstico de rede, tratamento de erros, manipulação de arquivos e testes automatizados.

## Como executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/01Stx/Scan_System.git
   ```

2. Entre na pasta do projeto:

   ```bash
   cd Scan_System
   ```

3. Execute o arquivo principal do projeto:

   ```bash
   python Scan_System.py
   ```
## Melhorias futuras

- Interface gráfica com Tkinter.
- Melhor tratamento de erros e validação de entradas.
- Separação dos módulos de diagnóstico e logs.
- Relatórios mais completos.
- Mais testes automatizados.

## Autor

Estudante de Técnico em Informática, com interesse em suporte técnico, redes de computadores, Python e segurança da informação.



