print('=-'*100)
print('Quantos dias existem entre duas datas')
d1=int(input('Digite o dia INICIAL: '))
m1=int(input('Digite o mes INICIAL: '))
d2=int(input('Digite o dia FINAL: '))
m2=int(input('Digite o mes FINAL: '))
if m1 == 1:
    rm1= 0 
if m1 == 2:
    rm1= 31
if m1 == 3:
    rm1 = 59
if m1 == 4:
    rm1 = 90
if m1 == 5:
    rm1= 120
if m1 == 6:
    rm1= 151
if m1 == 7: 
    rm1 = 182
if m1 == 8:
    rm1 = 213
if m1 == 9:
    rm1 = 243 
if m1 == 10: 
    rm1 = 274 
if m1 == 11:
    rm1 = 304
if m1 == 12:
    rm1 = 334

if m2 == 1:
    rm2= 0 
if m2 == 2:
    rm2= 31
if m2 == 3:
    rm2 = 59
if m2 == 4:
    rm2 = 90
if m2 == 5:
    rm5= 120
if m2 == 6:
    rm2= 151
if m2 == 7: 
    rm2 = 182
if m2== 8:
    rm2 = 213
if m2 == 9:
    rm2 = 243 
if m2 == 10: 
    rm2 = 274 
if m2 == 11:
    rm2 = 304
if m2 == 12:
    rm2 = 334

r1= rm1 + d1 
r2= rm2 + d2
rtot= r2 - r1

print('=-'*100)
print('Os dias decorridos entre {}/{} a {}/{}  \n são {} dias ao todo!'.format(d1,m1,d2,m2,rtot))
    