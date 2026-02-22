#escrever um programa que calcule o preço a pagar pela energia eletrica.  pergunte a quantidade de kWh consumida e o tipo de instalaçao. R para residensias e I para industrial, C para comercial.(calcular pela tabela do livro)
kWh = float(input('Quantos Kwh vc consumiu esse mês?'))
tipo = input('Qual o seu tipo de intalação [R/I/C], R para residencias e I para industrial, C para comercial').upper().strip()
if kWh <= 500 and  tipo == 'R':
    conta = kWh * 0.40
    print(f'Sua conta de luz deu {conta}')
elif kWh > 500 and tipo == 'R':
    conta = kWh * 0.65
    print(f'Sua conta de luz deu {conta}')
elif kWh <= 1000 and  tipo == 'C':
    conta = kWh * 0.55
    print(f'Sua conta de luz deu {conta}')
elif kWh > 1000 and tipo == 'C':
    conta = kWh * 0.60
    print(f'Sua conta de luz deu {conta}')
elif kWh  <= 5000 and tipo == 'I':
    conta = kWh * 0.55
    print(f'Sua conta de luz deu {conta}')
elif kWh > 5000 and tipo == 'I':
    conta = kWh * 0.60
    print(f'Sua conta de luz deu {conta}')