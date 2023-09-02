#746.824.890-70

cpf = input('Digite um cpf: ')

cpf_separado = cpf.split('-')

cpf_primeiros_numeros = cpf_separado[0].split('.')

multiplicador = 10
soma = 0

for i in range(0,(len(cpf_primeiros_numeros))):
    for j in range(0,(len(cpf_primeiros_numeros))):
        soma += int(cpf_primeiros_numeros[i][j]) * multiplicador
        multiplicador-= 1
        
resultado = (soma*10)%11

print(resultado)

resultado = 0 if resultado > 9 else resultado

print(resultado)



