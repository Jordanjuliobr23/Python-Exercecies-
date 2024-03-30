print('=-'*200)
print('A soma de todos os números mútiplos de 3 ou 5 entre 0 e 1000!')
soma= 0 
n=1 
while n <= 1000:
    if n % 5 == 0 or  n % 3 == 0:
        d3= True 
        d5= True
    if n % 5 != 0 or n % 3 != 0:
        d3= False
        d5= True
    if d5 and d3:
        soma= soma + n
    n= n + 1 
print(soma)

