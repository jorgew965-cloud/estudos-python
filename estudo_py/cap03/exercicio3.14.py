km = float(input(' Quantos km vc vai andar com seu carro alugado'))
dias = int(input(' Quantos dias vc pretende ficar com o carro alugado'))
total = (dias * 60) + (km * 0.15  )
print(f' O total deu  R${total:2f}')