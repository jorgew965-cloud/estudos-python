# 3 medias, materia 1 , materia 2, materia 3 , pra passar nota >= 7
materia1 = float(input('Digite a nota 1 da sua materia 1'))
materia2 = float(input('Digite a nota 2 da sua materia 2'))
materia3 = float(input('Digite a nota 3 da sua materia 3'))
media = (materia1 + materia2 + materia3 ) /3
if media >= 7:
    print(f' Parabens vc passou e sua media foi {media}')
else:
    print(f' Infelizmente vc n passou porque sua media foi {media}')
