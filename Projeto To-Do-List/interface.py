amarelo = '\033[33m'
branco = '\033[m'


def menu(texto, simbolo):
    tamanho = len(texto) * 2
    print(f'{simbolo}' * tamanho)
    print(texto.center(tamanho))
    print(f'{simbolo}' * tamanho)


def opçao(*texto):
    for pos, opcao in enumerate(texto):
        print(f'{amarelo}{pos+1} - {opcao}{branco}')
    print()
