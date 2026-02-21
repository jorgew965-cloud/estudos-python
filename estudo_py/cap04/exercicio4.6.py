#perguntar distancia em km e calcular o preço da passagem semdo 0.5 por km ate 200km e 0,45 para acima de 200
km = float(input(' Qual a distancia da sua viajem em Km'))
if km <= 200:
    passagem = km * 0.5
    print(' Sua passagem deu R${} '.format(passagem))
elif km > 200:
    passagem = km * 0.45
    print(f'Sua passagem deu R${passagem}')
    
