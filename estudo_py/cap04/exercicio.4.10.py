resposta = 0
# perguntar 2 numeros e a operação a ser realizada
a = float(input(' Diga 1 numero'))
b = float(input(' Diga o 2 numero'))
operação = input('Qual operação vc quer realizar [+,/,* ,-] ').strip()
if operação ==  '*':
    resposta = (a * b)
elif operação =='/':
    resposta = (a/b)
elif operação == '+':
    resposta =  (a  + b)
elif operação == '-':
    resposta = (a-b)
else:
    print('Operação invalida')
    resposta = 0
print('a resposta deu {}'.format(resposta))