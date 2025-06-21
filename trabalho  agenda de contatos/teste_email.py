while True:
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
                        print('Email validooo!!!!')
                        verificacao = True
                    
    if verificacao == False:
        print('Email inválido!')