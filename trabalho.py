conjuntos = []

def menu(escolha):
    print('1. Criar conjunto')
    print('2. Adicionar numeros a um conjunto')
    print('3. Ver conjuntos')
    print('4. Remover conjuntos')
    print('5. Sair')
    escolha = input('Escolha uma opção: ')
    return escolha

def criar_conjunto(lista_conjuntos: list):
    opcao = 's'
    while opcao == 's':
        nome_conjunto = input('Digite o nome do conjunto que deseja criar: ')
        if nome_conjunto not in lista_conjuntos:
            lista_conjuntos.append([nome_conjunto])
            print(f'Conjunto "{nome_conjunto}" criado com sucesso!')
        else:
            print(f'Conjunto "{nome_conjunto}" já exite!')
        opcao = input('Deseja adicionar outro conjunto? [s/n]')
    return lista_conjuntos


while True:
    esc = ''
    escolha = menu(esc)
    if escolha == '1':
        criar_conjunto(conjuntos)
        print(conjuntos)
    elif escolha == '5':
        print('Saindo do programa!')
        break
    else:
        print('Opção inválida!')
    