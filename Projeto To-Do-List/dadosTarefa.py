def adicionar_tarefa(nome_tarefa):
    with open("Tarefas.txt", "a") as tarefa:
        tarefa.write(f'[] {nome_tarefa}\n')


def ver_tarefas():
    with open("Tarefas.txt", "r") as tarefa:
        listaTarefas = tarefa.readlines()
        return listaTarefas


def altera_tarefa(pos, tarefa):
    with open("Tarefas.txt", "r+") as tarefas:
        lista_tarefas = tarefas.readlines()

        if 0 <= pos < len(lista_tarefas):
            lista_tarefas[pos] = f'{tarefa}'

            tarefas.seek(0)
            tarefas.writelines(lista_tarefas)


def atualizar():
    todas_tarefas = ver_tarefas()
    nova_lista = []
    for tarefa in todas_tarefas:
        if tarefa[0] == '\n':
            continue
        else:
            nova_lista.append(tarefa)
    with open("Tarefas.txt", "w") as tarefas:
        tarefas.writelines(nova_lista)
