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

while True:
    opcao = menu()
    if opcao == '1':
        print('ola')
    else:
        print('erro')