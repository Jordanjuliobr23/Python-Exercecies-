print('=-'*100)
l=[1]

s=0
for t in range (1, 20):
    l2=[1]
    for i in range (len(l) - 1):
        l2.append(l[i] + l[i+1]) 
    l2= l2 + [1]    
    if t >= 2:
        s= s + l2[-3]
        print(l2)
    l=l2 
print('A soma dos antepenúltimos elementos do triangulo de pascal valem: ',s)

