print('=-'*100)
print('MÉDIA DE IDADE DE UM GRUPO!')
print('Olá,digite a seguinte informação abaixo: ')
n=int(input('Por favor digite a quantidade de pessoas que responderam a pesquisa: '))
soma=0
c=0
while n > 0: 
    idade=int(input('Por favor, digite sua idade: '))
    soma= soma + idade 
    c= c + 1
    if c == n: 
        media= soma / n 
        if media > 0 and media <= 25: 
            print(f'A média de idade da turma é {media}, variando entre 0-25 anos, sendo uma turma de idade jovem!')
            break
        if media >= 26 and media <= 60: 
            print(f'A média de idade da turma é {media} , variando entre 26-60 anos, sendo uma turma de idade regular! ')
            break
        if media > 60: 
            print(f'A media de idade da turma é {media}, estando acima de 60 anos, sendo uma turma de idade idosa! ')
            break