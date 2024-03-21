print('='*200)
print('CAIXA ELETRONICO ')
c=float(input('Digite o valor total da compra: '))
d=float(input('Digite o valor corresponde ao pagamento do cliente: '))
t= d - c
print('O valor da compra corresponde a R$',c)
print('O valor do troco corresponde a R$',t)
# variáveis referentes a divisão das células e moedas do troco
n100= t//100 
print('A quantidade de notas de cem: ',n100)
t = t - n100 *100 
print('='*100)
n50= t//50
print('A quantidade de notas de cinquenta: ',n50)
t= t - n50 *50
print('='*100)
n20= t//20
print('A quantidade de notas de vinte: ',n20)
t= t - n20 *20
print('='*100)
n10= t//10
print('A quantidade de notas de dez: ',n10)
t= t - n10 *10
print('='*100)
n5= t//5
print('A quantidade de notas de cinco: ',n5)
t= t - n5 *5
print('='*100) 
n2= t//2
print('A quantidade de notas de dois: ',n2)
t= t - n2 *2
print('='*100)
n1= t//1
print('A quantidade de moedas de um:  ',n1)
t= t - n1*1
print('='*100)
n050= t * 0.5
print('A quantidade de moedas de cinquenta:  ',n050)
t= t - n050 //  0.5
print('='*100)
n025= t*0.25
print('A quantidade de moedas de vinte cinco:  ',n025)
t= t - n025//0.25
print('='*100)
n010= t*0.10
print('A quantidade de moedas de dez:  ',n010)
t= t - n010//0.10
print('='*100)
n005= t * 0.05
print('A quantidade de moedas de cinco:  ',n005)
t= t - n005//0.05
print('='*100)
n001= t//0.01
print('A quantidade de moedas de um:  ',n001)
t= t - n001*0.01
print('Troco resgatado com sucesso!')
# Aaron Goldberg - 20241014050033
# Jordan Julio - 20241014050014










