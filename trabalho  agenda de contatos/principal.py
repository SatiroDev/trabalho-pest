import json

def menu():
    print('-=-' * 20)
    print('--- AGENDA DE CONTATOS ---')
    print('1. Adicionar contato')
    print('2. Buscar contato')
    print('3. Editar contato')
    print('4. Remover contato')
    print('5. Sair')
    opcao = input('Escolha uma opção: [1,2,3,4,5] ')
    print('-=-' * 20)
    return opcao

def menu_edicao():
    print('-=-' * 20)
    print('O que deseja editar? ')
    print('1. Nome')
    print('2. Número')
    print('3. Email')
    opcao = input('Escolha uma opção: [1,2,3] ').lower()
    print('-=-' * 20)
    print()
    return opcao

def mostrar_contatos():
    print('-=-' * 20)
    print('Usuários adicionados: ')
    cont = 1
    for nome_user in agenda.keys():
        print(f'{cont}- {nome_user}')
        cont += 1
    print('-=-' * 20)
    print()

def adicionar_contato(agenda, usuario, nome, celular, email):
    print('-=-' * 20)
    agenda[usuario] = [nome, celular, email]
    salvar_agenda(agenda)
    print('Contato salvo com sucesso!')
    print('-=-' * 20)
    print()

def buscar_contato(agenda, usuario):
    print('-=-' * 20)
    if usuario in agenda.keys():
        print()
        print(f'Informações do(a) usuário(a) "{usuario}": ')
        print(f'Nome: {agenda[usuario][0]}')
        print(f'Número: {agenda[usuario][1]}')
        print(f'Email: {agenda[usuario][2]}')

    else:
        print(f'Usuário "{usuario}" não encontrado!')
    print('-=-' * 20)
    print()

def editar_contato(agenda, usuario, campo, novo_valor):
    print('-=-' * 20)
    if campo == '1':
        nome_campo = 'nome'

        if usuario in agenda.keys():
            agenda[usuario][0] = novo_valor
        
    elif campo == '2':
        nome_campo = 'número'

        if usuario in agenda.keys():
            agenda[usuario][1] = novo_valor
        
    else:
        nome_campo = 'email'

        if usuario in agenda.keys():
            agenda[usuario][2] = novo_valor

    print(f'Novo {nome_campo} salvo com sucesso!')
    salvar_agenda(agenda)
    print('-=-' * 20)
    print()

def remover_contato(agenda, usuario):
    print('-=-' * 20)
    if usuario in agenda.keys():
        del agenda[usuario]
        print(f'Usuário "{usuario}" removido com sucesso!')
        salvar_agenda(agenda)

    else:
        print(f'Usuário "{usuario}" não encontrado!')
    print('-=-' * 20)
    print()

def salvar_agenda(agenda):

    with open('contatos.json', 'w') as f:
        json.dump(agenda, f)

def carregar_agenda():
    if 'contatos.json':
        with open('contatos.json', 'r') as f:
            return json.load(f)
        
    else:
        return {}

agenda = carregar_agenda()

while True:

    opcao = menu()

    if opcao == '1':
        usuario = input('Digite o nome de usuário: ').lower()
        verificacao_geral = False

        if usuario[0] == '@':
            nome = input('Digite o nome do contato: ')
            numero = input('Digite o número: (ex: 99999-9999) ')
            verificacao = True
            contagem = 0

            if len(numero) == 10:

                for num in numero:
                    contagem += 1

                    if num in '0123456789' and numero[5] == '-':

                        if contagem == 10:
                            verificacao_geral = True
                        continue

                    else:
                        print('Número inválido!')
                        print('Você pode ter digitado letras sem querer, ou esqueceu do "-"!')
                        verificacao = False
                        break

                if verificacao_geral == True:
                    email = input('Digite o email do contato: ').lower()

                    if len(email) > 10 and email[-10:] == '@gmail.com' or email[-12:] == '@outlook.com':
                        adicionar_contato(agenda, usuario, nome, numero, email)

                    else:
                        print('Erro! Email não aceito!')

            else:
                print('O número tem que seguir esse padrão -> 99999-9999')

        else:
            print('O usuário precisa começar com o "@"!')


    elif opcao == '2':
        if len(agenda) >= 1:
            mostrar_contatos()
            usuario = input('Digite o @ do usuário que deseja buscar informações: ').lower()
            buscar_contato(agenda, usuario)

        else:
            print('Adicione pelo menos um contato para fazer uma busca!')

    elif opcao == '3':

        if len(agenda) >= 1:

            mostrar_contatos()

            usuario = input('Digite o seu nome de usuário: ').lower()
            if usuario in agenda.keys():
                verificacao = True
                opcao_edicao = menu_edicao()

                if opcao_edicao == '1':
                    novo_nome = input('Digite o novo nome: ')
                    editar_contato(agenda, usuario, opcao_edicao, novo_nome)

                elif opcao_edicao == '2':
                    novo_numero = input('Digite o novo número: (ex: 99999-9999) ')
                    verificacao_geral = False
                    verificacao = True
                    verificacao_traco = False
                    contagem = 0

                    if len(novo_numero) == 10:

                        for num in novo_numero:
                            contagem += 1

                            if num in '0123456789':

                                if contagem == 10:
                                    verificacao_geral = True
                                continue

                            elif num == novo_numero[5] and num == '-':
                                verificacao_traco = True
                                continue

                            else:

                                if verificacao_traco == False:
                                    print('Precisa ter o "-"!')
                                    print('O número tem que seguir esse padrão -> 99999-9999')
                                    break

                                else:
                                    print('Você tem que digitar números!')
                                    verificacao = False
                                    break

                        if verificacao_geral == True:
                            editar_contato(agenda, usuario, opcao_edicao, novo_numero)         

                    else:
                        print('O número tem que seguir esse padrão -> 99999-9999')

                elif opcao_edicao == '3' or opcao_edicao == 'email':
                    novo_email = input('Digite o novo email do contato: ').lower()
                    if len(novo_email) > 10 and novo_email[-10:] == '@gmail.com' or novo_email[-12:] == '@outlook.com':
                        editar_contato(agenda, usuario, opcao_edicao, novo_email)
                    else:
                        print('Erro! Email não aceito!')

                else:
                    verificacao = False
                    print('Opção inválida!')

            else:
                print('Usuário não encontrado!')

        else:
            print('Adicione pelo menos um contato para fazer uma busca!')

    elif opcao == '4':

        if len(agenda) >= 1:
            mostrar_contatos()
            usuario = input('Digite o nome do usuário que deseja remover: ').lower()
            remover_contato(agenda, usuario)

        else:
            print('Adicione pelo menos um contato para fazer uma busca!')
        

    elif opcao == '5':
        print('Saindo do programa...')
        break

    else:
        print('Escolha uma opção válida!')