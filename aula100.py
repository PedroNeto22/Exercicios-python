#746.824.890-70

cpf_usuario = input('Digite um cpf: ')

if ('.' in cpf_usuario) and ('-' in cpf_usuario):
    cpf_cru = f'{cpf_usuario[:3]}{cpf_usuario[4:7]}{cpf_usuario[8:11]}{cpf_usuario[12:]}'
else:
    cpf_cru = cpf_usuario

cpf_nove_primeiros_digitos = cpf_cru[:9]

multiplicador_1 = 10
soma_1 = 0

for i in range(0,len(cpf_cru)-2):
    soma_1 += int(cpf_cru[i])*multiplicador_1
    multiplicador_1 -= 1

digito_1 = (soma_1*10)%11

digito_1 = 0 if digito_1 > 9 else digito_1


multiplicador_2 = 11
soma_2 = 0

for i in range(0,len(cpf_cru)-1):
    soma_2 += int(cpf_cru[i])*multiplicador_2
    multiplicador_2 -= 1

digito_2 = (soma_2*10)%11

digito_2 = 0 if digito_2 > 9 else digito_2

cpf_gerado = f'{cpf_nove_primeiros_digitos}{digito_1}{digito_2}'

if cpf_gerado == cpf_cru:
    print(f'{cpf_usuario} é valido')
else:
    print('CPF invalido')

