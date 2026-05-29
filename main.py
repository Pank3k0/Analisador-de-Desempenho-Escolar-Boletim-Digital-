import os

def error():
        print('===============================================================')
        print('')
        print('   Sentimos muito, essa opção esta indisponivel no momento')
        print('')
        print('===============================================================')
        print('Pressione 0 para voltar')


aluno_nome = input('Digite seu nome: ').upper()

# função para limpar a tela

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para o titulo

def show_text():
    print('______       _      _   _            ______ _       _ _        _ ')
    print('| ___ \\     | |    | | (_)           |  _  (_)     (_) |      | |')
    print('| |_/ / ___ | | ___| |_ _ _ __ ___   | | | |_  __ _ _| |_ __ _| |')
    print("| ___ \\/ _ \\| |/ _ \\ __| | '_ ` _ \\  | | | | |/ _` | | __/ _` | |")
    print('| |_/ / (_) | |  __/ |_| | | | | | | | |/ /| | (_| | | || (_| | |')
    print('|____/ \\___/|_|\\___|\\__|_|_| |_| |_| |___/ |_|\\__, |_|\\__\\__,_|_|')
    print('                                               __/ |             ')
    print('                                              |___/              ')
    print('')
    

while True:
    print('')
    print('')
    show_text()
    print('===============================================')
    print('')
    print('1. Alunos')
    print('')
    print('2. Avaliações')
    print('')
    print('3. Boletim')
    print('')
    print('0. Sair')
    print('')
    print('===============================================')
    print('')
    opcao = int(input(f'Olá, {aluno_nome} escolha a opção desejada: '))

# aluno, se possivel nao mexam, nao sei como esta funcionando

    if opcao == 1:
        clear_screen()
        print('===============================================================')
        print('')
        print(f'ALuno: {aluno_nome}')
        print('')
        print('===============================================================')
        print('Digite 0 para voltar')
        opcao_diferente1 = int(input(f'{aluno_nome}, você deseja retornar?  '))
        if opcao_diferente1 == 0:
            clear_screen()
        continue

    else:
            print('opção invalida, por favor, tente novamente')

# acabou o aluno e começa a saida pq eu quero

    if opcao == 0:
        break

# agr a avaliação >:3

    if opcao == 2:
        clear_screen()
        error()
        opcao_diferente1 = int(input(f'{aluno_nome}, você deseja retornar?  '))
        clear_screen()
        if opcao_diferente1 == 0:
            continue

    else:
            print('opção invalida, por favor, tente novamente')

# Boletim TwT

    if opcao == 3:
        clear_screen()
        error()
    opcao_diferente1 = int(input(f'{aluno_nome}, você deseja retornar? '))
    clear_screen()
    if opcao_diferente1 == 0:
        continue

    else:
            print('opção invalida, por favor, tente novamente')