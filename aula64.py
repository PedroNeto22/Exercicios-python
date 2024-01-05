name = 'Pedro Neto'
tamanho_nome = len(name)
count = 0
new_name = ''
while count < tamanho_nome:
    new_name += f"*{name[count]}"
    count += 1
new_name += '*'
print(new_name)
