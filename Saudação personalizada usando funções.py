print('=-'*100) 
# criação da função 
def saudacao1 (nome,hora):
    if hora == 'manhã':
        saudacao = 'Bom dia'
    elif hora == 'tarde':
        saudacao = 'Boa tarde'
    elif hora == 'noite':
        saudacao = 'Boa noite'
    else:
        saudacao= 'Olá'
    
    print(f'{saudacao}, {nome}!')
    
n=str(input('Digite seu nome: '))
h=str(input('Digite o horário do dia (manhã, tarde, noite): '))

saudacao1(n,h)

