print('=-'*100)
print('Sistema de bilheteria em um estádio!')
time1=str(input('Digite o nome do time da casa: '))
time2=str(input('Digite o nome do time visitante: '))
preço=float(input('Digite o preço da entrada: '))
qtd=int(input('Selecione a quantidade de entradas: ')) 
# variável de controle para as quantidades de entradas
c1=0
estudantes=0
sosio=0
totalsosio=0
totalestd=0
total=0
while c1 < qtd: 
    n1=str(input('Por favor, digite seu nome e sobrenome: '))
    s=str(input(f'O torcedor {n1} é estudante? [Responda com Sim ou Não]: '))
    if s == 'sim' or s == 'Sim':
        i=str(input(f'Por favor, digite sua instituição de ensino: '))
        print(f'O torcedor {n1}, estudante da Instituição {i}, receberá um desconto de 30%')
        preço= ( preço - (preço * (30/100)))
        print('O valor a ser pago pela entrada do torcedor {} será R${:.2f}'.format(n1, preço))
        estudantes= estudantes + 1
        totalestd= totalestd + preço
        c1= c1 + 1 
        total= total + preço
    else: 
            
        if s == 'Não' or s== 'não':
            t=str(input(f'O torcedor {n1} é sósio do clube {time1}? [Responda Sim ou Não]: ')) 
            if t == 'Sim' or t == 'sim':
                print(f'O torcedor {n1}, por estar associado ao clube {time1}, receberá um desconto de 60% ')
                preço= ( preço - (preço * (60/100)))
                print('O valor a ser pago pela entrada do torcedor {} será de R${:.2f}'.format(n1,preço))
                totalsosio= totalsosio + preço 
                sosio= sosio + 1
                c1= c1 + 1
                total= total + preço 
            elif t == 'Não' or t =='não':
                print(f'O torcedor estará insento de descontos!')
                print(f'O torcedor pagará o valor inteiro de {preço}')
               
    
    if c1 == qtd: 
        print(f'=-'*50)
        print(' ===================== NOTA FISCAL - NOTA POTIGUAR =====================')
        print(f'Quantidade de ingressos: {qtd}')
        print(f'Ingressos sósios torcedor: {sosio}')
        print('        -> Valor: R${:.2f} '.format(totalsosio))
        print('Ingressos estudantes: {:.2f}'.format(estudantes))
        print('        -> Valor: R${:.2f} '.format(totalestd))
        print('=-'*20)
        print('Valor total: R${:.2f}'.format(total))
    
    

    