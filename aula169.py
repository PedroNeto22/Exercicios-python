# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(lista1, lista2):
    menor_lista = min(lista1, lista2, key=len)
    nova_lista = [(lista1[i], lista2[i]) for i in range(len(menor_lista))]
    return nova_lista


print(zipper(['Salvador', 'Ubatuba', 'Belo Horizonte'],
      ['BA', 'SP', 'MG', 'RJ']))
