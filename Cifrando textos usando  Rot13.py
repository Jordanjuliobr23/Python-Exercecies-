frase=(input('Por favor digite um texto: '))
alfabeto='ACDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
rot13='' 
for l in frase: # Laço de repetição que irá trabalhar com as letras da frase digitada
    if 'A' <= l <= 'Z': # Contempla todas as letras maiúsculas
        nl= ord(l) + 13 # Trabalha com a posição da letra na tabela ascii e soma 13 posições
        if nl > ord ('Z'): # Se ultrapassar número ultrapssar o z;
            nl=nl % ord('Z') + ord('A') -1 # Pegamos o número, fazemos 
    elif 'a' <= l < 'z':
        nl= ord (l) + 13 
        if nl > ord ('z'):
            nl= nl % ord ('z') + ord('a') -1
    else:
        nl=ord(l)
    rot13 += chr(nl)
print(rot13)