import os

alunos = []
notas = []
boletim = []

# função pra adicionar coisas nas listas

def add(tipo):
    if tipo == 'alunos':
        aluno = input('Digite o nome do aluno: ')
        alunos.append(aluno)
    
    elif tipo == 'notas':
        nota1 = float(input('digite a nota do 1° bimestre: '))
        nota2 = float(input('digite a nota do 2° bimestre: '))
        notas.append([nota1, nota2])

# função dos menus

def menus(menu):
    global nota1, nota2
    if menu == 'principal':
        print('+-------------------------+')
        print('1. Alunos')
        print('')
        print('2. Avaliações')
        print('')
        print('3. Boletim')
        print('')
        print('0. Sair')
        print('+-------------------------+')
        print('')
    elif menu == 'segundo':
        print('+-----------------------+')
        print('')
        print('Cadastro de Notas')
        print('')
        print('+-----------------------+')
        print('')
    elif menu == 'terceiro':
        print('+-------------------+')
        print('')
        print('Boletem Digital')
        print('')
        print('+-------------------+')

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
    menus('principal')
    opcao = int(input('Olá, escolha a opção desejada: '))

# aluno, se possivel nao mexam, nao sei como esta funcionando

    if opcao == 1:
        clear_screen()
        print('+-----------------------------+')
        print('')
        print('1.Adicionar alunos')
        print('2.Ver alunos')
        print('0.Voltar')
        print('')
        print('+-----------------------------+')
        escolha = int(input('Selecione a opção desejada: '))

        if  escolha == 1:
            add('alunos')
            clear_screen()
            continue

        elif escolha == 2:
            print('\nAlunos Cadastrados\n')

            if len(alunos) == 0:
                print('Nenhum aluno cadastrado')

            else:
                clear_screen()
                for i, aluno in enumerate(alunos, start=1):
                    print(f'{i}. {aluno}')

            input('Pressione ENTER para voltar')
            clear_screen()
            continue

# acabou o aluno e começa a saida pq eu quero

    if opcao == 0:
        break

# agr a avaliação >:3

    if opcao == 2:
        clear_screen()
        menus('segudo')
        for i, aluno in enumerate(alunos, start=1):
            print(f'{i}. {aluno}')
        int(input('Escolha o código do Aluno: '))-1
        add('notas')
        clear_screen()
        continue

# Boletim TwT

        if opcao == 3:
            print('em manutenção, voltamos em breve')
            clear_screen
            continue
