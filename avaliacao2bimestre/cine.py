NUM_SEATS = 30
seats = [False] * NUM_SEATS

while True:
    print("\nSistema de Reserva de Assentos do Cinema")
    print("1 - Reservar assento")
    print("2 - Cancelar reserva")
    print("3 - Exibir assentos")
    print("4 - Encerrar sistema")

    opcao_menu = input("\nEscolha uma opção: ")

    if opcao_menu == '1':
        try:
            assento_escolhido = int(input("Digite o número do assento a reservar (1 a 30): "))
            indice_assento = assento_escolhido - 1
            
            if 0 <= indice_assento < NUM_SEATS:
                if not seats[indice_assento]: 
                    seats[indice_assento] = True  
                    print(f"Assento {assento_escolhido} reservado!")
                else:
                    print(f"O assento {assento_escolhido} já está ocupado.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    elif opcao_menu == '2':
        try:
            assento_escolhido = int(input("Digite o número do assento a cancelar (1 a 30): "))
            indice_assento = assento_escolhido - 1

            if 0 <= indice_assento < NUM_SEATS:
                if seats[indice_assento]:  
                    seats[indice_assento] = False  
                    print(f"Reserva do assento {assento_escolhido} cancelada.")
                else:
                    print(f"O assento {assento_escolhido} já está livre.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    elif opcao_menu == '3':
        print("\n--- Status dos Assentos ---")
        total_livres = 0
        total_ocupados = 0
        lista_assentos_ocupados = "" 
        for i in range(NUM_SEATS):
            if seats[i]: 
                total_ocupados += 1
                
                if lista_assentos_ocupados != "":
                    lista_assentos_ocupados += ", "
                lista_assentos_ocupados += str(i + 1)
            else: 
                total_livres += 1
        
        print(f"Total de assentos livres: {total_livres}")
        print(f"Total de assentos ocupados: {total_ocupados}")
        
        if lista_assentos_ocupados: 
            print(f"Lista dos assentos ocupados: [{lista_assentos_ocupados}]")
        else:
            print("Nenhum está assento ocupado.")

    elif opcao_menu == '4':
        print("Até mais!")
        break 
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")