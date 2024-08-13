import datetime
print('=-'*100)
print('Quantos endereços distintos se conectaram ao servidor? ')
print('=-'*100) 
fd= open('apache_logs.txt','r')
ips_tot=[]

inicio= datetime.datetime.now()

for l in fd:
    l= l.split()
    ips_tot.append(l[0]) 
fd.close()
ips_diferentes= set(ips_tot)

agora= datetime.datetime.now()
print(f'Existem {len (ips_diferentes)} endereços IP diferentes que se concectaram ao servidor')