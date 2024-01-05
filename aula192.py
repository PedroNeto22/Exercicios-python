import os

# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

todo: list[str] = []

lista_opcao = ["refazer", "desfazer", "listar", "clear"]
lista_de_troca = []


def desfazer(todo: list):
    lista_de_troca.append(todo.pop())


def refazer(todo: list):
    todo.append(lista_de_troca.pop())


def listar(todo: list):
    print('TAREFAS:')
    print(*todo, sep='\n')


def escolher_opcao():
    print('Comandos: refazer, desfazer, listar, clear')
    opcao = input('Escolha uma ação ou digite uma tarefa: ')
    if opcao in lista_opcao:
        return opcao.lower()
    return opcao


def limpar_terminal():
    os.system('clear')


while True:
    opcao = escolher_opcao()

    if opcao in lista_opcao:
        if opcao == lista_opcao[0]:
            if len(lista_de_troca) == 0:
                print('NADA PARA REFAZER')
                continue
            refazer(todo)
        if opcao == lista_opcao[1]:
            if len(todo) == 0:
                print('NADA PARA DESFAZER')
                continue
            desfazer(todo)
        if opcao == lista_opcao[2]:
            if len(todo) == 0:
                print('NADA PARA LISTAR')
                continue
            listar(todo)
        if opcao == lista_opcao[3]:
            limpar_terminal()
    else:
        todo.append(opcao)
        print('TAREFAS:')
        print(*todo, sep='\n')
