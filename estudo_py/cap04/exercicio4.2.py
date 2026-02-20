velocidade = float(input(' Qual a velocidade do seu carro?'))
if velocidade > 80:
    multa = (velocidade - 80) -5 
    print(' Vc levou multa de R${}'.format(multa))
    