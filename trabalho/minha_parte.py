lista_conjuntos = []

def menu():
    print(f"{'_'*23}MENU{'_'*23}")
    print('1. Criar conjunto')
    print('2. Adicionar elemento (Em um conjunto ja existente!)')
    print('3. Remover elemento de um conjunto')
    print('4. Mostrar conjuntos')
    print('5. Apagar conjunto')
    print('6. União de conjuntos')
    print('7. Intersecção de conjuntos')
    print('8. Sair do programa')
    print('_'*50)
    print()
    opcao = input('Escolha uma opção: ')
    return opcao

def criar_conjunto(): # Função para criar um conjunto                                                
    elementos = [] 
    conjunto_elementos = []
    nome_conjunto = input('Qual o nome do conjunto? ')
    boleano = False
    for conjunto in lista_conjuntos: # loop que vai verificar se o nome do conjunto escolhido pelo usuário já foi adicionado antes
        if nome_conjunto == conjunto[0]: # se o nome do conjunto for igual a algum nome de conjunto já adicionado
            boleano = True
            break
    print()
    print('-=' * 25)
    print()
    if boleano == True: # se o nome do conjunto já estiver sido adicionado
        print(f'Conjunto com o nome "{nome_conjunto}" já existe!')
    else: # se o nome do conjunto não estiver sido adicionado
        conjunto_elementos.append(nome_conjunto)
        print(f'Conjunto "{nome_conjunto}" adicionado com sucesso!')
        print()
        escolha = 's'
        while escolha != 'n':
                elemento = int(input('Qual elemento você deseja adicionar: '))
                if elemento not in elementos: # se o elemento não estiver sido adicionado antes 
                    elementos.append(elemento) # adiciona o elemento a lista 'elementos'
                    print(f'Elemento "{elemento}" adicionado com sucesso!')
                else: # se o elemento já estiver sido adicionado antes
                    print(f'Elemento "{elemento}" repetido!')
                print()
                escolha = input('Deseja adicionar outro elemento (s/n)? ') 
        conjunto_elementos.append(elementos) # adiciona a lista 'elementos' em 'conjunto_elementos' 
        lista_conjuntos.append(conjunto_elementos) # adiciona a lista 'conjunto_elementos' em 'lista_conjuntos' -> (lista principal)
    print()
    print('-=' * 25)

def add_elemento_conjunto(): # Função para adicionar elementos a um conjunto existente
    print()
    print('-=' * 25)
    print()
    if len(lista_conjuntos) == 0: # se a lista principal estiver vazia, ou seja, sem nenhum conjunto adicionado
        print('A lista de conjuntos está vazia. Adicione um conjunto primeiro!')
    else: # se a lista principal não estiver vazia
        
        boleano = False
        nome_conjunto = input('Qual o nome do conjunto? ')
        for conjunto in lista_conjuntos:
            if nome_conjunto == conjunto[0]: # verifica se o nome do conjunto escolhido pelo usuário é igual a algum nome de conjunto que está adicionado a lista principal
                escolha = 's'
                while escolha != 'n':
                    elemento = int(input('Qual o elemento deseja adicionar? ')) 
                    if elemento not in conjunto[1]: # se o elemento não estiver adicionado 
                        conjunto[1].append(elemento)
                        print(f'Elemento "{elemento}" adicionado com sucesso!')
                    else: # se o elemento já estiver adicionado
                        print(f'Elemento "{elemento}" já existente!')
                    print()
                    escolha = input('Deseja adicionar outro elemento (s/n)? ')    
                boleano = True
        if boleano == False: # se o nome do conjunto escolhido pelo usuário não for achado dentro da lista principal
            print(f'Conjunto "{nome_conjunto}" inexistente!')
    print()
    print('-=' * 25)

