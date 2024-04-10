print('=-'*100)
print('ORAGANIZAÇÃO GUANABARA')
s=float(input('Digite seu salário: R$'))
if s <= 2080.00: 
    a1= s * (20/100)
    s1= (s * (20/100)) + s
    print('O salário que antes era de R${}, agora passa por um aumento de 20%, que corresponde R${:.2f} '.format(s,a1))
    print('O novo salário do funcionário corresponde a R${}'.format(s1))
if s > 2080.00 and s <= 4500.00:
    a2= s * (15/100)
    s2= (s * (15/100)) + s
    print('O salário que antes era de R${}, agora passa por um aumento de 15%, que corresponde R${:.2f}'.format(s,a2))
    print('O novo salário do funcionário corresponde a R${:.2f}'.format(s2))
if s > 4500.00  and s <= 7000.00:
    a3= s * (10/100)
    s3=  (s * (10/100)) + s
    print('O salário que antes era de R${}, agora passa por um aumento de 10%, que corresponde a R${:.2f}'.format(s,a3))
    print('O novo salário do funcionário corresponde a R${:.2f}'.format(s3))
if s > 7000.00 and s <= 10000.00:
    a4= s *  (5/100)
    s4= (s*  (5/100)) + s
    print('O salário que antes era de R${}, agora passa por um aumento de 5%, que corresponde a R${:.2f}'.format(s,a4))
    print('O novo salário do funcionário corresponde a R${:.2f}'.format(s4))
if s > 10000.00:
    a5= s * (1/100)
    s5= (s * (1/100)) + s
    print('O salário que antes era de R${}, agora passa por um aumento de 1%, que corresponde a R${:.2f}'.format(s,a5))
    print('O novo salário do funcionário corresponde a R${:.2f}'.format(s5))
