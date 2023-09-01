import os

lista = []

while True:
  print('Selecione uma opção')
  valid_options = ['i','a','l']
  option_list = input('[i]nserir [a]pagar [l]istar: ')

  if option_list not in valid_options:
    print('Selecione uma opção valida')
  if option_list == 'i':
    os.system('clear')
    add_list = input('Valor: ')
    lista.append(add_list)
    continue
  if option_list == 'l':
    os.system('clear')
    for i in range(0,len(lista)):
      print(i,lista[i])
    continue
  if option_list == 'a':
    try:
      remove_option = int(input('Selecione um índice para remover: '))
      lista.pop(remove_option)
    except:
      os.system('clear')
      print('Selecione um índice valido')
      continue
