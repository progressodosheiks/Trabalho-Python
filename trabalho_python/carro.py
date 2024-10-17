class Carro:
    def __init__(self, marca, modelo, ano, cor, valor):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.valor = valor

    def info(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - Cor: {self.cor} - Valor: R$ {self.valor}"