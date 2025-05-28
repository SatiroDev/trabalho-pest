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
    print('8. Sair do programa')
    print('_'*50)
    print()
    opcao = input('Escolha uma opção: ')
    return opcao

def criar_conjunto(): #Nesse def iremos dar o nome do conjunto e criar um conjunto 
    sub_elementos = []
    sub_nome = []
    escolha = 0
    nome_conjunto = input('Qual o nome do conjunto? ')
    sub_nome.append(nome_conjunto)
    print(f'Conjunto "{nome_conjunto}" adicionado com sucesso!')
    print()
    escolha = 0
    while escolha != 'n':
            elementos = int(input('Qual elemento você deseja adicionar: '))
            if elementos not in sub_elementos:
                sub_elementos.append(elementos)
                print('Elemento adicionado com sucesso!')
            else:
                print('Elemento repetido, por favor coloque outro!')
            escolha = input('Deseja adicionar mais elementos (s/n)? ') 
    sub_nome.append(sub_elementos)
    lista_conjuntos.append(sub_nome)

def add_elemento_conjunto(): #Nesse def iremos adicionar elementos a um conjunto existente
    boleano = False
    if len(lista_conjuntos) == 0:
        print('A lista de conjuntos está vazia. Adicione um conjunto primeiro!')
    else:
        nome = input('Qual o nome do conjunto? ')
        for conjunto in lista_conjuntos:
            if nome == conjunto[0]: 
                if nome in conjunto[0]:
                    escolha = 0
                    while escolha != 'n':
                        elemento = int(input('Qual o elemento deseja adicionar? ')) 
                        if elemento not in conjunto[1]:
                            conjunto[1].append(elemento)
                            print('Número adicionado com sucesso!')
                        else:
                            print('Número já existente')
                        escolha = input('Deseja adicionar mais elementos (s/n)? ')    
                boleano = True
    if boleano == False:
        print('Conjunto inexistente')

def remover_elemento_conjunto():
    if len(lista_conjuntos) == 0:
        print('A lista de conjuntos está vazia. Adicione um conjunto primeiro!')
    else:
        nome = input('Qual nome do conjunto? ')
        for conjunto in lista_conjuntos:
            if nome == conjunto[0]:
                escolha = 0
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
    for conjunto in lista_conjuntos:
        for elementos in range(0, len(conjunto)):
            print(f'Os elementos do {conjunto[0]} são: {lista_conjuntos[conjunto][elementos]}')
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