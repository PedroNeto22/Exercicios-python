import os

palavra_oculta = 'python'
letras_acertadas = ''
tentativas = 0 
while True:
    tentativas += 1
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue
    if letra in palavra_oculta:
        letras_acertadas += letra
    
    palavra_formada = ''

    for letra_secreta in palavra_oculta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_oculta:
        os.system('clear')
        print('PARABÉNS VOCÊ GANHOU')
        print(f'Numero de tentativas: {tentativas}')
        print(f'A palavra era "{palavra_oculta}"')
        letras_acertadas = ''
        tentativas = 0 
        
        


        