import json
def carregar_agenda():
    with open ('agenda.json', 'r') as f:
        return json.load (f)
def menu():
    print('--- AGENDA DE CONTATOS ---')
    print('1. Adicionar contato')
    print('2. Buscar contato')
    print('3. Editar contato')
    print('4. Remover contato')
    print('5. Sair')
    opção = input('Opção: ')
    return opção
def adicionar_contato(agenda, usuario, nome, celular, email):
    pass
agenda = carregar_agenda()
while True:
    escolha = menu()
    if escolha == '1':
        usuario = input('Qual o nome do usuário (Utilize @ no começo. Ex: @gaguin)? ').lower()
        bolean = False
        if len(usuario) == 0:
            print('Não deixe em branco')
        elif usuario[0] == '@':
            if usuario in agenda:
                print('Usuário existente.')
            else:
                nome = input('Qual o seu nome? ').title()
                telefone = input('Qual o seu número de Telefone (Lembre-se de colocar o hífen. ex: xxxxx-xxxx)? ').strip()
                if len(telefone) == 10:
                    
                    contador = 0
                    contagem = 0
                    for numero in telefone:
                        if telefone[5] == '-':
                            if numero in '0123456789':
                                contagem += 1
                                if contagem == 9:
                                    bolean = True
                            continue
                else:
                    print('Você esqueceu de algo. verifique se tem "-" e se possui 9 número')
                if bolean == True:
                    email = input('Qual o seu email (ex: email@provedor.extensão)? ')
                    cont = email.count('@')
                    if cont > 1:
                        print('O seu email tem mais que um @. Digite novamente')
                    elif cont == 0:
                        print('Você esqueceu de colocar o @ no email.')
                    if email[-1] == '.':
                        print('Email inválido')
                else:
                    print('Número inválido!')
        else:
            print('Por favor, comece o nome do usuário com @')
    #     criar_conjunto()
    # elif escolha == '2':
    #     add_elemento_conjunto()
    # elif escolha == '3':
    #     remover_elemento_conjunto()
    # elif escolha == '4':
    #     mostrar_conjuntos()
    # elif escolha == '5':
    #     apagar_conjunto()
    # elif escolha == '6':
    #     uniao_conjuntos()
    # elif escolha == '7':
    #     intersecao_conjuntos()
    # elif escolha == '8':
    #     print('Fim do programa!')
    #     break
    # else:
    #     print('Opção inválida!')