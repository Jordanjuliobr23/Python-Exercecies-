print('=-'*100)
print('TABELA DE DESEMPENHO NBA')
qtd=0
leste= []
oeste= []
while qtd < 30:
    c=int(input('Digite 1 para o time da conferencia Leste ou digite 2 para o time da conferencia Oeste: '))
    n=str(input('Digite o nome do time: '))
    v=int(input('Digite a quantidade de vitórias do time: '))
    if c == 1:
        leste.append((n,v))
    elif c == 2:
        oeste.append((n,v))
    qtd= qtd + 1
leste.sort(key=lambda x: x[1], reverse=True)
oeste.sort(key=lambda x: x[1], reverse=True)
i=0
while i < len(leste):
    team, vitorias = leste[i]
    print(f'{i+1} - {team}: {vitorias}/82')
    i= i + 1
print('PLAY=IN ZONE')
i= 7 
while i < 10: 
    team, vitorias= leste[i]
    print(f'{i+1} - {team}: {vitorias}/82')
    i= i + 1
print('Tank teams zone')
i= 10 
while i < len (leste):
    team, vitorias= leste[i]
    print(f'{i+1} - {team}: {vitorias}/82')
    i= i + 1 
    print('=-'*100)
i= 0 
while i < len(oeste):
    team, vitorias = oeste[i]
    print(f'{i+1} - {team}: {vitorias}/82')
    i= i + 1
print('PLAY=IN ZONE')
i= 7 
while i < 10: 
    team, vitorias= oeste[i]
    print(f'{i+1} - {team}: {vitorias}/82')
    i= i + 1
print('Tank teams zone')
i= 10 
while i < len (oeste):
    team, vitorias= oeste[i]
    print(f'{i+1} - {team}: {vitorias}/82')
    i= i + 1 
    print('=-'*100)   
            