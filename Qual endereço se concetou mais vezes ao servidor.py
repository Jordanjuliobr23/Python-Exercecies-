import datetime
print('=-'*100)
print('Quantos endereços distintos se conectaram ao servidor? ')
print('=-'*100) 
fd= open('apache_logs.txt','r')
ips_tot=[]
ip_mais_conec= None 
vezes_concec= 0
inicio= datetime.datetime.now()

for l in fd:
    l= l.split()
    ips_tot.append(l[0]) 
fd.close()
ips_diferentes= set(ips_tot)

for ip in ips_diferentes:
    conec= ips_tot.count(ip)
    if conec > vezes_concec:
        ip_mais_conec = ip 
        vezes_concec = conec

agora= datetime.datetime.now()

print(f'Tempo: {(agora- inicio).seconds}')
print(f'Existem {len (ips_diferentes)} endereços IP diferentes que se concectaram ao servidor')
print(f'O endereço IP que mais conectou-se ao servirodor foi {ip_mais_conec}, com {vezes_concec} conexões')