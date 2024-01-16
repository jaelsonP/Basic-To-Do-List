def adicionar_tarefa(nome_tarefa):
    with open("Tarefas.txt", "a") as tarefa:
        # Adicionar Tarefa e seus Status.
        tarefa.write(f'[] {nome_tarefa}\n')


def ver_tarefas():
    with open("Tarefas.txt", "r") as tarefa:
        # Criar uma lista com Tarefas.
        listaTarefas = tarefa.readlines()
        return listaTarefas


def altera_tarefa(pos, tarefa):
    with open("Tarefas.txt", "r+") as tarefas:
        lista_tarefas = tarefas.readlines()

        # Atualizar a Tarefa desejada.
        if 0 <= pos < len(lista_tarefas):
            lista_tarefas[pos] = f'{tarefa}'

            tarefas.seek(0)  # Direcionar para o começo.
            tarefas.writelines(lista_tarefas)  # Reescrever com suas alterações.


def atualizar():
    todas_tarefas = ver_tarefas()  # Recebe uma lista das Tarefas.
    nova_lista = []

    for tarefa in todas_tarefas:
        # Verificar Tarefa espaçada.
        if tarefa[0] == '\n':
            continue
        else:
            nova_lista.append(tarefa)

    # Retirar espaços em branco.
    with open("Tarefas.txt", "w") as tarefas:
        tarefas.writelines(nova_lista)
