import json

def menu():
    print('--- AGENDA DE CONTATOS ---')
    print('1. Adicionar contato')
    print('2. Buscar contato')
    print('3. Editar contato')
    print('4. Remover contato')
    print('5. Sair')
    opcao = input('Escolha uma opção: [1,2,3,4,5] ')
    return opcao

def menu_edicao():
    print('O que deseja editar? ')
    print('1. Nome')
    print('2. Número')
    print('3. Email')
    opcao = input('Escolha uma opção: [1,2,3] ').lower()
    return opcao

def adicionar_contato(agenda, usuario, nome, celular, email):
    agenda[usuario] = [nome, celular, email]
    

def buscar_contato(agenda, usuario):

    verificacao = False
    for nome_de_usuario, informacoes in agenda.items():
        if nome_de_usuario == usuario:
            print()
            print(f'Informações do(a) usuário(a) "{usuario}": ')
            print(f'Nome: {informacoes[0]}')
            print(f'Número: {informacoes[1]}')
            print(f'Email: {informacoes[2]}')
            verificacao = True
    if verificacao == False:
        print(f'Usuário "{usuario}" não encontrado!')
    print()
    


def editar_contato(agenda, usuario, campo, novo_valor):
    if campo == '1':
        nome_campo = 'nome'

        for nome_de_usuario, informacoes in agenda.items():
            if nome_de_usuario == usuario:
                informacoes[0] = novo_valor
    elif campo == '2':
        nome_campo = 'número'
        for nome_de_usuario, informacoes in agenda.items():
            if nome_de_usuario == usuario:
                informacoes[1] = novo_valor
    else:
        nome_campo = 'email'
        for nome_de_usuario, informacoes in agenda.items():
            if nome_de_usuario == usuario:
                informacoes[2] = novo_valor
    print(f'Novo {nome_campo} salvo com sucesso!')
    salvar_agenda(agenda)

def remover_contato(agenda, usuario):
    pass

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
        usuario = input('Digite o seu nome de usuário: ').lower()
        verificacao_geral = False

        if usuario[0] == '@':
            nome = input('Digite o nome do contato: ')
            numero = input('Digite o número: (ex: 99999-9999) ')
            verificacao = True
            verificacao_traco = False
            contagem = 0

            if len(numero) == 10:

                for num in numero:
                    contagem += 1

                    if num in '0123456789':

                        if contagem == 10:
                            verificacao_geral = True
                        continue

                    elif num == numero[5] and num == '-':
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
                    email = input('Digite o email do contato: ').lower()

                    if len(email) > 10 and email[-10:] == '@gmail.com' or email[-12:] == '@outlook.com':
                        adicionar_contato(agenda, usuario, nome, numero, email)
                        salvar_agenda(agenda)
                        print('Contato salvo com sucesso!')
                    else:
                        print('Erro! Email não aceito!')

            else:
                print('O número tem que seguir esse padrão -> 99999-9999')

        else:
            print('O usuário precisa começar com o "@"!')


    elif opcao == '2':
        if len(agenda) >= 1:
            print('Usuários adicionados: ')
            cont = 1

            for nome_user in agenda.keys():
                print(f'{cont}- {nome_user}')
                cont += 1
            print()
            usuario = input('Digite o @ do usuário que deseja buscar informações: ').lower()
            buscar_contato(agenda, usuario)

        else:
            print('Adicione pelo menos um contato para fazer uma busca!')

    elif opcao == '3':

        if len(agenda) >= 1:
            print('Usuários adicionados: ')
            cont = 1

            for nome_user in agenda.keys():
                print(f'{cont}- {nome_user}')
                cont += 1
            print()

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
                print('Usuário nao encontrado!')

        else:
            print('Adicione pelo menos um contato para fazer uma busca!')

    elif opcao == '4':
        remover_contato()

    elif opcao == '5':
        print('Saindo do programa...')
        break

    else:
        print('Escolha uma opção válida!')