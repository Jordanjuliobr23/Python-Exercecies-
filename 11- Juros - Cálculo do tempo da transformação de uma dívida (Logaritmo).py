import math
print('=-'*100)
print('Tempo do valor de uma dívida')
print('BANCO DO REAL')
m=float(input('Digite um valor em reais para o montante: R$'))
c=float(input('Digite um valor em reais para o capital:  R$'))
i=float(input('Digite um valor para ser atribuido a taxa: R$'))
# a operação para encontrar o tempo é realizada da seguinte forma
t= math.log(m/c) / math.log (1+i/100)
print('=-'*100)
print('O valor atribuido ao montante foi de {:.2f}, o valor atribuido ao capital foi de {:.2f} e a taxa atribuida é {}%'.format(m,c,i))
print('O tempo para que esse valor se transforme é de {:1f} '.format(t))
print(math.ceil())