
print('='*200)
print('ESTE PROGRAMA LER E FAZ A SOMA DOS QUATRO DIGITOS')
n=int(input('Digite um número com 4 algarismos: '))
#unidade 
a= n % 10
n= n // 10 
#dezena
b= n % 10
n= n // 10
#centena
c= n % 10
n= n // 10
#milhar 
d= n 
soma= a + b + c + d 
print('A soma dos digitos do número vale: ', soma)