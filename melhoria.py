usuario = "usuario1234"
senha = "senha1234"
saldo = 1000
historico_deposito = []
historico_saque = []

tentativas = 0

while tentativas < 3:
    login = input("Digite seu usuário: ")
    password = input("Digite sua senha: ")

    if login == usuario and password == senha:
        print("Acesso liberado!")

        while True:
            acao = input(
                "\n1 - Ver saldo\n"
                "2 - Depositar\n"
                "3 - Sacar dinheiro\n"
                "4 - Ver histórico de transações\n"
                "5 - Sair\n"
                "Escolha: "
            )

            if acao == "1":
                print(f"O seu saldo é R$: {saldo}")

            elif acao == "2":
                deposito = float(input("Valor a ser depositado: R$ "))
                if deposito <= 0:
                    print("Valor inválido!")
                    continue

                saldo += deposito
                historico_deposito.append(deposito)
                print(f"Depósito realizado! Saldo atual: R${saldo}")

            elif acao == "3":
                saque = float(input("Digite o valor do saque: R$ "))
                if saque <= 0:
                    print("Valor inválido!")
                    continue

                if saque <= saldo:
                    saldo -= saque
                    historico_saque.append(saque)
                    print(f"Saque realizado! Saldo atual: R${saldo}")
                else:
                    print("Saldo insuficiente!")

            elif acao == "4":
                print("\n--- HISTÓRICO ---")

                print("\nDepósitos:")
                if not historico_deposito:
                    print("Nenhum depósito realizado!")
                else:
                    for valor in historico_deposito:
                        print(f"Depósito: R${valor}")

                print("\nSaques:")
                if not historico_saque:
                    print("Nenhum saque realizado!")
                else:
                    for valor in historico_saque:
                        print(f"Saque: R${valor}")

            elif acao == "5":
                print("Encerrando o programa...")
                break

            else:
                print("Opção inválida!")

        break

    else:
        tentativas += 1
        print(f"Tente novamente! Tentativas restantes: {3 - tentativas}")

if tentativas == 3:
    print("Conta bloqueada!")
