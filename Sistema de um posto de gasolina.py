print('=-'*100)
print('Posto Guanabara')
print('A-Álcool  -  G-Gasolina')
print('R$ 3.43   -  R$ 6.78')
a=int(input('Digite 1 se deseja colocar álcool ou 0 se não deseja colocar álcool: '))
if a == 1: 
    v=float((input('Digite o valor do litro de álcool/Gasolina: R$')))
    l=int(input('Digite a quantidade de litros correspondente ao álcool: '))
    p= v * l
    if l > 20: 
        a1= p * (5/100)
        d1= p- (p * (5/100))
        print('Como o álcool atribuído ao veículo do cliente é superior a 20 litros, o cliente terá um desconto de 5%')
        print('Assim, o preço sem desconto de {:.2f}, sofrerá uma redução de {:.2f}, estando com o valor de {:.2f}'.format(p,a1,d1)) 
    if l <= 20: 
        a2= p * (3/100)
        d2= p - (p* (3/100))
        print('Como o álcool atribuído ao veículo do cliente é inferior a 20 litros, o cliente terá um desconto de 3%')
        print('Assim, o preço sem desconto de {:.2f}, sofrerá uma redução de {:.2f}, estando com o valor de {:.2f}'.format(p,a2,d2)) 
    if a != 0 and a !=1:
        print('O programa está encerrado pelos valores atribuidos serem diferentes de 0 e 1!')
if a == 0:
    print('Iremos prosseguir o programa, por favor aguarde...')
    g=int(input('Digite 2 se deseja colocar gasolina (Qualquer outro número colocado encerrará o sistema): '))
    if g == 0: 
        print('O programa não irá prosseguir pois o cliente não escolheu nem gasolina e nem álcool!')
    if g != 2 and g != 0:
        print('O programa está encerrado pelos valores atribuidos serem diferentes de 0 e 1!')
    if g == 2: 
        v=float((input('Digite o valor do litro de álcool/Gasolina: R$')))
        l=int(input('Digite a quantidade de litros correspondente a gasolina: '))
        p= v * l 
        if l > 20: 
            a1= p * (6/100)
            d1= p - (p*(6/100)) 
        print('Como a gasolina atribuida ao veículo do cliente é superior a 20 litros, o cliente receberá um desconto de 6%')
        print('Assim, o preço sem desconto de {:.2f}, sofrerá uma redução de {:.2f}, estando com o valor {:.2f}'.format(p,a1,d1))
    if l <= 20:
        a2= p * (4/100)
        d2= p - (p*(4/100))
        print('Como a gasolina atribuida ao veículo do cliente é inferior a 20 litros, o cliente receberá um desconto de 4%')
        print('Assim, o preço sem desconto de {:.2f}, sofrerá uma redução de {:.2f}, estando com o valor {:.2f}'.format(p,a2,d2))
