print('=-'*100)
print('COMPETIÇÃO DE SALTO!')
qtd=int(input('Digite a quantidade de atletas que partciparam da competição: '))
x=0
soma= 0
maiorsalto=0 
menorsalto=10000
maiormedia=0
maiormedianome=0
c= 0
while c < qtd:
    n=str(input('Digite o nome do atleta: '))
    s1=float(input('Primeiro Salto em metros: '))
    if s1 > maiorsalto:
        maiorsalto= s1 
    if s1 < menorsalto: 
        menorsalto= s1
    else: 
        soma= soma + s1
        x= x + 1
    s2=float(input('Segundo salto em metros: '))
    if s2 > maiorsalto:
        maiorsalto= s2
    if s2 < menorsalto:
        menorsalto = s2
    else: 
        soma= soma + s2
        x= x + 1
    s3=float(input('Terceiro salto em metros: '))
    if s3 > maiorsalto: 
        maiorsalto = s3
    if s3 < menorsalto:
        menorsalto = s3
    else: 
        soma= soma + s3
        x= x + 1
    s4= float(input('Quarto salto em metros: '))
    if s4 > maiorsalto:
        maiorsalto = s4 
    if s4 < menorsalto:
        menorsalto = s4
    else: 
        soma= soma + s4
        x= x + 1
    s5=float(input('Quinto salto em metros: '))
    if s5 > maiorsalto:
        maiorsalto= s5  
    if s5 < menorsalto:
        menorsalto= s5  
    else: 
        soma= soma + s4
        x= x + 1
    media= soma/x 
    if media > maiormedia:
        maiormedia= media
        maiormedianome= n
    c= c + 1
    print(f'Stats do atleta {n}') 
    print(f'Primeiro Salto: {s1}m')
    print(f'Segundo Salto: {s2}m')
    print(f'Terceiro Salto: {s3}m')
    print(f'Quarto Salto: {s4}m')
    print(f'Quinto Salto {s5}m')
    print('=-'*20)
    print(f'Melhor salto: {maiorsalto}m')
    print(f'Pior salto:{menorsalto}m ')
    print('Media dos demais saltos: {}m'.format(media))
print('=-'*20)
print('Vencedor: {}'.format(maiormedianome))
print('Média do atleta: {:.2f}'.format(maiormedia))
    