def remover_elemento_conjunto():
    print()
    print('-=' * 25)
    print()
    if len(lista_conjuntos) == 0: # se a lista principal estiver vazia, ou seja, sem nenhum conjunto adicionado
        print('A lista de conjuntos está vazia. Adicione um conjunto primeiro!')
    else: # se a lista principal não estiver vazia
        boleano = False
        nome_conjunto = input('Qual nome do conjunto? ')
        for conjunto in lista_conjuntos:
            if nome_conjunto == conjunto[0]: # verifica se o nome do conjunto escolhido pelo usuário é igual a algum nome de conjunto que está adicionado a lista principal
                boleano = True
                escolha = 's'
                while escolha != 'n':
                    remover = int(input('Qual elemento você deseja remover? '))
                    if remover in conjunto[1]: # se o elemento estiver na sub lista dos elementos do conjunto escolhido
                        conjunto[1].remove(remover)
                        print(f'Elemento "{remover}" removido com sucesso!')
                    else: # se o elemento não estiver na sub lista dos elementos do conjunto escolhido
                        print(f'Elemento {remover}" não encontrado!')
                    print()
                    escolha = input('Deseja remover outro elemento (s/n)? ')
        if boleano == False: # se o nome do conjunto escolhido pelo usuário não for achado dentro da lista principal
            print(f'Conjunto "{nome_conjunto}" inexistente!')   
    print()
    print('-=' * 25) 

def mostrar_conjuntos():
    print()
    print('-=' * 25)
    print()
    if len(lista_conjuntos) == 0: # se a lista principal estiver vazia, ou seja, sem nenhum conjunto adicionado
        print('A lista de conjuntos está vazia. Adicione um conjunto primeiro!')
        print()
    else: # se a lista principal não estiver vazia
        print('Conjuntos existentes:')
        for conjunto in lista_conjuntos: # loop para mostrar os conjuntos e seu elementos 
            print(f'Conjunto: {conjunto[0]}')
            print(f'Elementos: {conjunto[1]}')
            print()
    print('-=' * 25)

def apagar_conjunto():
    print()
    print('-=' * 25)
    print()
    boleano = False
    if len(lista_conjuntos) == 0: # se a lista principal estiver vazia, ou seja, sem nenhum conjunto adicionado
        print('A lista de conjuntos está vazia. Adicione um conjunto primeiro!')
    else: # se a lista principal não estiver vazia
        nome_conjunto = input('Qual conjunto deseja apagar? ')
        for conjunto in lista_conjuntos:
            if conjunto[0] == nome_conjunto: # verifica se o nome do conjunto escolhido pelo usuário é igual a algum nome de conjunto que está adicionado a lista principal
                boleano = True
                lista_conjuntos.remove(conjunto)
                print(f'Conjunto "{nome_conjunto}" removido com sucesso!')
        if boleano == False: # se o nome do conjunto escolhido pelo usuário não for achado dentro da lista principal
            print(f'Conjunto "{nome_conjunto}" não encontrado!')
    print()
    print('-=' * 25) 

