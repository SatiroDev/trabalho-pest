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

def criar_conjunto(conjuntos): # função para criar um novo conjunto
    print('=-'*25)
    nome_conjunto = input('Digite o nome do conjunto que deseja criar: ')
    elementos = []
    verificacao = True
    for conjunto in conjuntos:
        if nome_conjunto in conjunto: # verifica se o nome escolhido já existe nas sublistas
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

def add_elemento_conjunto(conjuntos): # função para adicionar elementos a uma lista ja existente
    print('=-'*25)
    if conjuntos == []: # verifica se a lista está vazia
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
    if conjuntos == []: # verifica se a lista está vazia
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
                    opcao = input('Deseja remover outro elemento? [s/n] ').lower()
        if verificacao == False:
            print(f'O nome "{nome_conjunto}" não existe')
    print('=-'*25)

def mostrar_conjunto(conjuntos):
    print('=-'*25)
    if conjuntos == []: # verifica se a lista está vazia
        print('Lista de conjunto está vazia!')
    else:
        print('Conjuntos existentes:')
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
    if conjuntos == []: # verifica se a lista está vazia
        print('Lista de conjunto está vazia!')
    else:
        print('Conjuntos existentes:')
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
            if conjuntos != []:
                opcao = input('Deseja apagar outro conjunto? [s/n] ').lower()
            else:
                break
    print('=-'*25)

def uniao_conjuntos(conjuntos): # função para mostrar a união entre 2 conjuntos
    if conjuntos == []: # verifica se a lista está vazia
        print('Lista de conjunto está vazia!')
    elif len(conjuntos) <= 1: # verifica se na lista principal tem apenas um conjunto adicionado
        print('A lista de conjuntos tem que conter pelo menos 2 conjuntos!')   
    else:
        print('Conjuntos existentes:')
        nomes_conjuntos = [] # lista para armazenar os nomes dos conjuntos (para melhor a verificação posteriormente)
        for conjunto in conjuntos:
            print(conjunto)
            nomes_conjuntos.append(conjunto[0]) # adiciona o nome do conjunto
        print('Digite dois de conjuntos para ver a união deles')
        nome_primeiro_conjunto = input('Nome do primeiro conjunto: ')
        if nome_primeiro_conjunto in nomes_conjuntos:
            nome_segundo_conjunto = input('Nome do segundo conjunto: ')
            if nome_segundo_conjunto == nome_primeiro_conjunto: # verifica se o usuário repetiu o nome do conjunto
                print('Não pode repetir o nome do conjunto escolhido anteriormente!')
            elif nome_segundo_conjunto in nomes_conjuntos:
                uniao = []
                todos_conjuntos = []
                nome_conjunto = nome_primeiro_conjunto # variável para ajudar na verificação posteriormente
                for i in range(0, len(conjuntos)): # loop irá rodar de acordo com a quantidade de conjuntos presentes na lista principal
                    for conjunto in conjuntos:
                        if nome_conjunto == conjunto[0] and nome_conjunto == nome_primeiro_conjunto: # verifica se o nome que usuário digitou está na lista e se é igual ao primeiro nome 
                            todos_conjuntos.append(conjunto[1]) # adiciona todos os elementos de um conjunto 
                            for elementos in conjunto[1]:
                                uniao.append(elementos) # adiciona elementos a lista 'uniao' 
                        if i == 1 and nome_conjunto == conjunto[0]:
                            todos_conjuntos.append(conjunto[1])
                            for elementos in conjunto[1]:
                                if elementos not in uniao:
                                    uniao.append(elementos)
                    nome_conjunto = nome_segundo_conjunto
                cont = 0
                for nome_conj in nomes_conjuntos:
                    print()
                    print(f'Conjunto "{nome_conj}": {todos_conjuntos[cont]}')
                    cont += 1
                print()
                print(f'União:',end=' ')
                uniao.sort()
                print(uniao)
            else:
                print(f'Conjunto "{nome_segundo_conjunto}" não escontrado')
        else:
            print(f'Conjunto "{nome_primeiro_conjunto}" não escontrado')

def interseccao_conjuntos(conjuntos):
    if conjuntos == []: # verifica se a lista está vazia
        print('Lista de conjunto está vazia!')
    elif len(conjuntos) <= 1: # verifica se na lista principal tem apenas um conjunto adicionado
        print('A lista de conjuntos tem que conter pelo menos 2 conjuntos!')   
    else:
        print('Conjuntos existentes:')
        nomes_conjuntos = [] # lista para armazenar os nomes dos conjuntos (para melhor a verificação posteriormente)
        for conjunto in conjuntos:
            print(conjunto)
            nomes_conjuntos.append(conjunto[0]) # adiciona o nome do conjunto
        print('Digite dois de conjuntos para ver a união deles')
        nome_primeiro_conjunto = input('Nome do primeiro conjunto: ')
        if nome_primeiro_conjunto in nomes_conjuntos:
            nome_segundo_conjunto = input('Nome do segundo conjunto: ')
            if nome_segundo_conjunto == nome_primeiro_conjunto: # verifica se o usuário repetiu o nome do conjunto
                print('Não pode repetir o nome do conjunto escolhido anteriormente!')
            elif nome_segundo_conjunto in nomes_conjuntos:
                interseccao = []
                todos_conjuntos = []
                nome_conjunto = nome_primeiro_conjunto # variável para ajudar na verificação posteriormente
                for i in range(0, len(conjuntos)): # loop irá rodar de acordo com a quantidade de conjuntos presentes na lista principal
                    for conjunto in conjuntos:
                        if nome_conjunto == conjunto[0] and nome_conjunto == nome_primeiro_conjunto: # verifica se o nome que usuário digitou está na lista e se é igual ao primeiro nome 
                            todos_conjuntos.append(conjunto[1]) # adiciona todos os elementos de um conjunto 
                            for elementos in conjunto[1]:
                                interseccao.append(elementos) # adiciona elementos a lista 'interseccao' 
                        if i == 1 and nome_conjunto == conjunto[0]:
                            todos_conjuntos.append(conjunto[1])
                            for elementos in conjunto[1]:
                                if elementos in todos_conjuntos[0]:
                                    interseccao.append(elementos)
                    nome_conjunto = nome_segundo_conjunto
                    
                cont = 0
                for nome_conj in nomes_conjuntos:
                    print()
                    print(f'Conjunto "{nome_conj}": {todos_conjuntos[cont]}')
                    cont += 1
                print()
                print(f'União:',end=' ')
                interseccao.sort()
                print(interseccao)
            else:
                print(f'Conjunto "{nome_segundo_conjunto}" não escontrado')
        else:
            print(f'Conjunto "{nome_primeiro_conjunto}" não escontrado')

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
    elif escolha == '6':
        uniao_conjuntos(lista_conjuntos)
