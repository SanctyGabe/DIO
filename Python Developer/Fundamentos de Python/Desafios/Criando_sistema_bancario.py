menu = '''
    ========== Bem vindo ==========

        Por favor selecione um 
        de nossos serviços

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

    ================================
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0

LIMITE_DE_SAQUES = 3

while True:
    print(menu)
    opcao = input()
    if opcao == "1":
        valor = float(input("Informe um valor a ser depositado: "))
        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} feito com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido, por favor tente novamente.")

    elif opcao == "2":
        valor = float(input("Informe um valor a ser sacado: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para saque.")

    elif opcao == "3":
        print("========== Extrato ==========")
        print(f"O seu saldo é de: R${saldo:.2f}")
        print(f"Foram feitos {numero_saques} saques.")
        print(extrato) 
        print("=============================")
        
    elif opcao == "0":
        print("Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")