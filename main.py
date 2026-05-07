aluno_nome = input('Digite seu nome: ').lower()



while True:
    print('Analisador-de-Desempenho-Escolar-Boletim-Digital')

    print('1. Alunos')
    
    print('2. Avaliações')

    print('3. Boletim')

    print('Sair')

    opcao = int(input(f'Olá, {aluno_nome} escolha a opção desejada: '))

# aluno, se possivel nao mexam, nao sei como esta funcionando

    if opcao == 1:
        print(f'ALuno: {aluno_nome}')
        print('digite 0 para voltar')

        opcao_diferente1 = int(input(f'{aluno_nome}, você deseja retornar?  '))
        if opcao_diferente1 == 0:
            continue

# acabou o aluno e começa a avaliação

