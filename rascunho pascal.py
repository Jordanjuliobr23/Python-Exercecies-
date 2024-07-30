print('=-'*100)
qtd=int(input('Digite a quantidade de linhas para o Triangulo de Pascal: '))
t=[[1]] # Primeira linha começar com 1 
# Objetivo 1, criar as linhas subsequente do triangulo de Pascal
for i in range (1,qtd):
    anterior=t[-1] # Última linha em cada rodada do laço 
    proxima= [1] # Primeiro elemento da próxima linha
# Objetivo 2, colcocar os elementos na próxima linha 
    for j in range (1, i): 
        proxima.append(anterior[j-1] + anterior[j]) 
    proxima.append(1)
    t.append(proxima)
for l in t:
    print(l)
        
    