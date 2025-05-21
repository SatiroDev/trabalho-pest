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
    print('=-'*25)
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
        print('=-'*25)
        return conjuntos.append([nome_conjunto, elementos])
    else: # se o nome já estiver em uso
        print(f'O nome "{nome_conjunto}" já está em uso!')
    print('=-'*25)

def add_elemento_conjunto(conjuntos):
    print('=-'*25)
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
                opcao = 's'
                while opcao != 'n':
                    elemento = int(input('Digite um elemento: '))
                    if elemento not in conjunto[1]:
                        conjunto[1].append(elemento)
                        print(f'Elemento "{elemento}" adicionado com sucesso!')
                    else:
                        print(f'Elemento "{elemento}" já está no conjunto!')
                    print('=-'*25)
                    opcao = input('Deseja adicionar mais elementos? [s/n] ').lower()
        if verificacao == False:
            print(f'O nome "{nome_conjunto}" não existe')
    print('=-'*25)

def remover_elemento(conjuntos):
    print('=-'*25)
    if conjuntos == []:
        print('Lista de conjunto está vazia!')
    else:
        print('Conjuntos existentes:')
        for conjunto in conjuntos:
            print(conjunto)
        nome_conjunto = input('Escolha o nome do conjunto no qual deseja remover elementos: ')
        verificacao = False
        for conjunto in conjuntos:
            if nome_conjunto in conjunto[0]:
                verificacao = True
                opcao = 's'
                while opcao != 'n':
                    elemento = int(input('Digite um elemento que deseja remover: '))
                    if elemento in conjunto[1]:
                        conjunto[1].remove(elemento)
                        print(f'Elemento "{elemento}" removido com sucesso!')
                    else:
                        print(f'Elemento "{elemento}" não está no conjunto!')
                    if conjunto[1] == []:
                        print(f'Conjunto {conjunto[0]} não contem mais elementos!')
                        break
                    print('=-'*25)
                    opcao = input('Deseja remover mais elementos? [s/n] ').lower()
        if verificacao == False:
            print(f'O nome "{nome_conjunto}" não existe')
    print('=-'*25)

def mostrar_conjunto(conjuntos):
    print('=-'*25)
    if conjuntos == []:
        print('Lista de conjunto está vazia!')
    else:
        for conjunto in conjuntos:
            print(f'Conjunto: {conjunto[0]}')
            if conjunto[1] != []:
                print(f'Elementos: {conjunto[1]}')
            else:
                print(f'Conjunto "{conjunto[0]}" não tem elementos adicionados!')
            print()
    print('=-'*25)

def apagar_conjunto(conjuntos):
    print('=-'*25)
    if conjuntos == []:
        print('Lista de conjunto está vazia!')
    else:
        opcao = 's'
        while opcao != 'n':
            for conjunto in conjuntos:
                print(conjunto)
            nome_conjunto = input('Digite o nome do conjunto no qual você deseja remover: ')
            verificacao = False
            print()
            for conjunto in conjuntos:
                if nome_conjunto in conjunto:
                    conjuntos.remove(conjunto)
                    print(f'Conjunto "{nome_conjunto}" removido com sucesso!')
                    verificacao = True
            if verificacao == False:
                print(f'Conjunto "{nome_conjunto}" não existe!')

            opcao = input('Deseja apagar mais conjuntos? [s/n] ').lower()

    print('=-'*25)

while True:
    menu()
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        criar_conjunto(lista_conjuntos)
    elif escolha == '2':
        add_elemento_conjunto(lista_conjuntos)
    elif escolha == '3':
        remover_elemento(lista_conjuntos)
    elif escolha == '4':
        mostrar_conjunto(lista_conjuntos)
    elif escolha == '5':
        apagar_conjunto(lista_conjuntos)
