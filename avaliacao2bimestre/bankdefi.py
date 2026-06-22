saldo = 500.00
deposito_contagem = 0
saque_contagem = 0
rodando = True

print("Bem-vindo ao Sistema Bancário!")
print(f"Seu saldo inicial é de R$ {saldo:.2f}")

while rodando:
    print("\nMENU")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("4 - Encerrar")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            try:
                valor_deposito = float(input("Digite o valor para depósito: R$ "))
                if valor_deposito <= 0:
                    print("Erro: O valor do depósito deve ser positivo.")
                else:
                    saldo += valor_deposito
                    deposito_contagem += 1
                    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
                    print(f"Seu novo saldo é de R$ {saldo:.2f}")
            except ValueError:
                print("Erro: Valor inválido. Digite um número para o depósito.")

        elif opcao == 2:
            try:
                valor_saque = float(input("Digite o valor para saque: R$ "))
                if valor_saque <= 0:
                    print("Erro: O valor do saque deve ser positivo.")
                elif valor_saque > saldo:
                    print("Erro: Saldo insuficiente para realizar o saque.")
                    print(f"Seu saldo atual é de R$ {saldo:.2f}")
                else:
                    saldo -= valor_saque
                    saque_contagem += 1
                    print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
                    print(f"Seu novo saldo é  R$ {saldo:.2f}")
            except ValueError:
                print("Erro: Valor inválido. Digite um número para o saque.")

        elif opcao == 3:
            print(f"Seu saldo atual é de R$ {saldo:.2f}")

        elif opcao == 4:
            print("Encerrando o sistema bancário")
            rodando = False 

        else:
            print("Opção inválida. Escolha um número entre 1 e 4.")

    except ValueError:
        print("Erro: Entrada inválida. Digite um número para escolher uma opção.")

print(f"Quantidade de depósitos realizados: {deposito_contagem}")
print(f"Quantidade de saques realizados: {saque_contagem}")
print(f"Saldo final: R$ {saldo:.2f}")
