print('=-'*100)
try:
    num=int(input('Digite um número qualquer: '))
    qtd=0
    soma=0
    media=0
    while num != 0:
        try:
            num=int(input('Digite um número novamente: '))
            soma= soma + num
            qtd= qtd + 1
            media= soma/qtd
            if num == 0:
                print(media)
        except ValueError:
                print('O que o usuário digitou não corresponde a um número válido!')
except num == str:
    print('O que o usuário digitou foi uma string e não um número!')
