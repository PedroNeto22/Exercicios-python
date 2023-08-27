hour = input('Diga uma hora ')
hour_int = None

try:
    hour_int = int(hour) 
    if hour_int <= 11:
        print('Bom Dia!')
    elif hour_int <= 17:
        print('Bom Tarde!')
    else:
        print('Boa Noite')
except:
    print('Digite apenas números inteiros')



