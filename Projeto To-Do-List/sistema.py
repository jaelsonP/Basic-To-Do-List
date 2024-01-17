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
                # Receber nome para Tarefa.
                print(f'{cores[3]}Digite "Sair" para Sair{cores[0]}')
                tarefa = str(input(f'{cores[3]}Digite a Tarefa aqui ->{cores[0]} ')).strip().title()

                if tarefa == 'Sair':
                    break

                if tarefa[0]:  # Verificar se está vázio
                    pass

            except IndexError:
                print(f'{cores[1]}ERRO! Não pode ficar vazio. Tente Novamente.{cores[0]}\n')
                continue

            else:
                # Impedir o começo de Números.
                if tarefa[0].isnumeric():
                    print(f'{cores[1]}ERRO! Comece com Letras e não números.{cores[0]}\n')
                    continue
                # Verificar tamanho Mínimo.
                elif len(tarefa) < 5:
                    print(f'{cores[1]}Tente Novamente! (Minímo de 5 Caracteres){cores[0]}\n')
                    continue
                # Criar a Tarefa.
                else:
                    adicionar_tarefa(tarefa)
            print()

    except KeyboardInterrupt:
        print(f'{cores[1]}...{cores[0]}\n')
        return True


# Opções para Exibir a Lista de Tarefas "Salva".
def exibi_tarefas():
    menu("!LOCAL DE TAREFAS!", "=")

    try:
        # Verificar Entrada e Tratar erros.
        while True:
            try:
                opcao("Tarefas", "Tarefas Concluídas", "Tarefas Deletadas", "Tarefas Em Andamento", "Sair")
                escolha = int(input(f'{cores[3]}Sua Opção -> {cores[0]}'))

            # Evita resposta Vázia e Letras.
            except ValueError:
                print(f'{cores[1]}ERRO! Digite um número Inteiro.{cores[0]}\n')

            else:
                # Exibir as Listas, dada a Opção do Usuário.
                if escolha in [1, 2, 3, 4, 5]:
                    if escolha == 1:
                        estado_tarefa('todas')
                    elif escolha == 2:
                        estado_tarefa('concluida')
                    elif escolha == 3:
                        estado_tarefa('deletada')
                    elif escolha == 4:
                        estado_tarefa('pendente')
                    else:
                        break
                else:
                    print(f'{cores[1]}ERRO! Opção não existe. Tente -> (1, 2, 3 ,4 ou 5){cores[0]}\n')

    except KeyboardInterrupt:
        print(f'{cores[1]}...{cores[0]}\n')
        return True


# Função para marca conclusão de uma Tarefa.
def concluir_tarefa():
    tarefas_pendentes = nome_tarefas()
    pendentes = status_tarefa()
    lista_pendentes = []
    try:
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
                concluir = int(input(f'{cores[3]}Tarefa concluída ->{cores[0]} ')) - 1

            except ValueError:
                print(f'{cores[1]}ERRO! Apenas números Inteiros.{cores[0]}\n')

            else:
                if concluir >= len(lista_pendentes) or concluir <= -1:
                    print(f'{cores[1]}ERRO! Tarefa não encontrada. Tente Novamente\n{cores[0]}')

                else:
                    # Atualizar o Status da tarefa para Concluída.
                    tarefa_concluida = f'[X] {lista_pendentes[concluir]}'
                    tarefa_pendente = f'[] {lista_pendentes[concluir]}'

                    altera_tarefa(pesquisar(tarefa_pendente), tarefa_concluida)
                    break

    except KeyboardInterrupt:
        print(f'{cores[1]}...{cores[0]}\n')
        return True


# Função para deletar tarefas Concluída.
def deletar_tarefa():
    tarefas_concluida = nome_tarefas()
    concluido = status_tarefa()
    lista_concluida = []

    try:
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
                # Analisar qual tarefa será deletada
                deletar = int(input(f'{cores[3]}Deletar Tarefa ->{cores[0]} ')) - 1
            except ValueError:
                print(f'{cores[1]}ERRO! Apenas números Inteiros.{cores[0]}\n')

            else:
                if deletar >= len(lista_concluida) or deletar <= -1:
                    print(f'{cores[1]}ERRO! Tarefa não encontrada. Tente Novamente{cores[0]}\n')

                else:
                    # Deletar Tarefas Concluídas.
                    deleta_tarefa = f'R {lista_concluida[deletar]}'
                    tarefa_concluida = f'[X] {lista_concluida[deletar]}'

                    altera_tarefa(pesquisar(tarefa_concluida), deleta_tarefa)
                    break

    except KeyboardInterrupt:
        print(f'{cores[1]}...{cores[0]}\n')
        return True


# Função para Concluir/Deletar Tarefas.
def deletar_concluir_tarefas():
    menu("Deletar/Concluir Tarefa", "=")

    try:
        while True:
            opcao("Marca Tarefa Concluída", "Deletar Tarefa", "Sair")

            try:
                # Analisar escolha.
                escolha = int(input(f'{cores[3]}Sua opção ->{cores[0]} '))

            except ValueError:
                print(f'{cores[1]}ERRO! Apenas números Inteiros.{cores[0]}\n')

            else:
                if escolha not in [1, 2, 3]:
                    print(f'{cores[1]}Opção não encontrada Tente Novamente.{cores[0]}\n')

                else:
                    print()
                    if escolha == 1:
                        if concluir_tarefa():
                            return True
                    elif escolha == 2:
                        if deletar_tarefa():
                            return True
                    else:
                        break
                    atualizar()

    except KeyboardInterrupt:
        print(f'{cores[1]}...{cores[0]}\n')
        return True
