print('='*200)
print('CÁLCULO DE DOIS PONOTS NO PLANO CARTEZIANO')
x1=float(input('Digite um valor para coordenada x1:  '))
x2=float(input('Digite um valor para cooordenada x2: ')) 
y1=float(input('Digite um valor para coordenada y1: '))
y2=float(input('Digite um valor para coordenada y2: '))
d= (((x2-x1)**2) + ((y2-y1)**2))**1/2
print('A coordenada escolhida pelo usuário para x1 foi  ',x1)
print('A coordenada escolhida pelo usuário para x2 foi  ',x2)
print('A coordenada escolhida pelo usuário para y1 foi ', y1)
print('A coordenada escolhida pelo usuário para y2 foi ', y2) 
print('A distancia com base nas coordenadas escolhidas pelo usuário será: ',d)
print('='*200)