class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def __del__(self):
        print("Parou de buzinar...")

    def parar(self):
        print("Parando bicicleta...")

    def __del__(self):
         print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

        def acelerando():
            if correr > self.acelerando:
                print("Fast af boiiiii...")              
            if correr < self.acelerando:
                print("Taca-lhe pau neste carrinho, Marcos")
            else:
                print("Poker face")
            
        # end def
    def __del__(self):
         print("Quase bateu...melhor parar agora")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
