print('=-'*100)
print('Sistema de tabela de juros')
n=float(input('Digite o valor de uma dívida: R$'))
qtd=0
vd= 1000.00
j1=0
vp=0
print(      ' Valor da Dívida - Valor do Juros -  Qtd de Parcelas   -   Valor da Parcela ')
while vd < n: 
    vd= vd + j1 
    j1= j1 + 50 
    qtd= qtd + 3
    vp= vd/qtd 
    print('   R$ {:.2f}              {}                {}                     R${:.2f}        '.format(vd,j1,qtd, vp))