name = input('Digite seu nome ')
age = input('Digite sua idade ')

if name and age:
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {name[::-1]}')
    print(f'Seu nome tem {len(name)} letras')
    if ' ' in name:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')
    print(f'A primeira letra do seu nome é {name[0]}')
    print(f'A ultima letra do seu nome é {name[len(name)-1]}')
else:
    print('Desculpe, você deixou compos vazios')
