from time import sleep
from sistema import *

# Programa Principal.
while True:
    try:
        menu("!LISTA DE TAREFAS!", "=")
        opcao("Adicionar Tarefas", "Mostrar Tarefas", "Concluir e Deletar", "Sair do Programa")

        try:
            # Analisar a Escolha.
            escolha = int(input(f'{cores[3]}Qual opção deseja escolher:{cores[0]} '))

        except ValueError:
            print(f"{cores[1]}ERRO! Apenas números Inteiros.{cores[0]}\n")

        else:
            # Verificar a Opção Escolhida.
            if escolha == 1:
                if cria_tarefas():
                    break

            elif escolha == 2:
                if exibi_tarefas():
                    break

            elif escolha == 3:
                if deletar_concluir_tarefas():
                    break

            elif escolha == 4:
                print(f'\n{cores[1]}ENCERRANDO O PROGRAMA...{cores[0]}\n')
                sleep(2)
                break

            else:
                print(f'{cores[1]}ERRO! Opção Invalida{cores[0]}\n')
            sleep(1)

    except KeyboardInterrupt:
        print(f'{cores[1]}...{cores[0]}\n')

# Finalizar o Programa com uma despedida :)
print(f'{cores[2]}FIM DO PROGRAMA, MUITO OBRIGADO POR TESTAR!')
