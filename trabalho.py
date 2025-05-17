conjuntos = []

def menu(escolha):
    print('1. Criar conjunto')
    print('2. Adicionar numeros a um conjunto')
    print('3. Ver conjuntos')
    print('4. Remover conjuntos')
    print('5. Sair')
    escolha = input('Escolha uma opção: ')
    return escolha

def criar_conjunto():
    opcao = 's'
    while opcao == 's':
        nome_conjunto = input('Digite o nome do conjunto que deseja criar: ')
        verificacao = True
        for conjunto in conjuntos:
            if conjunto[0] == nome_conjunto:
                verificacao = False
        if verificacao == True:
            conjuntos.append([nome_conjunto, []])
            print(f'Conjunto "{nome_conjunto}" criado com sucesso!')
        else:
            print(f'Conjunto "{nome_conjunto}" já exite!')
        opcao = input('Deseja adicionar outro conjunto? [s/n]')
        print(conjuntos)

def add_numeros_no_conjunto():
    if conjuntos == []:
        print('Nenhum conjunto adicionado!')
    else:
        print('Conjuntos adicionados:')
        for nome_conjunto in conjuntos:
            print(f'Conjunto: {nome_conjunto[0]}')
            print('=-' * 20)
        escolha_conjunto = input('Escolha um conjunto para adicionar os números: ')
        verificao = False
        indice_conjunto = 0
        for nome_conjunto in conjuntos:
            if escolha_conjunto == nome_conjunto[0]:
                verificao = True
                break
            indice_conjunto += 1
        if verificao == True:
            opcao = 's'
            while opcao == 's':
                numero = int(input('Digite um número para adicionar: '))
                if numero in conjuntos[indice_conjunto][1]:
                    print(f'O número {numero} já está no conjunto {conjuntos[indice_conjunto][1]}!')
                else:
                    conjuntos[indice_conjunto][1].append(numero)
                opcao = input('Deseja adicionar mais números ao conjunto? [s/n]').lower()
        else:
            print(f'Conjunto "{escolha_conjunto}" não encontrado!')
        
def mostrar_conjuntos():
    if conjuntos == []:
        print('Nenhum conjunto adicionado!')
    else:
        for conjunto in conjuntos:
            print(conjunto)
            print('=-' * 20)

while True:
    esc = ''
    escolha = menu(esc)
    if escolha == '1':
        criar_conjunto()
        print(conjuntos)
    elif escolha == '2':
        add_numeros_no_conjunto()
    elif escolha == '3':
        mostrar_conjuntos()
    elif escolha == '5':
        print('Saindo do programa!')
        break
    else:
        print('Opção inválida!')
    