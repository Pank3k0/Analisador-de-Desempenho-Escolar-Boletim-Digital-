import os

alunos = [[1,'amanda soninho']]
notas = []
boletim = []

def lista(tipo):
    if tipo == 'aluno':
        for aluno in alunos:
            print(f'Aluno: {aluno[0]} | {aluno[1]}')
    elif tipo == 'nota':
        for nota in notas:
            print(f'Nota : {nota[0]} | {nota[1]} | {nota[2]}')

# função pra adicionar coisas nas listas

def add(tipo):
    if tipo == 'alunos':
        codigo = len(alunos) + 1
        aluno = input('Digite o nome do aluno: ')
        alunos.append([aluno])
    elif tipo == 'notas':
        codigo = len(notas) + 1
        nota1 = float(input('digite a nota do 1° bimestre: '))
        nota2 = float(input('digite a nota do 2° bimestre: '))
        notas.append([codigo, nota1, nota2])
    elif tipo == 'boletim':
        lista('aluno')
        sniggers = int(input('digite o codigo do aluno: '))
        codigo = len(boletim) + 1

# função dos menus

def menus(menu):
    if menu == 'principal':
        print('+-------------------------+\n')
        print('1. Alunos\n')
        print('2. Avaliações\n')
        print('3. Boletim\n')
        print('0. Sair\n')
        print('+-------------------------+\n')
    elif menu == 'avaliacao':
        print('+-----------------------+\n')
        print('1.Adicionar notas\n')
        print('2.Ver notas cadastradas\n')
        print('0.Voltar\n')
        print('+-----------------------+\n')
        print('')
    elif menu == 'alunos':
        print('+-----------------------------+\n')
        print('1.Adicionar alunos\n')
        print('2.Ver alunos\n')
        print('0.Voltar\n')
        print('+-----------------------------+\n')
    elif menu == 'adnotas':
        print('+----------------------+\n')
        print('Adicionar notas\n')
        print('+----------------------+\n')
    elif menu == 'Boletim':
        print('\nBoletem Digital\n')
        print('+---------------------+\n')
        print('1.Criar Boletim\n')
        print('2.Ver Boletins\n')
        print('0.Voltar\n')
        print('+---------------------+\n')

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
    clear_screen()
    show_text()
    menus('principal')
    opcao = int(input('Olá, escolha a opção desejada: '))

#  aluno. Se possivel nao mexam, nao sei como esta funcionando
    if opcao == 1:
        clear_screen()
        menus('alunos')
        escolha = int(input('Selecione a opção desejada: '))

        if  escolha == 1:
            add('alunos')
            clear_screen()

        elif escolha == 2:
            print('\nAlunos Cadastrados\n')

            if len(alunos) == 0:
                print('Nenhum aluno cadastrado')

            else:
                clear_screen()
                lista('aluno')
                input('\nP' \
                'ressione ENTER para voltar')
                clear_screen()
                continue

# acabou o aluno e começa a saida pq eu quero

    if opcao == 0:
        break

# agr a avaliação >:3

    if opcao == 2:
        clear_screen()
        menus('avaliacao')
        escolha2 = int(input('selecione a opção que desejar: '))

        if escolha2 == 1:
            clear_screen()
            menus('adnotas')
            add('notas')
            clear_screen()
        
        elif escolha2 == 2:
            clear_screen()
            print('Notas Cadastradas\n')
            
            if len(notas) == 0:
                clear_screen()
                print('Nenhuma nota cadastrada')
                input('pressione ENTER para voltar ')
            else:
                lista('nota')
                input('\npressione ENTER para voltar ')



# Boletim TwT

    if opcao == 3:
        clear_screen()
        menus('Boletim')
        opcao3 = int(input('\nSelecione a opção desejada: '))
        
        if opcao3 == 1:
            clear_screen()
            lista('aluno')

            clear_screen()
            print('Boletim criado com sucesso?')
            input('\nPressione ENTER para voltar')
            clear_screen()