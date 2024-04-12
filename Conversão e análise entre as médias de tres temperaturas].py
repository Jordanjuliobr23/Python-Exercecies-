print('=-'*100)
print('CONVERSOR DE TEMPERATURA: ')
qtd=int(input('Digite a quantidade de vezes que deseja realizar a conversão das temperaturas: '))
c=0
soma=0
maiormedia=0
menormedia=1000
media=0
while c < qtd:
    c=float(input('Digite 1 para converter uma temperatura celsius para as demais (Digite outro número se não): '))
    f=float(input('Digite 2 uma temperatura Fahrenheit para as demais (Digite outro número se não): '))
    k=float(input('Digite 3 uma temperatura Kelvin para as  demais (Digite outro número se não): '))
    if c== 1: 
        t=float(input('Digite a temperatura em graus Celsius: '))
        convert1= (t * 1.8) + 32
        print(f'A conversão da temperatura de {t} graus Celsius para graus Fahrenheit corresponde a {convert1}')
        convert2= t + 273.15
        print(f'A conversão da temperatura de {t} graus Celsius para graus Kelvin corresponde a {convert2}')
        soma= soma + convert1 + convert2
        media= soma/2
        if media > maiormedia:
            maiormedia=media
        if media < menormedia:
            menormedia=media
    if c != 1:
        print('Prosseguindo para a próxima temperatura.....')
    if f == 2: 
        t=float(input('Digite a temperatura em graus Fahrenheit: '))
        convert1= (t-32) * 1.8
        print(f'A conversão da temperatura de {t} graus Fahrenheit  para graus Celsius corresponde a {convert1}')
        convert2= convert1 + 273.15
        print(f'A conversão da temperatura de {t} graus Fahrenheit  para graus Kelvin corresponde a {convert2}')
        soma= convert1 + convert2
        media= soma/2 
        if media > maiormedia:
            maiormedia = media 
        if media < menormedia:
            menormedia= media 
    if f != 2: 
        print(f'Prosseguindo para a próxima temperatura....')
    if k == 3: 
        t=float(input('Digite a temperatura em graus Kelvin: '))
        convert1= t- 273.15
        print(f'A conversão da temperatura de {t} graus Kelvin para graus Celsius corresponde a {convert1}')
        convert2= convert1 * 1.8 + 32
        print(f'A conversão da temperatura de {t} graus Kelvin para graus Fahrenheit corresponde a {convert2}')
        soma= soma + convert1 + convert2
        media= soma/2
        if media > maiormedia:
            maiormedia= media 
        if media < menormedia:
            menormedia= media 
    c= c + 1 
print(f'A maior média entre as temperaturas foi {maiormedia}')  
print(f'A menor média entre as temperaturas foi {menormedia}')  