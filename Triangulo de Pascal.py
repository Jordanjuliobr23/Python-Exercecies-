print('=-'*100)
qtd=int(input('Digite a quantidade de linhas para o triangulo de pascal: '))
t=[[1]] #Primeira linha começar em 1
for i in range (1, qtd):
    anterior= t[-1] 
    proxima= [1] # Próxima linha começa com o elemento 1
    for j in range(1, i):
        proxima.append(anterior[j-1] + anterior[j])
    proxima.append(1)
    t.append(proxima) 
for l in t: 
    print(l)    