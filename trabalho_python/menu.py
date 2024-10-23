# Faz a importação dos arquivos que serão utilizados
# No primeiro import, está importando a lista de carros já pronta (estática)
# E no segundo está sendo importada a classe de Carro, que é o molde para 
# as instâncias de Carro
from importcarros import lista_carros
from carro import Carro
import pandas as pd
import matplotlib.pyplot as plt

# Declaração de variáveis
# Declara duas listas para guardar os veículos comprados e vendidos
# Declara duas variáveis para guardar o valor do total de carros vendidos
# e valor total de carros comprados. Ambas iniciando com 0.0 para somar os valores
# conforme os carros são comprados e vendidos
carrosComprados = []
carrosVendidos = []
valorCarrosComprados = 0.0
valorCarrosVendidos = 0.0

# Passa por cada carro na lista de carros e mostra o nome na tela
# def é a palavra reservada usada para declarar uma função
# def = definition ou definição
# função é um agrupamento de código com determinada funcionalidade
# for é a palavra reservada para fazer um loop em uma lista
# lista é um parâmetro recebido pela função.
# Quem chama a função fica responsável por enviar a lista
def mostrarCarros(lista):
    for carro in lista:
        print(carro) 

# Nessa função é feito um loop em uma lista de carros
# Em cada iteração (giro) desse loop o valor do carro é somado a outra variável
# Os valores dos carros são somados a uma variável chamado valorFinal com +=
# Usar += é o mesmo que fazer o seguinte: valorFinal = valorFinal + float(carro.valor)
# float é usado para transformar o valor do carro no tipo numero com virgula (decimal)
def somaValores(listaCarros):
    valorFinal = 0.0
    for carro in listaCarros:
        valorFinal += float(carro.valor)
    return valorFinal

# Nessa função está sendo declarado um for com enumerate 
# o enumerate é uma função do python que permite iterar na lista trazendo o indice e o valor
def mostrarCarrosCompleto(listaCarros):
    for index, carro in enumerate(listaCarros, start=1):
        print(f"{index} - {carro.info()}")

def escolhaTres():
    print("Carros comprados:")
    mostrarCarros(carrosComprados)

def escolhaQuatro():
    global valorCarrosVendidos
    print("Carros vendidos:")
    mostrarCarrosCompleto(carrosVendidos)
    valorCarrosVendidos = somaValores(carrosVendidos)
    print("Total valor vendido: {}".format(valorCarrosVendidos))

# Função que representa a escolha 1 do menu
# O valor do carro é perguntado para o usuário 
def escolhaUm(listaCarros):
    mostrarCarrosCompleto(listaCarros)
    enunciado = "Qual veiculo sera vendido? "
    escolha = int(input(enunciado))
    veiculo = lista_carros[escolha - 1]
    carrosVendidos.append(veiculo)
    print("Voce vendeu {}".format(veiculo.info()))
    escolhaQuatro()

# A sintaxe global é usado para usar a variavel global
def escolhaDois():
    global valorCarrosComprados
    veiculo = str(input("Qual veiculo voce ira comprar? "))
    valor = float(input("Qual valor do veiculo? "))
    carrosComprados.append(veiculo)
    valorCarrosComprados += valor
    print("Voce comprou {} por R$ {:.2f}".format(veiculo, valor))
    escolhaTres()

def escolhaCinco():
    global valorCarrosVendidos
    global valorCarrosComprados
    valorCaixa = valorCarrosVendidos - valorCarrosComprados
    dados = {
        'Descrição': ['Total Carros Vendidos', 'Total Carros Comprados', 'Caixa'],
        'Valor': [valorCarrosVendidos, valorCarrosComprados, valorCaixa]
    }
    # Cria data frame
    df = pd.DataFrame(dados)
    #mostra dados tabelados de forma simples
    print(df.to_string(index=False))
    #Cria gráfico
    plt.figure(figsize=(8, 5))
    plt.bar(df['Descrição'], df['Valor'], color=['blue', 'orange', 'green'])
    plt.title('Valores de Carros Vendidos, Comprados e Caixa')
    plt.ylabel('Valor')
    plt.grid(axis='y')
    # Mostrando o gráfico
    plt.show()

menu = """
1 - Vender carro da loja
2 - Comprar carro de cliente
3 - Mostrar carros comprados
4 - Mostrar carros vendidos
5 - Ver balanço do caixa
Escolha: """

while(True):
    escolha = str(input(menu))
    if escolha == "1":
        escolhaUm(lista_carros)
    elif escolha == "2":
        escolhaDois()
    elif escolha == "3":
        escolhaTres()
    elif escolha == "4":
        escolhaQuatro()
    else:
        escolhaCinco()


