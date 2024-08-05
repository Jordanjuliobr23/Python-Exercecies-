print('=-'*100)
l=[1]
for t in range (1, 20):
    l2=[1]
    for i in range (len(l) - 1):
        l2.append(l[i] + l[i+1]) 
    l2= l2 + [1]    
    print(l2)
    l= l2 
