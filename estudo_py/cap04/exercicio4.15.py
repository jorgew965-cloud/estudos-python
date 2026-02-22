#reescreva o programa a seguir com if elif e else
#if hora < 12:
#    print('bom dia')
#if hora >= and hora <= 18:
#    print('Boa tarde')
#if hora >= 18:
#   print('boa noite')
horas = int(input('Que horas são?'))
if horas < 12:
    print('Bom dia')
elif horas >= 12 and horas <= 18:
    print('Boa tarde')
else:
    print('Boa noite')