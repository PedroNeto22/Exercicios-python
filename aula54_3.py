name = input('Digite seu nome ')

length_name = len(name)

if length_name > 1:
    if length_name <= 4:
        print('Seu nome é curto')
    elif length_name <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')
