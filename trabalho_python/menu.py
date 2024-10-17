# Faz a importação dos arquivos que serão utilizados
# No primeiro import, está importando a lista de carros já pronta (estática)
# E no segundo está sendo importada a classe de Carro, que é o molde para 
# as instâncias de Carro
from importcarros import lista_carros
from carro import Carro

# Declaração de variáveis
# Declara duas listas para guardar os veículos comprados e vendidos
carrosComprados = []
carrosVendidos = []

# Passa por cada carro na lista de carros e mostra o nome na tela
def mostrarCarros(lista):
    for carro in lista:
        print(carro) 

def somaValores(listaCarros):
    valorFinal = 0.0
    for carro in listaCarros:
        valorFinal += float(carro.valor)
    return valorFinal


def mostrarCarrosCompleto(listaCarros):
    for index, carro in enumerate(listaCarros, start=1):
        print(f"{index} - {carro.info()}")

# Função que representa a escolha 1 do menu
# O valor do carro é perguntado para o usuário 
def escolhaUm(listaCarros):
    mostrarCarrosCompleto(listaCarros)
    enunciado = "Qual veiculo sera vendido? "
    escolha = int(input(enunciado))
    veiculo = lista_carros[escolha - 1]
    carrosVendidos.append(veiculo)
    print("Voce vendeu {}".format(veiculo.info()))

def escolhaDois():
    veiculo = str(input("Qual veiculo voce ira comprar? "))
    valor = float(input("Qual valor do veiculo? "))
    carrosComprados.append(veiculo)
    print("Voce vendeu {} por R$ {:.2f}".format(veiculo, valor))

def escolhaTres():
    print("Carros comprados")
    mostrarCarros(carrosComprados)

def escolhaQuatro():
    print("Carros vendidos")
    mostrarCarrosCompleto(carrosVendidos)
    valorVendido = somaValores(carrosVendidos)
    print("Total valor vendido: {}".format(valorVendido))


menu = """
1 - Vender carro da loja
2 - Comprar carro de cliente
3 - Mostrar carros comprados
4 - Mostrar carros vendidos
Escolha: """

while(True):
    escolha = str(input(menu))
    if escolha == "1":
        escolhaUm(lista_carros)
    elif escolha == "2":
        escolhaDois()
    elif escolha == "3":
        escolhaTres()
    else:
        escolhaQuatro()


