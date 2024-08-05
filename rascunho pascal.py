print('=-'*100)
l=[1] # Lista 'l', inicialmente contendo apenas o valor 1
for t in range (1, 20): # Lista responsável pela quantidade de lista do triangulo (t é o indice que representa cada linha)
    l2=[1] # A nova lista gerada a partir dos valores da lista 'l'
    # O objetivo geral desse segundo 'for' é criar os elementos que compõe a próxima linha
    for i in range (len(l) - 1): # Enquanto o indice passar pelo conjunto do tamanho da lista l em cada rodada - 1 
        l2.append(l[i] + l[i+1]) #  Adicione-se a lista l2, o indice de cada rodada, somado ao indice de cada rodada + 1     
    l2= l2 + [1]    # Número 1 adicionado no fim da lista l2
    print(l2) # Ao terminar ás rodadas, mostre-me todas as linhas
    l= l2 # L receberá os elementos na lista l2 em cada rodada, a fim de prepará para próxima linha
    