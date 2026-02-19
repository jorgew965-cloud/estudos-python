mercadoria = float(input(' Qual o preço da mercadoria'))
desconto = float(input(' Qual o percentual de desconto'))
total = mercadoria * (desconto/100)
preço = mercadoria - total
print(f' O total deu {preço:.2f}')
