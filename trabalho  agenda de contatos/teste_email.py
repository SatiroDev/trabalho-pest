pribidos_no_email = """() <> [] ; : , \ / " ' ` ~ = + * & % $ # ! { } | ? ^"""
while True:
    email = input('Digite o email do contato: ').lower().strip()
    cont_arroba = email.count('@') #conta quantos '@' o usuário escreveu na variável 'email'
    verificacao = False
    verificacao_proibidos = False
    for string in pribidos_no_email:
        if string in email:
            verificacao_proibidos = True
            break
    if cont_arroba == 1 and verificacao_proibidos == False:
        pontos_seguidos = 0 # variável para ajudar na verificação
        for i in range(len(email)+1):
            if i == len(email)-1: # condição para o codigo não quebar
                break
            if email[i] == email[i+1] and email[i] == '.': # se uma string em uma pocição for igual ao do lado, e a string verificada for um ponto
                pontos_seguidos += 1 

        posicao_arroba = email.index('@') # posição de onde está o '@'
        if email[0] != '@' and email[0] != '.' and email[-1] != '@' and email[-1] != '.' and pontos_seguidos == 0 and email[posicao_arroba-1] != '.' and email[posicao_arroba+1] != '.': # se não começar com "@" nem "." e não terminar com "@" nem "." e não tiver pontos seguidos e antes e dps do arroba não for um "."
            if len(email[posicao_arroba:]) >= 4:
                sub_email = email[posicao_arroba:]
                if '.' in sub_email:
                    posicao_ponto = sub_email.index('.')
                    if '.' not in sub_email[-2:]:
                        print('Email válidooo!!')
                        verificacao = True
                                        
    if verificacao == False:
        print('Email inválido!')