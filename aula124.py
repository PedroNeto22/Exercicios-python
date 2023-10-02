perguntas = [
    {
      'Pergunta': 'Quanto é 2+2',
      'Opções': ['1','3','4','5'] ,
      'Resposta': '4'
    },
    {
      'Pergunta': 'Quanto é 5*5',
      'Opções': ['25','55','10','51'] ,
      'Resposta': '25'
    },
    {
      'Pergunta': 'Quanto é 10/2',
      'Opções': ['4','5','2','1'] ,
      'Resposta': '5'
    },
]


def questionario(perguntas):
  acertos = 0 
  for i in perguntas:
    print(f'Pergunta: {i.get("Pergunta")}')
    for index,op in enumerate(i.get('Opções')):
      if op == i.get("Resposta"):
        resp = str(index)
      print(f'{index}) {op}')
    opcao = input('Escolha uma opção: ')
    if opcao == resp:
      print('Acertou 👍')
      acertos += 1
    else:
      print('Errou ❌')

  print(f'Voce acertou {acertos}, de {len(perguntas)} perguntas')

questionario(perguntas)