def myfun(num):
  if num % 2 == 0:
    return 'par'
  return 'impar'


num = int(input('Digite um numero: '))

resultado = myfun(num)

print(resultado)