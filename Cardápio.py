print('=-'*100)
print('BARRACA DO CACHORRÃO')
print('CARDÁPIO')
print('ESPECIFICAÇÃO  - CÓDIGO - PREÇO ')
print('Cachorro Quente - 100 - R$3.50 ')
print('X-Tudo - 101 - R$4.00')
print('Misto Quente - 102 - R$2.50')
print('Caldo de Cana - 103 - R$ 1.50')
c1= 3.50
c2=4.00
c3=2.50
c4=1.50
qtd=int(input('Digite a quantidade de produtos comprados: '))
c=0
soma=0
while c < qtd: 
    n=int(input('Digite o código do produto comprado: '))
    if n == 100:
        print(f'O Cachorro Quente custou {c1}')
        soma= soma + c1
    elif n == 101:
        print(f'O X-Tudo custou {c2}')
        soma= soma + c2
    elif n == 102:
        print(f'O misto quente custa {c3}')
        soma= soma + c3
        print(f'O Misto Quente custa {c3}')
    elif n == 103:
        print(f'O Caldo de Cana custa {c4}')
        soma= soma + c4
    else:
        print('Código não registrado no cardápio! Tente outra vez!')
    c= c + 1 
print(f'O total a ser pago será {soma}')
        
        
