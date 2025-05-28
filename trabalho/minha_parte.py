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

def criar_conjunto(): # Nesse def iremos dar o nome do conjunto e criar um conjunto 
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
    if boleano == True: # se o nome já estiver sido adicionado
        print(f'Conjunto com o nome "{nome_conjunto}" já existe')
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
                    print(f'Elemento "{elemento}" repetido')
                print()
                escolha = input('Deseja adicionar outro elemento (s/n)? ') 
        conjunto_elementos.append(elementos) # adiciona a lista 'elementos' em 'conjunto_elementos' 
        lista_conjuntos.append(conjunto_elementos) # adiciona a lista 'conjunto_elementos' em 'lista_conjuntos' -> (lista principal)
    print()
    print('-=' * 25)

def add_elemento_conjunto(): # Nesse def iremos adicionar elementos a um conjunto existente
    if len(lista_conjuntos) == 0: # se a lista principal estiver vazia, ou seja, sem nenhum conjunto adicionado
        print('A lista de conjuntos está vazia. Adicione um conjunto primeiro!')
    else: # se a lista principal não estiver vazia
        boleano = False
        nome_conjunto = input('Qual o nome do conjunto? ')
        for conjunto in lista_conjuntos:
            if nome_conjunto == conjunto[0]: # verifica se o nome é igual a algum nome de conjunto que está adicionado a lista principal
                escolha = 's'
                while escolha != 'n':
                    elemento = int(input('Qual o elemento deseja adicionar? ')) 
                    if elemento not in conjunto[1]: # se o elemento não estiver adicionado 
                        conjunto[1].append(elemento)
                        print(f'Elemento "{elemento}" adicionado com sucesso!')
                    else: # se o elemento já estiver adicionado
                        print(f'Elemento "{elemento}" já existente')
                    escolha = input('Deseja adicionar outro elemento (s/n)? ')    
                boleano = True
        if boleano == False: # se o nome não for achado dentro da lista principal
            print(f'Conjunto "{nome_conjunto}" inexistente')

def remover_elemento_conjunto():
    if len(lista_conjuntos) == 0: # se a lista principal estiver vazia, ou seja, sem nenhum conjunto adicionado
        print('A lista de conjuntos está vazia. Adicione um conjunto primeiro!')
    else: # se a lista principal não estiver vazia
        nome_conjunto = input('Qual nome do conjunto? ')
        for conjunto in lista_conjuntos:
            if nome_conjunto == conjunto[0]:
                escolha = 's'
                while escolha != 'n':
                    remover = int(input('Qual elemento você deseja remover? '))
                    if remover in conjunto[1]:
                        conjunto[1].remove(remover)
                        print('Número removido com sucesso!')
                    else:
                        print('Elemento não encontrado')
                    escolha = input('Deseja remover mais elementos (s/n)? ')
            else:
                print('Elemento inexistente')    

def mostrar_conjuntos():
    if len(lista_conjuntos) == 0: # se a lista principal estiver vazia, ou seja, sem nenhum conjunto adicionado
        print('A lista de conjuntos está vazia. Adicione um conjunto primeiro!')
    else: # se a lista principal não estiver vazia
        print('Conjuntos existentes:')
        for conjunto in lista_conjuntos:
            print(f'Conjunto: {conjunto[0]}')
            print(f'Elementos: {conjunto[1]}')
            print()

def apagar_conjunto():
    boleano = False
    if len(lista_conjuntos) == 0:
        print('A lista de conjuntos está vazia. Adicione um conjunto primeiro!')
    else:
        nome_conjunto = input('Qual conjunto deseja apagar? ')
        for conjunto in lista_conjuntos:
            if conjunto[0] == nome_conjunto:
                boleano = True
                lista_conjuntos.remove(conjunto)
                print('Conjunto removido com sucesso!')
    if boleano == False:
        print('Conjunto não encontrado!')
def uniao_conjuntos():
    lista_uniao = [] 
    boleano = True
    conjunto1 = input('Qual o primeiro conjunto para fazer a união? ')
    for conjunto in lista_conjuntos:
        if conjunto1 in conjunto[0]:
            conjunto2 = input('Qual o segundo conjunto para fazer a união? ')
            if conjunto2 in conjunto[0]:
                for conjuntox in lista_conjuntos:
                    if conjuntox[0] == conjunto1:
                        for numero in conjuntox[1]:
                            lista_uniao.append(numero)
                    if conjuntox[0] == conjunto2:
                        for numero in conjuntox[1]:
                            lista_uniao.append(numero)
        elif conjunto1 not in conjunto[0]:
            boleano = False
    if boleano == False:
        print('Conjunto inexistente')
    elif boleano == True:    
        cp_lista_uniao = lista_uniao
        for elemento_fixo in cp_lista_uniao:
           cont = 0
           for elementos_lista in lista_uniao:
               if elemento_fixo == elementos_lista:
                   cont += 1
                   if cont >= 2:
                       lista_uniao.remove(elemento_fixo)
    print(lista_uniao)
def intersecao_conjuntos():
    lista_intersecao = [] 
    conjunto1 = input('Qual o primeiro conjunto para fazer a interseção? ')
    for conjunto in lista_conjuntos:
        if conjunto1 in conjunto[0]:
            conjunto2 = input('Qual o segundo conjunto para fazer a interseção? ')
        if conjunto2 in conjunto[0]:
            for conjuntox in lista_conjuntos:
                if conjuntox[0] == conjunto1:
                    for numero in conjuntox[1]:
                        lista_intersecao.append(numero)
                if conjuntox[0] == conjunto2:
                     for numero in conjuntox[1]:
                        lista_intersecao.append(numero)
        else:
            print('Conjunto inexistente')
        cp_lista_uniao = lista_intersecao
        for elemento_fixo in cp_lista_uniao:
           for elementos_lista in lista_intersecao:
               if elemento_fixo != elementos_lista:
                   lista_intersecao.remove(elemento_fixo)
    print(lista_intersecao)

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