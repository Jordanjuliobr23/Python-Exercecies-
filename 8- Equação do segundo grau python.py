print('='*200)
print('CÁLCULO DE UMA FUNÇÃO DE 2o GRAU: ') 
a=float(input('Atribua um valor para a: '))
b=float(input('Atribua um valor para b: '))
c=float(input('Atribua um valor para c: '))
delta= b**2 - 4*a*c
raiz= -b**2 * delta
x1= -b + raiz 
x2= -b - raiz 
print('O valor atribuido para a foi {}, o valor atribuido a b foi {} e o valor atribuido a c foi {}'.format(a,b,c))
print('O resultado para x1 é {}'.format(x1))
print('O resultado para x2 é {}'.format(x2))