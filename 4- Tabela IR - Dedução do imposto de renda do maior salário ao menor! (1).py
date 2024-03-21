print('='*200)
print('Tabela IR - Dedução do imposto de renda')
print('Do maior salário ao menor')
s=float(input('Digite o valor correspondente ao salário: '))
if s > 4664.68:
    a1= s * (27.5/100) - 896.00
    n1= s - a1
    print('O salário atual com as atribuições será de R${:.2f}'.format(n1))
if 3751.06 <= s <= 4464.68:
    a2= s * (22.5/100) - 662.77
    n2= s - a2
    print('O salário atual com as atribuições irá corresponder a R${}'.format(n2))
if 2826.66 <= s <= 3751.05: 
    a3= s * (15/100) - 381.44 
    n3= s - a3 
    print('O salário atual com as atribuições irá corresponder a R${:.2f}'.format(n3))
if 2259.21 <= s <= 2826.65: 
    a4= s * (7.5/100)
    n4= s - a4
    print('O salário atual com as atribuições irá corresponder a R${:.2f}'.format(n4))
if s <= 2259.20: 
    print('O salário estará insento de aliquota e parcela de dedução, permanecendo R${:.2f}'.format(s))

  