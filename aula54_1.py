num = input('Digite um numero inteiro ')

num_int = None

try:
  num_int = int(num)
  if num_int % 2 == 0:
    print('Esse numero é par')
  else:
    print('Esse numero é impar')
except:
    print('Esse numero não é um inteiro')