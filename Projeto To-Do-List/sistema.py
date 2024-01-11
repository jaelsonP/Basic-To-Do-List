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
                opçao("Tarefas", "Tarefas Concluídas", "Tarefas Deletadas", "Tarefas Em Andamento", "Sair")
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


"""
# Função para marca conclusão de uma Tarefa.
def concluir_tarefa():
    menu("!CONCLUSÃO DE TAREFA!", "=")

    while True:
        if len(tarefasAndamento) == 0:
            print(f'{cores[1]}--> Não há Tarefas Pendentes! <--{cores[0]}\n')
            break
        mostrar_tarefas_ordenadas(tarefasAndamento, cores[0])
        try:
            concluir = int(input(f'{cores[3]}Tarefa concluída ->{cores[0]} '))
        except ValueError:
            print(f'{cores[1]}ERRO! Apenas números Inteiros.{cores[0]}\n')

        else:
            if (concluir - 1) >= len(tarefasAndamento) or (concluir - 1) <= -1:
                print(f'{cores[1]}ERRO! Tarefa não encontrada. Tente Novamente\n{cores[0]}')

            else:
                # Adicionar a Lista de tarefas Concluídas.
                salvarPro = tarefasAndamento[concluir - 1][3::]
                listaTarefas.pop(concluir - 1)
                tarefasAndamento.pop(concluir - 1)
                tarefasConcluida.append(f'{cores[2]}[x] {salvarPro}{cores[0]}')   # Cor verde
                listaTarefas.insert(concluir, f'{cores[2]}[x] {salvarPro}{cores[0]}')
                break


# Função para deletar tarefas.
def deletar_tarefa():
    menu("!DELETAR TAREFA!", "=")
    while True:
        if len(tarefasConcluida) == 0:
            print(f'{cores[1]}--> Não há mais Tarefas Concluídas para serem Deletadas <--{cores[0]}\n')
            break
        mostrar_tarefas_ordenadas(tarefasConcluida, cores[0])
        try:
            deletar = int(input(f'{cores[3]}Deletar Tarefa ->{cores[0]} '))
        except ValueError:
            print(f'{cores[1]}ERRO! Apenas números Inteiros.{cores[0]}\n')

        else:
            if (deletar - 1) >= len(tarefasConcluida) or (deletar - 1) <= -1:
                print(f'{cores[1]}ERRO! Tarefa não encontrada. Tente Novamente{cores[0]}\n')

            else:
                # Deletar Tarefas Concluídas.
                deletarPro = tarefasConcluida[deletar - 1][9::]
                tarefasConcluida.pop(deletar - 1)
                listaTarefas.pop(deletar - 1)
                tarefasDeletada.append(deletarPro)
                break


# Função para Concluir/Deletar Tarefas.
def deletar_concluir_tarefas():
    menu("Deletar/Concluir Tarefa" , "=")

    while True:
        opçao("Marca Tarefa Concluída", "Deletar Tarefa", "Sair")
        try:
            opcao = int(input(f'{cores[3]}Sua opção ->{cores[0]} '))
        except ValueError:
            print(f'{cores[1]}ERRO! Apenas números Inteiros.{cores[0]}\n')

        else:
            if opcao not in [1, 2, 3]:
                print(f'{cores[1]}Opção não encontrada Tente Novamente.{cores[0]}\n')

            else:
                print()
                if opcao == 1:
                    concluir_tarefa()
                elif opcao == 2:
                    deletar_tarefa()
                else:
                    break

"""