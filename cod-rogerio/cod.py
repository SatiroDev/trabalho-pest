agendas = []
ult_id = {"id": 1}
def menu_tarefas():
    print('Bem-vindo a lista de tarefas. O que deseja fazer?\n' 
        '[C] Criar Tarefas \n' 
        '[R] ler ou visualizar tarefas\n' 
        '[U] Atualizar tarfas\n'
        '[D] Deletar tarefas\n' 
        '[S] Sair do programa')
    opcao = input('Escolha uma opção: ').lower()
    return opcao
def criar_tarefas():
    while True:
        resposta = 0
        aux = {}
        id = ult_id['id']
        if len(agendas) != 0:
            id += 1
        
        tarefa = input('Qual o nome da tarefa que deseja adiconar? ')
        if len(tarefa) == 0:
            print('A tarefa tem que ter no mínimo 1 carácter')
            break
        descricao = input('Qual a descrição da tarefa? ')
        if len(descricao) <= 5:
            print('A descrição tem que ter no mínimo 5 carácter')
            break
        status = input('Qual o status da sua tarefa? (Feita/Pendente) ').capitalize()
        while resposta != 's' and resposta != 'n':
            resposta = input('Deseja adcionar mais tarefas(s/n): ').lower()
            if resposta != 's' and resposta != 'n':
                print('Você deve escrever S ou N')
        if status != 'Feita' and status != 'Feito' and status != 'Pendente':
            status = 'Pendente'
        aux['id'] = id
        aux['Tarefa'] = tarefa
        aux['Descrição'] = descricao
        aux['Status'] = status
        ult_id['id'] = id
        agendas.append(aux)
        if resposta == 's':
            continue
        elif resposta == 'n':
            break
def ler_vizualizar_tarefas():
    print('----TAREFAS ATRIBUIDAS----')
    for agenda in agendas:
        for T, v in agenda.items():
            print(f'{T}: {v}')
    print('=+'*13)
def atualizar_agenda():
    print('---- EDITAR AGENDA ----')
    print('O que você deseja editar?\n'
            '[1] Tarefa\n' 
            '[2] Descrição\n' 
            '[3] Status')
    opcao = input('Qual opção você deseja? ')
    while True:
        if opcao == '1':
            opcao = 0
            editar_tarefa()
        elif opcao == '2':
            opcao = 0
            editar_descricao()
def editar_tarefa():
    print('=+'*13)
    for agenda in agendas:
        for T, v in agenda.items():
            print(f'{T}: {v}')
    print('=+'*13)
    bolean = False
    while True:
        editar = input('Qual o ID da tarefa que você deseja editar? ')
        editar = int(editar)
        for agenda in agendas:
            for T,V in agenda.items():
                if bolean == True:
                    if T == 'descricao':
                            novo_nome = input("Qual o novo nome da tarefa? ")
                            agenda[T] = novo_nome
                if editar == V:
                    bolean = True
        resposta = input('Você deseja continuar(s/n)? ').lower()
        if resposta == 's':
            continue
        elif resposta == 'n':
            break
    if bolean == False:
        print('Este ID não foi encontrado! Reveja sua lista')
def editar_descricao():
    print('=+'*13)
    for agenda in agendas:
        for T, v in agenda.items():
            print(f'{T}: {v}')
    print('=+'*13)
    bolean = False
    while True:
        editar = input('Qual o ID da tarefa que você deseja editar? ')
        editar = int(editar)
        for agenda in agendas:
            for T,V in agenda.items():
                if bolean == True:
                    if T == 'descricao':
                            novo_nome = input("Escreva a nova descrição da tarefa? ")
                            agenda[T] = novo_nome
                if editar == V:
                    bolean = True
        resposta = input('Você deseja continuar(s/n)? ').lower()
        if resposta == 's':
            continue
        elif resposta == 'n':
            break
    if bolean == False:
        print('Este ID não foi encontrado! Reveja sua lista')
while True:
    escolha = menu_tarefas()
    if escolha == 'c':
        criar_tarefas()
    elif escolha == 'r':
        if len(agendas) == 0:
            print('A agenda está vazia. Coloque algo antes!')
        else:
            ler_vizualizar_tarefas()
    elif escolha == 'u':
        if len(agendas) == 0:
            print('A agenda está vazia. Coloque algo antes!')
        else:
            atualizar_agenda()