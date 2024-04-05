print('=-'*100)
print('ELEIÇÃO COM TRES CANDIDATOS!')
n=int(input('Por favor digite o número total de eleitores: ')) 
voto= 0 
c= 0
soma1=0
soma2=0
soma3=0
while c < n:
    c1=int(input('Digite 1 se for votar no candidato 1, se não, digite 0:  '))
    c2=int(input('Digite 1 se for votar no candidato 2, se não , digite 0: '))
    c3=int(input('Digite 1 se for votar no candidato 3, se não, digite 0:  '))
    if c1 == 1:
        print('Voto confirmado ao candidato 1!')
        soma1= soma1 + 1 
    elif c1 == 0:
        print('Voto não confirmado ao candidato 1!')
    elif c1 != 1 and c1 != 0:
        print('Votação cancelada!')
    if c2 == 1:
        print('Voto confirmado ao candidato 2!')
        soma2= soma2 + 1
    elif c2 == 0: 
        print('Voto não confirmado ao candidto 2!')
    elif c2 != 1 and c2 != 0:
        print('Votação cancelada!')
    if c3 == 1:
        print('Voto confirmado ao candidato 3!')
        soma3= soma3 + 1
    elif c3 == 0: 
        print('Voto não confirmado ao candidato 3!')
    elif c3 != 1 and c3 != 0:
        print('Votação cancelada!')
    c= c + 1
if soma1 > soma2 and soma1 > soma3:
    print(f'O candidato 1, venceu a eleição, com {soma1} votos!') 
elif soma1 < soma2 and soma2 > soma3:
    print(f'O candidato 2, venceu a eleição, com {soma2} votos!')
elif soma1 < soma3 and soma2 < soma3:
    print(f'O candidato 3, venceu a eleição com {soma3} votos')
elif soma1 == soma2 and soma2 == soma3:
     print(f'De acordo com a apuração dos votos, os candidatos estão empatados com {soma1} votos! ')
elif soma1 == soma2 and soma1 != soma3:
    print(f'De acordo coma a apuração dos votos os candidatos 1 e 2 estão empatados com {soma1} votos cada! ')
elif soma1 != soma2 and soma1 == soma3: 
    print(f'De acordo com apuração dos votos os candidatos 1 e 3 estão empatados com {soma1} votos cada!')
elif soma1 != soma2 and soma2 == soma3:
    print(f'De acordo com a apuração dos votos os candidatos 2 e 3 estão empatados com {soma2} votos cada!')
elif soma1==0 and soma2==0 and soma3==0:
     print(f'A eleição está cancelada em virtude da carencia de votos em ambos os candidatos!') 
        