def analisar_energia(nivel_energia):
    
    if nivel_energia <= 8000:
        return "Inseto!"
    else:
        return "Mais de 8000!"

numero_de_testes = int(input(""))

for _ in range(numero_de_testes):
    nivel = int(input(""))
    resultado = analisar_energia(nivel)
    print(resultado)