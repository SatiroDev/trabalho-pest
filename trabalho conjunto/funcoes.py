lista_conjuntos = []

def menu():
    print('1. Criar conjunto')
    print('2. Adicionar elemento (Em um conjunto ja existente!)')
    print('3.Remover elemento de um conjunto')
    print('4. Mostrar conjuntos')
    print('5. Apagar conjunto')
    print('6. União de conjuntos')
    print('7. Intersecção de conjuntos')

def criar_conjunto(conjuntos):
    nome_conjunto = input('Digite o nome do conjunto que deseja criar: ')
    elementos = []
    verificacao = True
    for conjs in conjuntos:
        if nome_conjunto in conjs:
            verificacao = False
    if verificacao == True:
        opcao = 's'
        while opcao != 'n':
            elemento = int(input('Digite um elemento'))
            if elemento not in elementos:
                elementos.append(elemento)
                print(f'Elemento "{elemento}" adicionado com sucesso!')
            else:
                print(f'Elemento "{elemento}" já está no conjunto!')
            opcao = input('Deseja adicionar mais elementos? [s/n] ').lower()
        return conjuntos.append([nome_conjunto, elementos])
    else:
        print(f'O nome "{nome_conjunto}" já está em uso!')


while True:
    menu()
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        funcao = criar_conjunto(lista_conjuntos)