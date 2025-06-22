pribidos_no_email = """() <> [] ; : , \ / " ' ` ~ = + * & % $ # ! { } | ? ^"""

emails_invalidos = [

    # 1. Falta de @ ou múltiplos @
    "josegmail.com",
    "jose@@gmail.com",
    "jose@gmail@com",

    # 2. Parte local inválida (antes do @)
    ".jose@gmail.com",
    "jose.@gmail.com",
    "jo..se@gmail.com",
    "-jose@gmail.com",
    "jose.@gmail.com.",
    "jose._@gmail.com",
    "jose-@gmail.com",
    "jose..abc@gmail.com",
    "jose!silva@gmail.com",

    # 3. Domínio inválido (após o @)
    "jose@.com",
    "jose@com.",
    "jose@-gmail.com",
    "jose@gmail-.com",
    "jose@gm_ail.com",
    "jose@.gmail.com",
    "jose@gmail..com",
    "jose@gmail._com",

    # 4. Extensão (TLD) inválida
    "jose@gmail.c",
    "jose@gmail.1a",
    "jose@gmail.123",
    "jose@gmail.",
    "jose@gmail..com",
    "jose@gmail.-com",
    "jose@gmail.com-",
    "jose@gmail..com.br",
    "jose@gmail.com..",

    # 5. Caracteres proibidos
    "jo$e@gmail.com",
    "jose@em*ail.com",
    "jose;silva@gmail.com",
    "jose,ana@gmail.com",
    "jose@ema(il).com",
    "jose@ema>il.com",
    "jose@ema il.com",

    # 6. Espaços ou campos vazios
    "jose @gmail.com",
    "jose@ gmail.com",
    "@gmail.com",
    "jose@",
    "",
    " ",
]

for email in emails_invalidos:
    email = email.lower().strip() 
    
    cont_arroba = email.count('@') #conta quantos '@' o usuário escreveu na variável 'email'
    verificacao = False
    verificacao_proibidos = False
    print(email)
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
        
        verificacao_email = True
        if len(sub_email_antes_do_arroba) >= 3:
            if sub_email_antes_do_arroba[-2] == '.' and sub_email_antes_do_arroba[-1] == '-' or sub_email_antes_do_arroba[-1] == '_' and sub_email_antes_do_arroba[-2] == '.':
                verificacao_email = False
        email_invertido = email[::-1]
        if '.' in email_invertido:
            posicao_ponto = email_invertido.index('.')
        if email_invertido[posicao_ponto+1] != '-' and email_invertido[posicao_ponto-1] != '-':
            if verificacao_email == True and email[0] != '@' and email[0] != '.' and email[-1] != '@' and email[-1] != '.' and pontos_seguidos == 0 and email[posicao_arroba-1] != '.' and email[posicao_arroba+1] != '.' and email[posicao_arroba+1] != '-' and email[posicao_arroba-1] != '-'and '_' not in email[posicao_arroba:]: # se não começar com "@" nem "." e não terminar com "@" nem "." e não tiver pontos seguidos e antes e dps do arroba não for um "." e se não tem "_" depois do "@"
                if email[0] != "-" and email[0] != "_" and email[-1] != "-" and email[-1] != "_":
                    if len(email[posicao_arroba:]) >= 4: # se o tamanho da 'sub_string' começando de onde está o '@' for maior que 4
                        sub_email = email[posicao_arroba:]
                        if '.' in sub_email: # se tiver '.' no "sub_email"
                            if '.' not in sub_email[-2:]: # se um '.' não estiver nem na penúltima e nem última posição 
                                print('Validooo!!')
                                verificacao = True
                                        
    if verificacao == False:
        print('Email inválido!')
    print()