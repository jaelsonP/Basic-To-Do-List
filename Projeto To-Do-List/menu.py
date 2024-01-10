from dadosTarefa import *

vermelho = '\033[31m'
amarelo = '\033[33m'
branco = '\033[m'


def menu(texto, simbolo):
    tamanho = len(texto) * 2
    print(f'{simbolo}' * tamanho)
    print(texto.center(tamanho))
    print(f'{simbolo}' * tamanho)


def opçao(*texto):
    for pos, opcao in enumerate(texto):
        print(f'{amarelo}{pos+1} - {opcao}{branco}')
    print()


# Função para pegar o nome Completo da tarefa
def nome_tarefas():
    tarefas = ver_tarefas()
    lista_tarefas = []
    for tarefa in tarefas:
        nome_tarefa = tarefa.split()[1::]
        nome_completo = ''
        for palavra in nome_tarefa:
            nome_completo += palavra + ' '
        lista_tarefas.append(nome_completo)
    return lista_tarefas


def status_tarefa():
    status = ver_tarefas()
    pass




def estado_tarefa(opcao):
    pass