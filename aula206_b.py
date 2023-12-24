# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

class pessoa:

  def __init__(self,nome,sobrenome,idade):
    self.nome = nome
    self.sobrenome = sobrenome
    self.idade = idade

with open('aula206.json','r') as arquivo:
  dados = json.load(arquivo)

pessoa1 = pessoa(**dados)

print(pessoa1.nome)