def uniao_conjuntos(): # função para mostrar a união entre 2 conjuntos
    print()
    print('-=' * 25)
    print()
    if len(lista_conjuntos) == 0: # verifica se a lista está vazia
        print('Lista de conjunto está vazia!')
    elif len(lista_conjuntos) <= 1: # verifica se na lista principal tem apenas um ou menos conjuntos adicionado
        print('A lista de conjuntos tem que conter pelo menos 2 conjuntos!')   
    else:
        print('Conjuntos existentes:')
        nomes_conjuntos = [] # lista para armazenar os nomes dos conjuntos (para melhorar a verificação posteriormente)
        for conjunto in lista_conjuntos:
            print(conjunto)
            nomes_conjuntos.append(conjunto[0]) # adiciona o nome do conjunto à lista 'nomes_conjuntos'
        print('Digite dois de conjuntos para ver a união deles')
        nome_primeiro_conjunto = input('Nome do primeiro conjunto: ')
        if nome_primeiro_conjunto in nomes_conjuntos: # se o primeiro nome do conjunto que o usuário escolheu tiver dentro da lista 'nomes_conjuntos'
            nome_segundo_conjunto = input('Nome do segundo conjunto: ')
            if nome_segundo_conjunto == nome_primeiro_conjunto: # verifica se o usuário repetiu o nome do conjunto
                print('Não pode repetir o nome do conjunto escolhido anteriormente!')
            elif nome_segundo_conjunto in nomes_conjuntos: # se o segundo nome do conjunto que o usuário escolheu tiver dentro da lista 'nomes_conjuntos'
                uniao = []
                conjuntos_elementos = []

                for conjunto in lista_conjuntos:
                    if conjunto[0] == nome_primeiro_conjunto: # verifica se o nome que usuário digitou está na lista e se é igual ao primeiro nome do conjunto que o usuário escolheu
                        conjuntos_elementos.append([nome_primeiro_conjunto,conjunto[1]]) 
                        for elemento in conjunto[1]:
                            if elemento not in uniao: # se o elemento não tiver na lista 'uniao'
                                uniao.append(elemento) 
                        

                    if conjunto[0] == nome_segundo_conjunto: # verifica se o nome que usuário digitou está na lista e se é igual ao segundo nome do conjunto que o usuário escolheu
                        conjuntos_elementos.append([nome_segundo_conjunto,conjunto[1]])
                        for elemento in conjunto[1]:
                            if elemento not in uniao: # se o elemento não tiver na lista 'uniao'
                                uniao.append(elemento)
                for conjunto in conjuntos_elementos:
                    print()     
                    print(f'Conjunto "{conjunto[0]}": {conjunto[1]}')
                print()
                uniao.sort()
                print(f'União: {uniao}')
            else:
                print(f'Conjunto "{nome_segundo_conjunto}" não escontrado')
        else:
            print(f'Conjunto "{nome_primeiro_conjunto}" não escontrado')
    print()
    print('-=' * 25) 

def intersecao_conjuntos():
    print()
    print('-=' * 25)
    print()
    if len(lista_conjuntos) == 0: # verifica se a lista está vazia
        print('Lista de conjunto está vazia!')
    elif len(lista_conjuntos) <= 1: # verifica se na lista principal tem apenas um ou menos conjuntos adicionado
        print('A lista de conjuntos tem que conter pelo menos 2 conjuntos!')   
    else:
        print('Conjuntos existentes:')
        nomes_conjuntos = [] # lista para armazenar os nomes dos conjuntos (para melhorar a verificação posteriormente)
        for conjunto in lista_conjuntos:
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
                conjuntos_elementos = []
                verificar = 0
                for conjunto in lista_conjuntos:
                    if conjunto[0] == nome_primeiro_conjunto: # verifica se o nome que usuário digitou está na lista e se é igual ao primeiro nome 
                        conjuntos_elementos.append([nome_primeiro_conjunto, conjunto[1]]) 
                        if verificar == 0:
                            verificar = conjunto[1]
                        else:
                            for elementos in conjunto[1]:
                                if elementos in verificar:
                                    interseccao.append(elementos) # adiciona elementos a lista 'interseccao' 
                    if nome_segundo_conjunto == conjunto[0]:
                        conjuntos_elementos.append([nome_segundo_conjunto, conjunto[1]])
                        if verificar == 0:
                            verificar = conjunto[1]
                        else:
                            for elementos in conjunto[1]:
                                if elementos in verificar:
                                    interseccao.append(elementos) # adiciona elementos a lista 'interseccao' 
                for conjunto in conjuntos_elementos:
                    print()     
                    print(f'Conjunto "{conjunto[0]}": {conjunto[1]}')
                print()
                interseccao.sort()
                print(f'Intersecção: {interseccao}')

            else:
                print(f'Conjunto "{nome_segundo_conjunto}" não escontrado')
        else:
            print(f'Conjunto "{nome_primeiro_conjunto}" não escontrado')
    print()
    print('-=' * 25) 

while True:
    escolha = menu()
    if escolha == '1':
        criar_conjunto()
    elif escolha == '2':
        add_elemento_conjunto()
    elif escolha == '3':
        remover_elemento_conjunto()
    elif escolha == '4':
        mostrar_conjuntos()
    elif escolha == '5':
        apagar_conjunto()
    elif escolha == '6':
        uniao_conjuntos()
    elif escolha == '7':
        intersecao_conjuntos()
    elif escolha == '8':
        print('Fim do programa!')
        break
    else:
        print('Opção inválida!')