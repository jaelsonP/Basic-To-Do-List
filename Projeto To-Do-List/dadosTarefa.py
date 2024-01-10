def adicionar_tarefa(nome_tarefa):
    with open("Tarefas.txt", "a") as tarefa:
        tarefa.write(f'[] {nome_tarefa}\n')


def ver_tarefas():
    with open("Tarefas.txt", "r") as tarefa:
        listaTarefas = tarefa.readlines()
        return listaTarefas


def renomear_tarefa():
    pass

