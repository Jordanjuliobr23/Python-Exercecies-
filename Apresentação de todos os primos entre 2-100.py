print('=-'*100)
print('MOSTRAR TODOS OS PRIMOS DE 1 ATÉ 100')
ndiv= 0
n = 1
while n <= 100:
    if n > 1 and n % n == 0: 
        primo= True 
        div = 2 
        while div < n: 
            if n % div == 0:
                primo = False  
            div = div + 1 
        if primo: 
            print('Número primo entre 1-100: ')
            print(n)
    n = n + 1 

            



    
    
    
    
