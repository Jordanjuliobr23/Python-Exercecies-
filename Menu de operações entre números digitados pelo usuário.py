print('=-'*100)
print('Menu de operações envolvendo números: ')
qtd=int(input('Digite a quantidade de números que deseja-se trabalhar: '))
c=0
soma=0
mutiplicação=1
div=0
maior=0 
menor= 10000000
novosnúmeros=0
sairdoprograma=0
while c < qtd:
    for n in range (0,qtd):
        n=int(input('Digite um número: '))
        soma= soma + n 
        mutiplicação= mutiplicação * n 
        div= div + n / n 
        if n > maior: 
            maior= n 
        if n < menor: 
            menor= n
        c= c + 1
print(f'=======    MENU  =======  ')
print(f' [1] A soma dos {qtd} números digitados vale {soma}')  
print(f' [2] O produto dos {qtd} números digitados vale {mutiplicação}')
print(f' [3] A divisão dos {qtd} números digitados vale {div}')
print(f' [4] O maior valor dos {qtd} números digitados vale {maior}')
print(f' [5] O menor valor dos {qtd} números digitados vale {menor}')
print(f' [6] Os novos números encontrados foram {soma}, {mutiplicação} e {div}')
print(f' [7] Programa encerrado')
