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
            acao = input("1 - Ver saldo. \n"
                        "2 - Depositar. \n"
                        "3 - Sacar Dinheiro.\n"
                        "4 - Ver Historico de transação.\n"
                        "5 - Sair.\n"
                        "Escolha: ")
            if acao == "1":
                print(f"O seu saldo é R$: {saldo}")
            elif acao == "2":
                deposito = int(input("Valor a ser depositado: R$ "))
                if deposito < 0:
                    print("Valor negado!")
                    continue
                saldo += deposito
                historico_deposito.append(deposito)
                print(f"Saldo depositado a sua conta bancaria e seu saldo atualizou para {saldo}.")
            elif acao == "3":
                saque = int(input("Digite o valor do saque: R$ "))
                if saque < 0:
                    print("Valor negado!")
                    continue
                if saque <= saldo:
                    saldo -= saque
                    historico_saque.append(saque)
                    print(f"saque realizado com sucesso! o saldo atualizou para R${saldo}")
                else:
                    print("Saldo insuficiente para saque!")
            elif acao == "4":
                print("\n--- HISTÓRICO ---")
                print("Depositos:", historico_deposito)
                print("Saques:", historico_saque)
            elif acao == "5":
                print("Encerrando o programa...")
                break
            break
    else:   
        tentativas += 1
        print(f"Tente novamente! Tentativas restantes: {3 - tentativas}")

if tentativas == 3:
    print("Conta bloqueada!")
