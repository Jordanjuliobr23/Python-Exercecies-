print('=-'*100) 
print('Número médio de alunos por turma!') 
t=int(input('Digite a quantidade de turmas: ')) 
qtd= 0
média=0
c= 0
while t > 0:
    a=int(input('Digite a quantidade de alunos para a turma: '))  
    if a > 40:
        print('O número limite de alunos por sala é 40, assim, o número digitado excede esse limite!')
    else: 
        qtd= qtd + a 
        c= c + 1
    if c == t:
        média= int(qtd/t) 
        print(f'A média de alunos para cada uma das {t} turmas será de aproximadamente {média}')
    
