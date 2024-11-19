# --------------------CONHECENDO MÉTODOS UTEIS DA CLASSE STRING--------------------!

# PRINCIPAIS METODOS UTEIS--------------------!

#curso = "pYtHon"

#print (curso.upper()) -> Tudo em maiusculo
#print (curso.lower()) -> Tudo em minusculo
#print (curso.title()) -> Deixando somente o primeiro em maiusculo

#curso = "  Python "

#print (curso.strip()) -> Tira qualquer espaço existente 
#print (curso.lstrip()) -> Tira o espaço da esquerda
#print (curso.rstrip()) -> Tira o espaço da direita

#curso = "Python"

#print (curso.center(10,"#")) >>> "##Python##" ->
#print (".". join (curso)) >>> "P.y.t.h.o.n" -> Comum em listas

#EXEMPLO_1:

#nome = "Gabriel"

#print (nome.upper())
#print (nome.lower())
#print (nome.title())

#EXEMPLO_2:

#texto = "   Boa noite    "

#print (texto.strip() + "!")
#print (texto.lstrip() + "!")
#print (texto.rstrip() + "!")

#EXEMPLO_3

#menu = "Python"

#print(menu.center(16,"_"))
#print ("_". join (menu))

# --------------------INTEPOLAÇÃO DE VARIAVEIS--------------------!
# %-> não é mais recomendada devido a complexidade--------------------!

#EXEMPLO:

#nome = "Gabriel"
#idade = 26
#profissao = "dev"
#linguagem = "Python"

#indice 

#dados = {nome, idade, profissao, linguagem}

#print ("Olá me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))


#Metodo format -> antigo porem menos complexo utulizando "{}"--------------------!

#EXEMPLO_02:

#primeira forma
#print ("Olá me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

#segunda forma
#print ("Olá me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

#terceira forma
#print ("Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(nome = nome, idade = idade, profissao = profissao, linguagem = linguagem))

#quarta forma -> utiliza=se de um index.
#print ("Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa)

# f-string --------------------!
# passa o ponto da variavel

# --------------------FATIAMENTO DE STINGS--------------------!
# Como o nome diz cortar a string em um caracter

#EXEMPLO_01:

#nome = "Gabriel Cecilio"

#print(nome[0])
#print(nome[:7])
#print(nome[8:])
#print(nome[:8])
#print(nome[8:16])
#print(nome[8:16:2])
#print(nome[:])
#print(nome[::-1])


# --------------------STRING DE MULTIPLAS LINHAS--------------------!
# Atribuirda utilizando """

nome = "Gabriel"

mensagem = f"""
Oi meu nome é {nome}
Eu só queria umas pamonhas
e uns beijo da maldita
"""
print(mensagem)

print(f'''
    ============ MENU ============

      1 - Depositar
      2 - Sacar
      0 - Sair
      
    ==============================
      
    Obrigado por entrar em contato!
      
      ''')