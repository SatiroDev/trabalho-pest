usuario = input('>> Qual o nome do usuário (Utilize @ no começo. Ex: @gaguin)? ').lower()
print(usuario)
bolean = False
if len(usuario) == 0:
    print('Não deixe em branco')
elif usuario[0] == '@' and len(usuario) > 1:
    print('Usuario ', usuario, 'olaa')
print(len(usuario))