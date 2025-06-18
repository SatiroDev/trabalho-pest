import json

def menu():
    print('--- AGENDA DE CONTATOS ---')
    print('1. Adicionar contato')
    print('2. Buscar contato')
    print('3. Editar contato')
    print('4. Remover contato')
    print('5. Sair')
    opcao = input('Escolha uma opção: ')
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
    pass

def remover_contato(agenda, usuario):
    pass

def salvar_agenda(agenda):
    pass



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
                        with open('contatos.json', 'w') as f:
                            json.dump(agenda, f)
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
        editar_contato()
    elif opcao == '4':
        remover_contato()
    elif opcao == '5':
        print('Saindo do programa...')
        break
    else:
        print('Escolha uma opção válida!')