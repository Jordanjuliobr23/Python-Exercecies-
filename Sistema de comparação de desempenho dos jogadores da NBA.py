print('=-'*100)
print('SISTEMA DE COMPARAÇÃO DE DESEMPENHO DE JOGADORES DE NBA')
qtd=int(input('Digite a quantidade de jogadores que terão suas principais estatísticas comparadas: '))
if qtd < 2:
    print(f'O usuário digitou apenas 1 jogador! O programa não irá prosseguir!')
c= 0
nmaiorpts=0
maiorpts=0
menorpts= 1000
nmenorpts= 1000
nmaiorast=0
maiorast=0
menorast=1000
nmenorast=1000
nmaiorreb=0
maiorreb=0
menorreb=1000
nmenorreb=1000
nmaiortpts=0
maiortpts=0
menortpts=1000
nmenortpts=1000
while c < qtd: 
    n=str(input('Digite o nome do jogador: '))
    pts=float(input('Digite sua média de pontuação: '))
    ast=float(input('Digite sua média de assistencias: '))
    reb=float(input('Digite sua média de rebotes: '))
    tpts=float(input('Digite sua média de bolas triplas por jogo: '))
    if pts > maiorpts: 
        nmaiorpts= n
        maiorpts=pts 
    if pts < menorpts:
        nmenorpts= n
        menorpts= pts
    if ast > maiorast:
        nmaiorast= n
        maiorast= ast
    if ast < menorast:
        nmenorast = n
        menorast= ast 
    if reb > maiorreb:
        nmaiorreb= n
        maiorreb= reb 
    if reb < menorreb:
        nmenorreb= n
        menorreb= reb 
    if tpts > maiorreb:
        nmaiortpts= n
        maiortpts= tpts 
    if tpts < menortpts:
        nmenortpts= n
        menortpts= tpts 
    c= c + 1
print(f'O jogador {nmaiorpts} é aquele que contém a maior pontuação dentre os {qtd} jogadores com aproximadamente {maiorpts}pts de média por jogo!')
print(f'O jogador {nmenorpts} é aquele que contém a menor pontuação dentre os {qtd} jogadores coma aproximadamente {menorpts}pts de média por jogo')
print(f'O jogador {nmaiorast} é aquele que contém a maior série de assistencias dentre os {qtd} jogadores com aproximadamente {maiorast}ast de média por jogo!')
print(f'O jogador {nmenorast} é aquele que contém a menor série de assistencias dentre os {qtd} jogadores coma aproximadamente {menorast}ast de média por jogo')
print(f'O jogador {nmaiorreb} é aquele que contém o  maior número de rebotes dentre os {qtd} jogadores com aproximadamente {maiorreb}reb de média por jogo!')
print(f'O jogador {nmenorreb} é aquele que contém o menor número de rebotes dentre os {qtd} jogadores coma aproximadamente {menorreb}reb de média por jogo')
print(f'O jogador {nmaiortpts} é aquele que contém a maior pontuação em bolas triplas dentre os {qtd} jogadores com aproximadamente {maiortpts} de média por jogo!')
print(f'O jogador {nmenortpts} é aquele que contém a menor pontuação em bolas triplas dentre os {qtd} jogadores coma aproximadamente {menortpts} de média por jogo')

        
        