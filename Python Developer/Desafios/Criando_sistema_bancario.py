import textwrap


def menu():
    menu = """\n
    ========== Bem vindo ==========

        Por favor selecione um 
        de nossos serviços

    [nc]\tNovaconta
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [lc]\tListar contas
    [nu]\tNovo usuarío
    [q]\t Sair
   
    ================================
    => """
    return imput(textwrap.dedent(menu))
   

def depositar(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor 
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} feito com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

        return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_de_saques, limite_de_saques):
            excedeu_saldo = valor > saldo
            execedeu_limite = valor > limite
            execedeu_saques = numero_de_saques >= limite_de_saques
        
            if excedeu_saldo:
            print("\n Operação falhou. Saldo insufieciente.")
        
            elif execedeu_limite:
            print("\n Operação falhou! Limite execedido")
        
            elif execedeu_saques:
            print("\n Operação falhou! Limite de saques execedido.")
        
            elif valor >0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
            print("\n Valor sacado com sucesso!")
        
            else:
            print("\n Operação falou! Valor informado invalido.")

        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
        print("========== Extrato ==========")
        print("Ainda não foram realizadas nenhuma movimentação em sua conta" if not extrato else extrato)
        print(f"\nSaldo:\t\tR$ {saldo:2f}")
        print("=============================")

def criar_usario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n CPF já cadastrado")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cof, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuario):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None   
       
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuario não encontrado, fluxo de conta encerrado!")

    def listar_contas(contas)
        for conta in contas:
            linha = f"""z
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titualar:\t{conta['usuario']["nome"]}
            """
            print("=" * 100)
            print(textwarp.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

          if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()