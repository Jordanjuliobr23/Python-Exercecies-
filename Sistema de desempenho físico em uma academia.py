print('=-'*100)
print('ACADEMIA SALA DO TEMPO')
print('=-'*100)
print('DESEMPENHO FÍSICO DOS CLIENTES')
n=int(input('Digite a quantidade de clientes que serão comparados: '))
qtd=0 
alto=0
baixo=1000
mpeso=0
mnpeso=1000
soma1=0
soma2=0
nmpeso=0
nmmpeso=0
nalto=0
nbaixo=0
while qtd < n:
    x=str(input('Digite o nome do cliente: '))
    p=float(input('Peso do cliente em KG: '))
    h=float(input('Altura do cliente em Cm: '))
    qtd= qtd + 1
    soma1= soma1 + p
    soma2= soma2 + h
    média1= soma1/qtd
    média2= soma2/qtd
    if qtd == n:
        print('Sistema encerrado!')
        print('Obtendo resultados...')
    if h > alto:
        alto= h
        nalto= x 
    if h < baixo:
        baixo= h
        nbaixo= x
    if p > mpeso:
        mpeso=p
        nmpeso= x
    if p < mnpeso:
        mnpeso=p
        nmmpeso=x
print(f'O aluno mais alto é o cliente {nalto}, com {alto}cm!')
print(f'O aluno mais baixo é o cliente {nbaixo}, com {baixo}cm!')
print(f'O aluno mais pesado é o cliente {nmpeso}, com {mpeso}Kg!')
print(f'O aluno menos pesado é o aluno {nmmpeso}, com {mnpeso}Kg!')
print('A média das alturas entre os {} alunos é de {:.2f}Cm!'.format(n,média2))
print('A média de pesos entre os {} alunos é de {:.2f}KG!'.format(n,média1))
