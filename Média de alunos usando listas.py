print('=-'*100)
print('Média de altura de alunos')
menor=[]
maior=[]
normal=[]
soma=0
m=0
t=0
n=0
qtd=int(input('Digite a quantidade de alunos: '))
for i in range (qtd):
    idade=int(input(f'Digite a idade do aluno {i+1}: '))
    h=float(input(f'Digite a altura do aluno: {i+1}: '))
    soma= soma + h
    media= soma/qtd 
    if idade > 13 and h < media: 
        m= m + 1
        menor.append(m)
    elif idade < 13 and h >= media: 
        t= t + 1 
        maior.append(t)
    if idade > 13 and h >= media: 
        n= n + 1
        normal.append(t)
print('A média de altura dos alunos são: {:.2f}'.format(media))
print(f' A quantidade de alunos SUPERIOR de 13 anos com altura ABAIXO da média é: {menor}')
print(f'A quantidade de alunos com idade SUPERIOR a 13 anos com altura ACIMA ou IGUAL média é: {maior}')
print(f'A quantidade de alunos com idade INFERIOR a 13 anos com altura ACIMA ou IGUAL a média é: {normal}')