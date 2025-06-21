pribidos_no_email = """() <> [] ; : , \ / " ' ` ~ = + * & % $ # ! { } | ? ^"""
while True:
    email = input('Digite o email do contato: ').lower().strip()
    cont_arroba = email.count('@') #conta quantos '@' o usuário escreveu na variável 'email'
    verificacao = False
    verificacao_proibidos = False
    for caracter in pribidos_no_email:
        if caracter in email: # se um caractere proibido estiver no email que o usuário digitou
            verificacao_proibidos = True
            break
        if cont_arroba == 1 and verificacao_proibidos == False: # se o email tiver so um '@' e não tiver nenhum caractere  proibido
            pontos_seguidos = 0 # variável para ajudar na verificação
    for i in range(len(email)+1):
        if i == len(email)-1: # condição para o codigo não quebar
            break
        if email[i] == email[i+1] and email[i] == '.': # se uma string em uma pocição for igual ao do lado, e a string verificada for um ponto
            pontos_seguidos += 1 
                            
    posicao_arroba = email.index('@') # posição de onde está o '@'
    sub_email_antes_do_arroba = email[:posicao_arroba] # sub_email, do começo até antes do "@"
    print(sub_email_antes_do_arroba)
    verificacao_email = True
    if len(sub_email_antes_do_arroba) >= 3:
        if sub_email_antes_do_arroba[-2] == '.' and sub_email_antes_do_arroba[-1] == '-' or sub_email_antes_do_arroba[-1] == '_' and sub_email_antes_do_arroba[-2] == '.':
            verificacao_email = False
    if verificacao_email == True and email[0] != '@' and email[0] != '.' and email[-1] != '@' and email[-1] != '.' and pontos_seguidos == 0 and email[posicao_arroba-1] != '.' and email[posicao_arroba+1] != '.' and '_' not in email[posicao_arroba:]: # se não começar com "@" nem "." e não terminar com "@" nem "." e não tiver pontos seguidos e antes e dps do arroba não for um "." e se não tem "_" depois do "@"
        if len(email[posicao_arroba:]) >= 4: # se o tamanho da 'sub_string' começando de onde está o '@' for maior que 4
            sub_email = email[posicao_arroba:]
            if '.' in sub_email: # se tiver '.' no "sub_email"
                if '.' not in sub_email[-2:]: # se um '.' não estiver nem na penúltima e nem última posição 
                    print('Validooo!!')
                    verificacao = True
                                        
    if verificacao == False:
        print('Email inválido!')