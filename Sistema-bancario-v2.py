
from datetime import datetime 
# Sistema Bancário v2
# Função principal do menu
def menu_bancario():
    saldo_atual = 0
    contador_de_saque = 0
    maximo_de_saques = 3
    transacoes = 10
    dia_e_hora = datetime.now()
    extrato = []

    while True:
        operacao_escolhida = int(input("\nDigite uma operação: \n[1] - Depósito \n[2] - Saque \n[3] - Extrato \n[0] - Sair \n\n"))

        if operacao_escolhida == 1: # DEPOSITO
            if transacoes == 0:
                print("\nNúmero máximo de transações atingido.")
            else:
                valor_deposito = float(input("\nDigite o valor do depósito: "))
                if valor_deposito > 0:
                    saldo_atual += valor_deposito
                    dia_e_hora_transacao = dia_e_hora.strftime('%d/%m/%Y %H:%M:%S')
                    extrato.append(f"Depósito: R$ {valor_deposito:.2f} - {dia_e_hora_transacao}")
                    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso em {dia_e_hora_transacao}.")
                    transacoes -= 1
                    print(f"Transações restantes: {transacoes}")
                    dia_e_hora = datetime.now()
                else:
                    print("\nValor inválido.")
        elif operacao_escolhida == 2: # SAQUES
            if transacoes == 0:
                print("\nNúmero máximo de transações atingido.")
            else:
                if contador_de_saque < maximo_de_saques:
                    valor_saque = float(input("Digite o valor do saque: "))
                    if valor_saque <= saldo_atual:
                        saldo_atual -= valor_saque
                        dia_e_hora_transacao = dia_e_hora.strftime('%d/%m/%Y %H:%M:%S')
                        extrato.append(f"Saque: R$ str({valor_saque:.2f}) - {dia_e_hora_transacao}")
                        contador_de_saque += 1
                        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso em {dia_e_hora_transacao}.")
                        print(f"Seu novo saldo é de R$ {saldo_atual:.2f}")
                        transacoes -= 1
                        print(f"Transações restantes: {transacoes}")
                        dia_e_hora = datetime.now()
                    else:
                        print("\nSaldo insuficiente.")

        elif operacao_escolhida == 3: # EXTRATO
            if transacoes == 0:
                print("\nNúmero máximo de transações atingido.")
            else:
                print("\n======================EXTRATO======================\n")
            dia_e_hora_transacao = dia_e_hora.strftime('%d/%m/%Y %H:%M:%S')
            print(f"Não foram realizadas movimentações em {dia_e_hora_transacao}." if not extrato else "\n".join(extrato))
            print(f"\nSaldo atual: R$ {saldo_atual:.2f} em {dia_e_hora_transacao}")
            transacoes -= 1
            print(f"Transações restantes: {transacoes}")
            dia_e_hora = datetime.now()
        elif operacao_escolhida == 0:
            break
        else:
            print("\nOperação inválida. Tente novamente.")

# Executar o menu bancário
menu_bancario()