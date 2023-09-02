#746.824.890-70

cpf = input('Digite um cpf: ')

if ('.' in cpf) and ('-' in cpf):
    cpf_cru = f'{cpf[:3]}{cpf[4:7]}{cpf[8:11]}{cpf[12:]}'
else:
    cpf_cru = cpf

multiplicador = 11
soma = 0

for i in range(0,len(cpf_cru)-1):
    soma += int(cpf_cru[i])*multiplicador
    multiplicador -= 1

resultado = (soma*10)%11

resultado = 0 if resultado > 9 else resultado

print(resultado)

