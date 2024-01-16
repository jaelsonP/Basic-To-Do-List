from dadosTarefa import *

cores = ['\033[m',    # [0] Branco/Limpo
         '\033[31m',  # [1] Vermelho
         '\033[33m',  # [2] Amarelo
         '\033[32m']  # [3] Verde


def menu(texto, simbolo):
    tamanho = len(texto) * 2
    print(f'{simbolo}' * tamanho)
    print(texto.center(tamanho))
    print(f'{simbolo}' * tamanho)


def opcao(*texto):
    # Exibir Várias opções.
    for i, valor in enumerate(texto):
        print(f'{cores[2]}{i+1} - {valor}{cores[0]}')
    print()


# Função para pegar o nome Completo da tarefa
def nome_tarefas():
    tarefas = ver_tarefas()
    lista_nomes = []

    # Criar uma repetição para cada Nome.
    for nome in tarefas:
        nome_tarefa = nome.split()[1::]
        comprimento = len(nome_tarefa)
        nome_completo = ''

        # Concatenar a Tarefa Completa.
        for i in range(comprimento):
            if i < comprimento:
                nome_completo += nome_tarefa[i] + ' '
                continue
            nome_completo += nome_tarefa[i]

        lista_nomes.append(nome_completo)
    return lista_nomes


def status_tarefa():
    status = ver_tarefas()
    lista_status = []

    # Criar uma lista para Status.
    for statu in status:
        statu_tarefa = statu.split()[0]
        lista_status.append(statu_tarefa)

    return lista_status


def estado_tarefa(estado):
    tarefas = nome_tarefas()
    comprimento = len(tarefas)
    status = status_tarefa()

    # Listar todas as Tarefas.
    if estado == 'todas':
        for i in range(comprimento):
            if status[i] == '[]':
                print(f'{status[i]:<3} - {tarefas[i]}')
            elif status[i] == '[X]':
                print(f'{cores[3]}{status[i]:<3} - {tarefas[i]}{cores[0]}')
            else:
                print(f'{cores[1]}{tarefas[i]}{cores[0]}')

    # Listar tarefas Concluída.
    elif estado == 'concluida':
        for i in range(comprimento):
            if status[i] == '[X]':
                print(f'{cores[3]}{status[i]:<3} - {tarefas[i]}{cores[0]}')

    # Listar tarefas Deletadas.
    elif estado == 'deletada':
        for i in range(comprimento):
            if status[i] == 'R':
                print(f'{cores[1]}{tarefas[i]}{cores[0]}')

    # Listar tarefas Pendentes
    else:
        for i in range(comprimento):
            if status[i] == '[]':
                print(f'{status[i]:<3} - {tarefas[i]}')

    print()
    