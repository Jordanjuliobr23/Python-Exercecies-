print('=-'*100)
print('Sistema de correção de notas com gabarito')
qtd=0
q= 1
pt=0
gab=['A,B,C,D,E,E,D,C,B,A']
while q < 10:
    n=str(input(f'Digite as letraa correspondente a questão {q}: '))
    if n == 'A':
        pt= pt + 1
    if n != 'A':
        pt= pt + 0
    q= q + 1 
    n=str(input(f'Digite as letra correspondente a questão {q}: '))
    if n == 'B':
        pt= pt + 1
    if n != 'B':
        pt= pt + 0
    q= q + 1 
    n=str(input(f'Digite as letra correspondente a questão {q}: '))
    if n == 'C':
        pt= pt + 1
    if n != 'C':
        pt= pt + 0
    q= q + 1 
    n=str(input(f'Digite as letra correspondente a questão {q}: '))
    if n == 'D':
        pt= pt + 1
    if n != 'D':
        pt= pt + 0
    q= q + 1 
    n=str(input(f'Digite as letra correspondente a questão {q}: '))
    if n == 'E':
        pt= pt + 1
    if n != 'E':
        pt= pt + 0
    q= q + 1 
    n=str(input(f'Digite as letra correspondente a questão {q}: '))
    if n == 'E':
        pt= pt + 1
    if n != 'E':
        pt= pt + 0
    q= q + 1 
    n=str(input(f'Digite as letra correspondente a questão {q}: '))
    if n == 'D':
        pt= pt + 1
    if n != 'D':
        pt= pt + 0
    q= q + 1 
    n=str(input(f'Digite as letra correspondente a questão {q}: '))
    if n == 'C':
        pt= pt + 1
    if n != 'C':
        pt= pt + 0
    q= q + 1 
    n=str(input(f'Digite as letra correspondente a questão {q}: '))
    if n == 'B':
        pt= pt + 1
    if n != 'B':
        pt= pt + 0
    q= q + 1 
    n=str(input(f'Digite as letra correspondente a questão {q}: '))
    if n == 'A':
        pt= pt + 1
    if n != 'A':
        pt= pt + 0
    print(f'O aluno conquistou {pt}/10 pontos na avalição')
    print('Programa encerrado')
    print('=-'*100)
   