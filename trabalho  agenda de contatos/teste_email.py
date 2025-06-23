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


emails_validos = [
    'validar_email@gmail.com',
    # Básicos e comuns
    "jose 34@gmail.com",
    "joao@gmail.com",
    "ana.silva@outlook.com.br",
    "maria_2024@yahoo.com",
    "carlos-dev@empresa.org",
    "lucas123@host.net",

    # Com hífens e underlines no nome de usuário
    "user_test-01@dominio.com",
    "ana-bia_1988@meusite.com.br",
    "lucas.dev_pro@startup.dev",

    # Subdomínios
    "contato@sub.dominio.com",
    "user@suporte.empresa.tech",
    "admin@server1.host123.com",

    # TLDs variados e modernos
    "nome@loja.online",
    "dev@site.tech",
    "suporte@instituto.edu.br",
    "info@empresa.ai",
    "hello@site.dev",

    # Domínios com números no meio ou no fim
    "jose@host123.com",
    "ana@empresa2025.com",
    "time@projeto2.org",
    "exemplo@v2.portal.gov.br",

    # Endereços curtos mas válidos
    "a@b.co",
    "x@y.io",
    "z9@d4.dev",

    # Combinando vários estilos
    "lucas_oliveira-test@sub.projeto-2024.org",
    "user.name_01@infra.ti.gov.br",
]


for email in emails_validos:
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
            verificacao_numero = True
            for i in email_invertido[:posicao_ponto]: # verificar se tem número na extensão
                if i in '1234567890':
                    verificacao_numero = False
                    break
        if email_invertido[posicao_ponto+1] != '-' and email_invertido[posicao_ponto-1] != '-' and verificacao_numero == True:
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