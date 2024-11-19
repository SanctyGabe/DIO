# --------------------IDENTAÇÃO DE BOLOCOS--------------------!
# MELHORANDO A LEGIBILIDADE DO CODIGO
# APERTE TAB OU 4* ESPAÇO PRA SEPARAR OS BLOCOS

#def sacar(valor):
#    saldo = 500

#    if saldo >= valor:
#        print("Valor sacado!")
#        print("Retire seu cartão!")
    
#    print("Obrigado por utilizar nossos serviços!")

#def depositar(valor):
#    saldo = 500
#    saldo += valor

#    if saldo >= valor:
#        print("Valor depositado!")
#        print("Obrigado por utilizar nossos serviços!")

#sacar(100)
# --------------------ESTRUTURAS CONDICIONAIS--------------------!
# if/else/elif--------------------!
#if e else

#Exemplo:
#saldo = 2000
#saque = float(input("Informe o valor que deseja sacar: "))

#if saldo >= saque:
#    print("Valor sacado!")
#    print("Saque realizado com sucesso!")

#else:
#    print("Saldo insuficiente!")
#    print("Saque não realizado!");
#    print("Obrigado por utilizar nossos serviços!")

#elif
#opcao = int(input("informe uma opção: [1] para sacar \n[2] Extrato"))

#if opcao == 1:
#    valor = float(input("Informe o valor que deseja sacar: "))
#    sacar(valor)

#elif opcao == 2:
#    print("Extrato")

#else:
#    sys.exit("Opção inválida")

#--------------------!
#MAIOR_DE_IDADE = 18
#IDADE_ESPECIAL = 17

#idade = int(input("Informe sua idade: "))

#if idade >= MAIOR_DE_IDADE:
#    print("Você é maior de idade, pode tirar a CNH.")

#elif idade == IDADE_ESPECIAL:
#     print("No momento você só pode fazer aulas teoricas.")

#else:
#    print("Você é menor de idade, não pode tirar a CNH.")


# If aninhado --------------------!
#If aninhado = pode se ter if/else/elif dentro de uma variavel if

#Exemplo:
#conta_normal = False
#conta_universitaria = False

#saldo = 2000
#saque = 3005
#cheque_especial = 450

#if conta_normal:

#    if saldo >= saque:
#        print ("Saque realizado com sucesso!")

#    elif saque <= (saldo + cheque_especial):
#        print("Saque realizado com uso de cheque especial!")

#    else:
#        print("Saldo insuficiente!")

#elif conta_universitaria:

#    if saldo >= saque:
#        print ("Sque realizado com sucesso!")
#    else:
#        print("Saldo insuficiente!")
#else:
#    print("O sistema não reconheceu o tipo de conta. Entre em contato com o banco.")

# If ternario --------------------!
#If ternario = mesma linha -> retorno exp logica = true, exp logica, retorno caso invalido
#Utilizado para verificação simples

#Exemplo:

#saldo = 2000
#saque = 500

#status = "Sucesso" if saldo >= saque else "falha"

#print(f"{status} ao realizar o saque!")

# --------------------ESTRUTURAS DE REPETIÇÃO--------------------!
#For e while

#for--------------------!

#Exemplo sem repetição:

#a = int(input("Informe um numero inteiro: "))
#print(a)

#a += 1
#print(a)

#a += 1
#print(a)

#For -> bom saber o numero maximo de vezes que será repetido

#Exemplo:
#texto = input ("Digite um texto ")
#VOGAIS = "AEIOU"

#for letra in texto:
#    if letra.upper() in VOGAIS:
#        print(letra, end="")
#print()

#for/else--------------------!

#Exemplo:

#texto = input ("Digite um texto ")
#VOGAIS = "AEIOU"

#for letra in texto:
#    if letra.upper() in VOGAIS:
#        print(letra, end="")
#else:
#    print()


#Range --------------------!

#Range -> Produzir uma sequencia apartir de inicio (inclusivo) para um fim (exclusivo)
# range(stop) -> range object
# range(start, stop[, step]) -> range object

#Exemplo:

#for numero in range(0, 51, 5):
#    print(numero, end=" ")

#While --------------------!

#While -> utilizar quando não se sabe o numero de vezes que o codigo deve ser executado.

#Exemplo: 
#opcao = -1
#while opcao != 0:
#    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] sair \n: "))

#    if opcao == 1:
#        print("Sacando...")
   
#    elif opcao == 2:
#        print("Exibindo extrato...")
#   
#    else:
#        print("Saindo...")
#        print("Agradecemos por utilizar nossos serviços")

#print()

#Break --------------------!

while True:
    numero = int(input("Informe um numero: "))

    if numero >= 10:
        break
    print(numero)
