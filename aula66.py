option = True

result_str = ''

while option:
    calc = input('Voce quer fazer alguma conta? ')
    if calc == 'Sim' or calc == 's' or calc == 'sim':
        print('As únicas operações possíveis sao de + - / * ')
        number1 = float(input('Informe um Numero: '))
        number2 = float(input('Informe outro numero: '))
        operator = input('Informe um operador: ')
        if len(operator) > 1:
            print('Digite apenas um operador')
            continue
        if operator == '+':
            result = number1 + number2
            result_str = f'{number1} {operator} {number2} = {result}'
            print(result_str)
        elif operator == '-':
            result = number1 - number2
            result_str = f'{number1} {operator} {number2} = {result}'
            print(result_str)
        elif operator == '/':
            result = number1 / number2
            result_str = f'{number1} {operator} {number2} = {result}'
            print(result_str)
        elif operator == '*':
            result = number1 * number2
            result_str = f'{number1} {operator} {number2} = {result}'
            print(result_str)
        else:
            print('Isso não é um operador valido')
    elif calc == 'Não' or calc == 'n' or calc == 'nao':
        print('Você escolheu sair')
        option = False

        
        