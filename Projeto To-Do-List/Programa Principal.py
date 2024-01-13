from time import sleep

from sistema import *

# Programa Principal.
while True:
    menu("!LISTA DE TAREFAS!", "=")
    opçao("Adicionar Tarefas", "Mostrar Tarefas", "Concluir e Deletar", "Sair do Programa")

    try:
        opcao = int(input(f'{cores[3]}Qual opção deseja escolher:{cores[0]} '))
    except ValueError:
        print(f"{cores[1]}ERRO! Apenas números Inteiros.{cores[0]}\n")
        sleep(1)

    else:
        # Verificar a Opção Escolhida.
        if opcao == 1:
            cria_tarefas()
        elif opcao == 2:
            exibi_tarefas()
        elif opcao == 3:
            deletar_concluir_tarefas()
        elif opcao == 4:
            print()
            print(f'{cores[1]}ENCERRANDO O PROGRAMA...{cores[0]}\n')
            sleep(2)
            break
        else:
            print(f'{cores[1]}ERRO! Opção Invalida{cores[0]}\n')
        sleep(1)

# Finalizar o Programa com uma despedida :)
print(f'{cores[2]}FIM DO PROGRAMA, MUITO OBRIGADO POR TESTAR!')
print(f'{cores[1]}(PROXIMA ATUALIZAÇÃO VAI SALVAR SUAS TAREFAS)')
