#Programa que leia 3 números e imprima o maior e menor
a= int(input('Diga um numero'))
b =int(input('Diga um numero'))
c = int(input(' Diga um numero'))
maior = a
if b > a and b > c:
    maior = b
if c > a and c >= b:
    maior = c
menor = a
if b < c and  b < a:
    menor = b
if c <= b and  b < a:
    menor = c
print('O maior numero foi {}'.format(maior))
print(' O menos numero foi {}'.format(menor))

