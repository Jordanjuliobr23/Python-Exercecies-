print('='*200)
print('CÁLCULO DO PLANO CARTESIANO') 
x1=float(input('Atribua um valor para a coordenada x1: '))
x2=float(input('Atribua um valor para coordenada x2: '))
y1=float(input('Atribua um valor para a coordenada y1: '))
y2=float(input('Atribua um valor para coordenada y2: ')) 
d= (((x2-x2)**2) + ((y2-y1)**2))*0.5 
print('Oa valores atribuidos pelo usuário as coordenadas x1 e x2 foram respectivamente {} e {}'.format(x1,x2))
print('Os valores atribuidos pelo usuário as coordenadas y1 e y2 foram respectivamente {} e {}'.format(y1,y2))
print('A distancia entre os pontos correspomnde ao resultado: ',d)