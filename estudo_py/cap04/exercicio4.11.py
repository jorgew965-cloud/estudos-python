valor_casa = float(input("Qual o valor da casa que você quer comprar?"))
salario = float(input(" Qual o seu salario?"))
anos = float(input(" Em quatos anos quer pagar sua casa?"))
calculador_meses = ( anos * 12)
calcular_prestação = ( valor_casa/ calculador_meses)
calcular_limite = (salario * 0.3)
if calcular_limite >= calcular_prestação:
    print("Parabens, o banco liberou o emprestimo")
elif calcular_prestação > calcular_limite:
    print("Infelizmente o banco não liberou ")
