print('=-'*100)
print('SLAM DUNK CONTEST')
y=int(input('Digite o número da temporada (exemplo: 2016): '))
n=str(input('Digite o nome do atleta: '))
f=str(input('Digite o nome da sua franquia: '))
qtd=int(input('Digite a quantidade de jurados: '))
soma=0
media=0 
maiornota=0
menornota=10000
c= 0
x= 0
j=1
while c < qtd:
    print(f'Jogador: {n}')
    print(f'Time: {f}') 
    nota=float(input(f'Jurado {j} por favor digite sua nota: '))
    j= j + 1
    if nota > maiornota:
        maiornota= nota 
    if nota < menornota:
        menornota= nota 
    else: 
        soma= soma + nota
        x= x + 1 
        media= soma/x 
    c= c + 1
print('=--'*100)
print('RESULTADO FINAL: ') 
print(f' Slam Dunk Contest {y}')
print(f'Jogador: {n}')
print(f'Time: {f}') 
print(f'Melhor nota: {maiornota}')
print(f'Pior nota: {menornota}')
print(f'Sua média foi {media}')