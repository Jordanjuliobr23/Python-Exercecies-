print('=-'*200)
print('Sequencia de Fibonacci!')
print('A soma apenas dos números pares da sequencia de Fibonacci !')
a, b= 1, 1
soma= 0
while a <= 4000000:
    if a % 2 == 0:
        soma = soma + a
    a, b = b, a + b
print(soma)
