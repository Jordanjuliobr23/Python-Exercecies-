print('=-'*100) 
print('Quantos números de 9 digitos, cujo a soma dos 3 últimos números é menor que 8 existem? ') 
c=0 
for x in range (100000000,1000000000): 
    n= x 
    z= n % 10 
    n= n // 10 
    y= n % 10
    n= n // 10
    w= n % 10
    n= n // 10 
    soma= z + y + x
    if soma < 8: 
        c= c + 1
print('=-'*100)
print(f'A quantidade de números de 9 digitos, cujo a soma dos 3 últimos números é menor que 8 são: {c}')