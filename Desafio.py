menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDepósito de R$ {valor:.2f} Realizado com Sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")                
    elif opcao == "2":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação Falhou! O valor de saque excede o limite.")   
        elif excedeu_saques:
            print("Operação Falhou! Número máximo de saques excedido.") 
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
            print(f"\nSaque de R$ {valor:.2f} Realizado com Sucesso!")
        else:
            print("Operação Falhou! O valor informado é inválido.")            
    elif opcao == "3":
        print("\n================== EXTRATO ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$: {saldo:.2f}")
        print("==============================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por faovr selecione novamente a opreção desejada.")
