cigarros = int(input(' Quanto cigarros vc fuma por dia'))
anos = int(input(' quanto Anos vc ja fumou'))
vida =  anos * 365 * cigarros  * 10
dias =  (vida /60 ) / 24
print(f' Vc perdeu {dias:2f} dias de vida fumando cigarro ')