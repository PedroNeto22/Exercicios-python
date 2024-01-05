import random

cpf_nove_primeiros_digitos = ''

for i in range(9):
    cpf_nove_primeiros_digitos += str(random.randint(0, 9))

multiplicador_1 = 10
soma_1 = 0

for i in range(0, len(cpf_nove_primeiros_digitos)):
    soma_1 += int(cpf_nove_primeiros_digitos[i])*multiplicador_1
    multiplicador_1 -= 1

digito_1 = (soma_1*10) % 11

digito_1 = 0 if digito_1 > 9 else digito_1

cpf_incompleto = f'{cpf_nove_primeiros_digitos}{digito_1}'
multiplicador_2 = 11
soma_2 = 0

for i in range(0, len(cpf_incompleto)):
    soma_2 += int(cpf_incompleto[i])*multiplicador_2
    multiplicador_2 -= 1

digito_2 = (soma_2*10) % 11

digito_2 = 0 if digito_2 > 9 else digito_2

cpf_gerado = f'CPF-CRU: {cpf_nove_primeiros_digitos}{digito_1}{digito_2}'
cpf_gerado_formatado = f'CPF-FORMATADO: {cpf_nove_primeiros_digitos[:3]}.{cpf_nove_primeiros_digitos[3:6]}.{cpf_nove_primeiros_digitos[6:9]}-{digito_1}{digito_2}'

print(cpf_gerado)
print(cpf_gerado_formatado)
