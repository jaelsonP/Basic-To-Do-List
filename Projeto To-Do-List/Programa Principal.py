from time import sleep

from sistema import *

# Programa Principal.
while True:
    menu("!LISTA DE TAREFAS!", "=")
    opcao("Adicionar Tarefas", "Mostrar Tarefas", "Concluir e Deletar", "Sair do Programa")

    try:
        resp = int(input(f'{cores[3]}Qual opção deseja escolher:{cores[0]} '))
    except ValueError:
        print(f"{cores[1]}ERRO! Apenas números Inteiros.{cores[0]}\n")
        sleep(1)

    else:
        # Verificar a Opção Escolhida.
        if resp == 1:
            cria_tarefas()
        elif resp == 2:
            exibi_tarefas()
        elif resp == 3:
            deletar_concluir_tarefas()
        elif resp == 4:
            print()
            print(f'{cores[1]}ENCERRANDO O PROGRAMA...{cores[0]}\n')
            sleep(2)
            break
        else:
            print(f'{cores[1]}ERRO! Opção Invalida{cores[0]}\n')
        sleep(1)

# Finalizar o Programa com uma despedida :)
print(f'{cores[2]}FIM DO PROGRAMA, MUITO OBRIGADO POR TESTAR!')
