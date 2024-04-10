print('=-'*100)
print('COLETA DE DADOS IBGE')
n=int(input('Digite o número de cidades a serem comparadas: '))
qtd=0
qtd2=0
maior1=0
menor1=100000
nmaior1=0
nmenor1=100000
soma1=0
soma2=0
while qtd < n: 
    nome=str(input('Digite o nome da cidade: '))
    v=int(input('Número de veículos em passeio em 1999: '))
    a=int(input('Número de acidentes de transito em 1999: '))
    qtd= qtd + 1
    soma1= soma1 + v
    media1= soma1/qtd
    soma2= soma2 + a
    if a > maior1:
        maior1 = a
        nmaior1= nome
    if a < menor1:
        menor1= a
        nmenor1= nome
    if v < 2000: 
        soma2= soma2 + a
        qtd2= qtd2 + 1
        media2= soma2/qtd2
print(f'O menor índice de acidentes de transito no ano de 1999 pertence a cidade {nmenor1}, com {menor1} acidentes registrados!')
print(f'O maior índice de acidentes de transito no ano de 1999 pertence a cidade {nmaior1}, com {maior1} acidentes registrados')
print(f'A média de veículos em 1999 das {n} cidades juntas corresponde a aproximadamente: {media1}')
print(f'A média de acidentes de transito nas cidades inferiores 2000 veículos em atividade em 1999 corresponde a: {media2} ')
        
        
    