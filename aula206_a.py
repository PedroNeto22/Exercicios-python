# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json


class pessoa:

    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


pessoa1 = pessoa('Pedro', 'Neto', 19)

with open('aula206.json', 'w') as arquivo:
    json.dump(vars(pessoa1), arquivo)
