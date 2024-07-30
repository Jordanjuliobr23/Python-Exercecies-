print('=-'*100) 
soma=[0]
for i in range (1,50): 
    soma.append(soma[-1] + i) 
print('As somas dos 50 elementos até 50 correspondem aos seguintes números: ')
print(soma)