from menu import *

from dadosTarefa import *

cores = ['\033[m',    # [0] Branco/Limpo
         '\033[31m',  # [1] Vermelho
         '\033[32m',  # [2] Verde
         '\033[34m']  # [3] Azul


# Função para criar tarefas desejadas.
def cria_tarefas():
    menu("!ADICIONAR TAREFAS!", "=")
    try:
        # verificar e Impedir dados Inválidos.
        while True:
            try:
                tarefa = str(input(f'{cores[3]}Digite a Tarefa aqui ->{cores[0]} ')).strip().title()
                if tarefa[0]:  # Verificar se está vázio
                    pass
            except IndexError:
                print(f'{cores[1]}ERRO! Não pode ficar vazio. Tente Novamente.{cores[0]}\n')
                continue

            else:
                if tarefa[0].isnumeric():
                    print(f'{cores[1]}ERRO! Comece com Letras e não números.{cores[0]}\n')
                    continue
                elif len(tarefa) < 5:
                    print(f'{cores[1]}Tente Novamente! (Minímo de 5 Caracteres){cores[0]}\n')
                    continue
                else:
                    adicionar_tarefa(tarefa)

            # Verificar respostas Valídas.
            while True:
                try:
                    resposta = str(input(f'{cores[3]}Deseja Continuar? (S/N){cores[0]} ')).strip().lower()[0]
                    if resposta in 'sn':
                        break
                    print(f'{cores[1]}ERRO! Apenas S ou N.{cores[0]}\n')
                except IndexError:
                    print(f'{cores[1]}ERRO! Apenas S ou N.{cores[0]}\n')

            print()
            if resposta == 'n':
                break
    except KeyboardInterrupt:
        print(f'{cores[1]}O usuário decidiu não colocar informações!{cores[0]}\n')


# Opções para Exibir a Lista de Tarefas "Salva".
def exibi_tarefas():
    menu("!LOCAL DE TAREFAS!", "=")
    try:
        # Verificar Entrada e Tratar erros.
        while True:
            try:
                opcao("Tarefas", "Tarefas Concluídas", "Tarefas Deletadas", "Tarefas Em Andamento", "Sair")
                resposta = int(input(f'{cores[3]}Sua Opção -> {cores[0]}'))
            except ValueError:
                print(f'{cores[1]}ERRO! Digite um número Inteiro.{cores[0]}\n')

            else:
                # Exibir as Listas, dada a Opção do Usuário.
                if resposta in [1, 2, 3, 4, 5]:
                    if resposta == 1:
                        estado_tarefa('todas')
                    elif resposta == 2:
                        estado_tarefa('concluida')
                    elif resposta == 3:
                        estado_tarefa('deletada')
                    elif resposta == 4:
                        estado_tarefa('pendente')
                    else:
                        break  # Sair do loop principal. OBS: Sim eu sei que não precisa falar
                else:
                    print(f'{cores[1]}ERRO! Opção não existe. Tente -> (1, 2, 3 ,4 ou 5){cores[0]}\n')
    except KeyboardInterrupt:
        print(f'{cores[1]}O usuário decidiu não colocar informações!{cores[0]}\n')


# Função para marca conclusão de uma Tarefa.
def concluir_tarefa():
    tarefas_pendentes = nome_tarefas()
    pendentes = status_tarefa()
    lista_pendentes = []

    for pos in range(len(tarefas_pendentes)):
        if pendentes[pos] == '[]':
            lista_pendentes.append(tarefas_pendentes[pos])

    menu("!CONCLUSÃO DE TAREFA!", "=")

    while True:
        if len(lista_pendentes) == 0:
            print(f'{cores[1]}--> Não há Tarefas Pendentes! <--{cores[0]}\n')
            break

        for pos in range(len(lista_pendentes)):
            print(f'{pos+1:<2} - [] {lista_pendentes[pos]}')
        print()

        try:
            concluir = int(input(f'{cores[3]}Tarefa concluída ->{cores[0]} '))
        except ValueError:
            print(f'{cores[1]}ERRO! Apenas números Inteiros.{cores[0]}\n')

        else:
            if (concluir - 1) >= len(lista_pendentes) or (concluir - 1) <= -1:
                print(f'{cores[1]}ERRO! Tarefa não encontrada. Tente Novamente\n{cores[0]}')

            else:
                # Adicionar a Lista de tarefas Concluídas.
                tarefa_conluida = f'[X] {lista_pendentes[concluir-1]}\n'
                altera_tarefa(tarefas_pendentes.index(lista_pendentes[concluir-1]), tarefa_conluida)
                atualizar()
                break


# Função para deletar tarefas.
def deletar_tarefa():
    tarefas_concluida = nome_tarefas()
    concluido = status_tarefa()
    lista_concluida = []
    for pos in range(len(concluido)):
        if concluido[pos] == '[X]':
            lista_concluida.append(tarefas_concluida[pos])

    menu("!DELETAR TAREFA!", "=")
    while True:
        if len(lista_concluida) == 0:
            print(f'{cores[1]}--> Não há mais Tarefas Concluídas para serem Deletadas <--{cores[0]}\n')
            break
        for pos in range(len(lista_concluida)):
            print(f'{pos+1:<2} - [X] {lista_concluida[pos]}')
        print()

        try:
            deletar = int(input(f'{cores[3]}Deletar Tarefa ->{cores[0]} '))
        except ValueError:
            print(f'{cores[1]}ERRO! Apenas números Inteiros.{cores[0]}\n')

        else:
            if (deletar - 1) >= len(lista_concluida) or (deletar - 1) <= -1:
                print(f'{cores[1]}ERRO! Tarefa não encontrada. Tente Novamente{cores[0]}\n')

            else:
                # Deletar Tarefas Concluídas.
                deleta_tarefa = f'R {lista_concluida[deletar-1]}\n'
                altera_tarefa(tarefas_concluida.index(lista_concluida[deletar-1]), deleta_tarefa)
                atualizar()
                break


# Função para Concluir/Deletar Tarefas.
def deletar_concluir_tarefas():
    menu("Deletar/Concluir Tarefa", "=")

    while True:
        opcao("Marca Tarefa Concluída", "Deletar Tarefa", "Sair")
        try:
            resposta = int(input(f'{cores[3]}Sua opção ->{cores[0]} '))
        except ValueError:
            print(f'{cores[1]}ERRO! Apenas números Inteiros.{cores[0]}\n')

        else:
            if resposta not in [1, 2, 3]:
                print(f'{cores[1]}Opção não encontrada Tente Novamente.{cores[0]}\n')

            else:
                print()
                if resposta == 1:
                    concluir_tarefa()
                elif resposta == 2:
                    deletar_tarefa()
                else:
                    break
