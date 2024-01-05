# 746.824.890-70
# Primeira forma que eu fiz
# cpf = input('Digite um cpf: ')

# if ('.' not in cpf) and ('-' not in cpf):
#     cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

# cpf_separado = cpf_formatado.split('-')

# cpf_primeiros_numeros = cpf_separado[0].split('.')

# multiplicador = 10
# soma = 0

# for i in range(0,(len(cpf_primeiros_numeros))):
#     for j in range(0,(len(cpf_primeiros_numeros))):
#         soma += int(cpf_primeiros_numeros[i][j]) * multiplicador
#         multiplicador-= 1

# resultado = (soma*10)%11

# print(resultado)

# resultado = 0 if resultado > 9 else resultado

# print(resultado)


# 746.824.890-70
# Segunda forma que eu fiz

cpf = input('Digite um cpf: ')

if ('.' in cpf) and ('-' in cpf):
    cpf_cru = f'{cpf[:3]}{cpf[4:7]}{cpf[8:11]}{cpf[12:]}'
else:
    cpf_cru = cpf

multiplicador_1 = 10
soma_1 = 0

for i in range(0, len(cpf_cru)-2):
    soma_1 += int(cpf_cru[i])*multiplicador_1
    multiplicador_1 -= 1

digito_1 = (soma_1*10) % 11

digito_1 = 0 if digito_1 > 9 else digito_1

print(digito_1)
