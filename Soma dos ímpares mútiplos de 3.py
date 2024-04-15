# soma de ímpares mútiplos de 3
print('=-'*100)
print('A soma dos números ímpares de 1 a 500 mútilpos de 3 corresponde a: ')
soma=0
for c in range (1,501,2):
   if c % 3 == 0: 
        soma= soma + c 
print(soma)