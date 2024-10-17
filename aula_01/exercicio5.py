# Crie um programa que calcule um aumento de 15% para um salário que será digitado pelo usuário

salario = float(input("Digite seu salário? "))
aumento = 15/100 * salario
novoSalario = salario + aumento
print("Seu salário atual é {:.2f}. Seu aumento será de {:.2f} e o salário total é {:.2f}".format(
    salario, aumento, novoSalario
))