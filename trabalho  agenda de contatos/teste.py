string = 'jose..@gamil.com......'
pos = string.index('@')
print(pos)
print(string[pos:])

pontos = 0
for i in range(len(string)+1):
    if i == len(string)-1:
        break
    if string[i] == string[i+1] and string[i] == '.':
        pontos += 1
print(pontos)