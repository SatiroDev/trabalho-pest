lista_conjuntos = [['x', [1,2,3,4,5,6,7]], ['y', [2,3,4]]]


lista_uniao = [] 
conjunto1 = input('Qual o primeiro conjunto para fazer a união? ')
for conjunto in lista_conjuntos:
    if conjunto1 in conjunto[0]:
        conjunto2 = input('Qual o segundo conjunto para fazer a união? ')
    if conjunto2 in conjunto[0]:
        for conjuntox in lista_conjuntos:
            if conjuntox[0] == conjunto1:
                for num in conjuntox[1]:
                    lista_uniao.append(num)
            if conjuntox[0] == conjunto2:
                for num in conjuntox[1]:
                    lista_uniao.append(num)
    else:
        print('Conjunto inexistente')
    for elemento in lista_uniao:
        cont = 0
        contador = lista_uniao.count(elemento)
        if contador > 1:
            while cont < contador-1:
                lista_uniao.remove(elemento)
                cont += 1
print(lista_uniao)