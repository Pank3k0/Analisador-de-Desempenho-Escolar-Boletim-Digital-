aluno_nome = input('Digite seu nome: ').upper()

def text():
    print("__________       .__          __  .__          ________  .__       .__  __         .__   ")
    print("\\______   \\ ____ |  |   _____/  |_|__| _____   \\______ \\ |__| ____ |__|/  |______  |  |  ")
    print(" |    |  _//  _ \\|  | _/ __ \\   __\\  |/     \\   |    |  \\|  |/ ___\\|  \\   __\\__  \\ |  |  ")
    print(" |    |   (  <_> )  |_\\  ___/|  | |  |  Y Y  \\  |    `   \\  / /_/  >  ||  |  / __ \\|  |__")
    print(" |______  /\\____/|____/\\___  >__| |__|__|_|  / /_______  /__\\___  /|__||__| (____  /____/")
    print("        \\/                 \\/              \\/          \\/  /_____/               \\/      ")

while True:
    text()
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
    opcao = int(input(f'Olá, {aluno_nome} escolha a opção desejada: '))

# aluno, se possivel nao mexam, nao sei como esta funcionando

    if opcao == 1:
        print(f'ALuno: {aluno_nome}')
        print('Digite 0 para voltar')

        opcao_diferente1 = int(input(f'{aluno_nome}, você deseja retornar?  '))
        if opcao_diferente1 == 0:
            continue

# acabou o aluno e começa a saida pq eu quero

    if opcao == 0:
        break

# agr a avaliação >:3

    if opcao == 2:
        print('Sentimos muito, essa opção esta indisponivel no momento')
        print('Pressione 0 para voltar')

        opcao_diferente1 = int(input(f'{aluno_nome}, você deseja retornar?  '))
        if opcao_diferente1 == 0:
            continue

# Boletim TwT

    if opcao == 3:
        print('Sentimos muito, essa opção esta indisponivel no momento ')
        print('Pressione 0 para voltar')
    

    opcao_diferente1 = int(input(f'{aluno_nome}, você deseja retornar? '))
    if opcao_diferente1 == 0:
        continue