

# for nome in nomes:
nome = input('Digite o nome do contato: ').title().strip()
verificacao_nome = False
for i in range(len(nome)):
    if nome[i] in '0123456789':
        break
    else:
        if i == len(nome)-1:
            verificacao_nome = True
print(nome)
if verificacao_nome:
    print('certooo')
else:
    print('Erro')