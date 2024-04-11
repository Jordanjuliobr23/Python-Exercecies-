print('=-'*100)
print('Fruteira da Maria')
print('              Até 5 Kg              Acima de 5kg')
print('Morango     R$2.50 por Kg         R$ 2.20 por Kg')
print('Maçã        R$1.80 por Kg         R$ 1.50 por Kg')
qtd1=int(input('Digite a quantidade de morangos: '))
qtd2=int(input('Digite a quantidade de maçãs: '))
tot= qtd1 + qtd2
soma=0
p=0
if qtd1 <= 5:
    p= qtd1 * 2.50
    print('O preço a se pagar pelos {:.2f}Kg de morangos será de {:.2f}'.format(qtd1,p))
    soma= soma + p
if qtd1 > 5:
    p= qtd1 * 2.20
    print('O preço a se pagar pelos {:.2f}Kg de morangos será de {:.2f} '.format(qtd1,p))
    soma= soma + p
if qtd2 <= 5:
    p= qtd2 * 1.80
    print('O preço a se pagar pelos {:.2f}Kg de maçãs será de {:.2f}'.format(qtd2,p))
    soma= soma + p
if qtd2 > 5:
    p= qtd2 * 1.50 
    print('O preço a se pagar pelos {:.2f}Kg de maçãs será de {:.2f}'.format(qtd2,p))
    soma= soma + p
if tot > 8: 
    o= tot
    d=(soma * (10/100))
    soma= soma - d
    print('Pelo peso de {:.2f}Kg das frutas ultrapassarem 8Kg, o valor total sofrerá um desconto de 10%, descontando-se R${:.2f}'.format(o,d))
    print('Assim, o novo valor corresponde a {:.2f}'.format(soma))
if soma > 25: 
    o= soma
    d=(soma * (10/100))
    soma= soma - d 
    print('Pelo valor total de R${:.2f}, ultrapassar R$25.00, o valor total sofrerá um desconto de 10%, descontando-se R${:.2f}'.format(o,d))
    print('Assim, o novo valor corresponde a R${:.2f}'.format(soma))