import os

alunos = [['amanda soninho']]
notas = []
boletim = []

# função pra adicionar coisas nas listas
def lista():
    for i, aluno in enumerate(alunos, start=1):
        print(f'{i}. {aluno}')


def add(tipo):
    if tipo == 'alunos':
        aluno = input('Digite o nome do aluno: ')
        alunos.append([aluno])
    
    elif tipo == 'notas':
        nota1 = float(input('digite a nota do 1° bimestre: '))
        nota2 = float(input('digite a nota do 2° bimestre: '))
        notas.append([nota1, nota2])

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
        print('+-------------------+\n')
        print('Boletem Digital\n')
        print('+-------------------+\n')

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
                lista()

            input('Pressione ENTER para voltar')
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
            add(notas)
        
        elif escolha2 == 2:
            clear_screen()
            print('\nNotas Cadastrados\n')
            if len(notas) == 0:
                print('Nenhuma nota cadastrada')

            else:
                clear_screen()
                lista()
        



# Boletim TwT

    if opcao == 3:
        clear_screen
        menus('boletim')

        continue