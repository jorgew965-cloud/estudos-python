#escrever um programa que pergunte o salario do funcionario e calcular o valor do aumento, para salarios superiores a R$1.250 calcular  um aumento de 10%. para inferiores ou iguais de 15 %
salario = float(input("Qual o seu salario"))
if salario > 1250:
    aumento = salario * 0.10
    print('Seu aumento so salario é {}'.format(aumento))
if salario <= 1250:
    aumento = salario * 0.15
    print(f'seu aumento do salario e {aumento}')