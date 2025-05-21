lista_conjuntos = []

def menu():
    print('_'*23,end='MENU')
    print('_'*23)
    print('1. Criar conjunto')
    print('2. Adicionar elemento (Em um conjunto ja existente!)')
    print('3. Remover elemento de um conjunto')
    print('4. Mostrar conjuntos')
    print('5. Apagar conjunto')
    print('6. União de conjuntos')
    print('7. Intersecção de conjuntos')
    print('_'*50)
    print()
def criar_conjunto(conjuntos):
    nome_conjunto = input('Digite o nome do conjunto que deseja criar: ')
    elementos = []
    verificacao = True
    for conjs in conjuntos:
        if nome_conjunto in conjs: # verifica se o nome escolhido já existe nas sublistas
            verificacao = False 
            break
    if verificacao == True: # se o nome ainda não estiver em uso
        opcao = 's'
        while opcao != 'n':
            elemento = int(input('Digite um elemento: '))
            if elemento not in elementos:
                elementos.append(elemento)
                print(f'Elemento "{elemento}" adicionado com sucesso!')
            else:
                print(f'Elemento "{elemento}" já está no conjunto!')
            opcao = input('Deseja adicionar mais elementos? [s/n] ').lower()
        return conjuntos.append([nome_conjunto, elementos])
    else: # se o nome já estiver em uso
        print(f'O nome "{nome_conjunto}" já está em uso!')

def add_elemento_conjunto(conjuntos):
    if conjuntos == []:
        print('Lista de conjunto está vazia!')
    else:
        print('Conjuntos existentes:')
        for conjunto in conjuntos:
            print(conjunto)
        nome_conjunto = input('Escolha o nome do conjunto no qual deseja adicionar elementos: ')
        verificacao = False
        for conjunto in conjuntos:
            if nome_conjunto in conjunto[0]:
                verificacao = True
                elementos = []
                opcao = 's'
                while opcao != 'n':
                    elemento = int(input('Digite um elemento: '))
                    if elemento not in conjunto[1]:
                        conjunto[1].append(elemento)
                        print(f'Elemento "{elemento}" adicionado com sucesso!')
                    else:
                        print(f'Elemento "{elemento}" já está no conjunto!')
                    opcao = input('Deseja adicionar mais elementos? [s/n] ').lower()
        if verificacao == False:
            print(f'O nome "{nome_conjunto}" não existe')
    print('=-'*25)

while True:
    menu()
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        funcao = criar_conjunto(lista_conjuntos)
    elif escolha == '2':
        add_elemento_conjunto(lista_conjuntos)
