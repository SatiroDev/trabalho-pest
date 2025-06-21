import json
import os

def menu():
    print()
    print('-=-' * 15)
    print(f'{"-"*12} AGENDA DE CONTATOS {"-"*12}')
    print('1. Adicionar contato')
    print('2. Buscar contato')
    print('3. Editar contato')
    print('4. Remover contato')
    print('5. Sair')
    opcao = input('Escolha uma opção: [1,2,3,4,5] ')
    print('-=-' * 15)
    return opcao

def menu_edicao():
    print()
    print('-=-' * 15)
    print('O que deseja editar? ')
    print('1. Nome')
    print('2. Número')
    print('3. Email')
    opcao = input('Escolha uma opção: [1,2,3] ').lower()
    print('-=-' * 15)
    return opcao

def mostrar_contatos():
    print()
    print('-=-' * 15)
    print('Usuários adicionados: ')
    cont = 1
    for nome_user in agenda.keys():
        print(f'{cont}- {nome_user}')
        cont += 1
    print('-=-' * 15)


def adicionar_contato(agenda, usuario, nome, celular, email):
    print()
    print('-=-' * 15)
    agenda[usuario] = [nome, celular, email]
    salvar_agenda(agenda)
    print('Contato salvo com sucesso!')
    print('-=-' * 15)

def buscar_contato(agenda, usuario):
    print()
    print('-=-' * 15)
    if usuario in agenda.keys():
        print(' - '*15)
        print(f'Informações do(a) usuário(a) "{usuario}": ')
        print(f'Nome: {agenda[usuario][0]}')
        print(f'Número: {agenda[usuario][1]}')
        print(f'Email: {agenda[usuario][2]}')

    else:
        print(f'Usuário "{usuario}" não encontrado!')
    print('-=-' * 15)
    print(' - '*15)

def editar_contato(agenda, usuario, campo, novo_valor):
    print()
    print('-=-' * 15)
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
    print(' - '*15)
    print(f'Novo {nome_campo} salvo com sucesso!')
    salvar_agenda(agenda)
    print(' - '*15)
    print('-=-' * 15)

def remover_contato(agenda, usuario):
    print()
    print('-=-' * 15)
    if usuario in agenda.keys():
        del agenda[usuario]
        print(f'Usuário "{usuario}" removido com sucesso!')
        salvar_agenda(agenda)

    else:
        print(f'Usuário "{usuario}" não encontrado!')
    print('-=-' * 15)

def salvar_agenda(agenda):

    with open('agenda_de_contatos.json', 'w', encoding='utf-8') as f:
        json.dump(agenda, f, ensure_ascii=False, indent=4)

def carregar_agenda():
    if os.path.exists('agenda_de_contatos.json'):
        with open('agenda_de_contatos.json', 'r', encoding='utf-8') as f:
            return json.load(f)
        
    else:
        return {}

agenda = carregar_agenda()

while True:

    opcao = menu()

    if opcao == '1':
        usuario = input('Digite o nome de usuário: ').lower().strip()
        if usuario not in agenda:
            verificacao_geral = False

            if usuario[0] == '@':
                nome = input('Digite o nome do contato: ').title().strip()
                numero = input('Digite o número: (ex: 99999-9999) ').strip()
                contagem = 0

                if len(numero) == 10:

                    for num in numero:
                        if numero[5] == '-':
                            if num in '0123456789':
                                contagem += 1
                                if contagem == 9:
                                    verificacao_geral = True
                            continue
                        else:
                            break

                    if verificacao_geral == True:
                        email = input('Digite o email do contato: ').lower().strip()
                        cont_arroba = email.count('@')

                        pontos_seguidos = 0
                        for i in range(len(email)+1):
                            if i == len(email)-1:
                                break
                            if email[i] == email[i+1] and email[i] == '.':
                                pontos_seguidos += 1
                        verificacao = False
                        if '@' in email:
                            posicao_arroba = email.index('@')
                            if cont_arroba == 1 and email[0] != '@' and email[0] != '.' and email[-1] != '@' and email[-1] != '.' and pontos_seguidos == 0 and email[posicao_arroba-1] != '.' and email[posicao_arroba+1] != '.':
                                if len(email[posicao_arroba:]) >= 4:
                                    sub_email = email[posicao_arroba:]
                                    if '.' in sub_email:
                                        posicao_ponto = sub_email.index('.')
                                        if '.' not in sub_email[-2:]:
                                            adicionar_contato(agenda, usuario, nome, numero, email)
                                            verificacao = True
                                        
                        if verificacao == False:
                            print('Email inválido!')
                    
                if verificacao_geral == False:

                    print('Erro! O número tem que seguir esse padrão -> 99999-9999')

            else:
                print('O usuário precisa começar com o "@"!')
        else:
            print(f'Usuário "{usuario}" já está adicionado!')


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

                            if num in '0123156789':
                                contagem += 1
                                if contagem == 9:
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
                        print('Erro! O número tem que seguir esse padrão -> 99999-9999')

                elif opcao_edicao == '3':
                    novo_email = input('Digite o novo email do contato: ').lower()
                    if len(novo_email) > 10 and novo_email[-10:] == '@gmail.com' or novo_email[-12:] == '@outlook.com':
                        editar_contato(agenda, usuario, opcao_edicao, novo_email)
                    else:
                        print('Erro! Email não aceito!')

                else:
                    verificacao = False
                    print('Opção inválida!')
                    print('Digite "1" ou "2" ou "3"!')

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
            print()
        

    elif opcao == '5':
        print(' - '*15)
        print('Saindo do programa...')
        print(' - '*15)
        print('-=-' * 15)
        break

    else:
        print('Escolha uma opção válida!')
        print('Digite "1" ou "2" ou "3" ou "4" ou "5"!')
        print(' - '*15)