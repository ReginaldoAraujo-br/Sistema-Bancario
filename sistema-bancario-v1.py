# Sistema Bancário v1

# Função principal do menu
def menu_bancario():
    saldo_atual = 0
    saldo_anterior = 0
    contador_de_saque = 0
    maximo_de_saques = 3
    extrato = []

    while True:
        operacao_escolhida = int(input("\nDigite uma operação: \n[1] - Depósito \n[2] - Saque \n[3] - Extrato \n[0] - Sair \n\n"))

        if operacao_escolhida == 1: # DEPOSITO
            valor = float(input("\nDigite o valor do depósito: "))
            if valor > 0:
                saldo_atual += valor
                extrato=(f"Depósito: R$ {valor:.2f}")
                print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("\nValor inválido.")
        elif operacao_escolhida == 2: # SAQUES
            if contador_de_saque < maximo_de_saques:
                valor = float(input("Digite o valor do saque: "))
                if valor <= saldo_atual:
                    saldo_atual -= valor
                    extrato.append(f"\nSaque: -{valor:.2f}")
                    contador_de_saque += 1
                    print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.")
                    print(f"Seu novo saldo é de R$ {saldo_atual:.2f}")
                else:
                    print("\nSaldo insuficiente.")
            else:
                print("\nNúmero máximo de saques atingido.")
        elif operacao_escolhida == 3: # EXTRATO
            print("\n======================EXTRATO======================\n")
            print("Não foram realizadas movimentações."if not extrato else extrato)
            print(f"\nSaldo atual: R$ {saldo_atual:.2f}")
        elif operacao_escolhida == 0:
            break
        else:
            print("\nOperação inválida. Tente novamente.")

# Executar o menu bancário
menu_bancario()