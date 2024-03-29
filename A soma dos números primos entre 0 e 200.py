print('=-'*100)
print('Soma de todos os primos de 0-200')
soma= 0
n = 1
while n <= 200:
    if n > 1 and n % n == 0: 
        primo= True 
        div = 2 
        while div < n: 
            if n % div == 0:
                primo = False  
            div = div + 1 
        if primo: 
            soma= soma + n 
    n= n + 1 
print(soma)
            