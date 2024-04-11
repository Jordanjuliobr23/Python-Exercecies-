print('=-'*100)
print('Supershow - Supermercado')
print('Promoção do açogue: ')
print ('                Até 5kg            Acima de 5kg   Código')
print('Filé Duplo    R$4.90 por Kg         R$5.80 por Kg   100')
print('Alcatra       R$5.90 por Kg         R$6.80 por Kg   101')
print('Picanha       R$6.90 por Kg         R$7.80 por Kg   102')
n=str(input('Digite o código da carne solicitado pelo cliente: '))
k=int(input('Digite o peso da carne solicitada pelo cliente: '))
qtd=int(input('Digite a quantidade de carne comprada: '))
c=int(input('Digite 1 caso a compra for realizada no cartão Supershow,se não digite qualquer outro número inteiro: '))
t=str(input('Digite o tipo de pagamento: '))
tot=0
p=0
if c == 0: 
    if n== '100' and k <= 5: 
        p= qtd *  4.90
        tot= tot + p
        print('O tipo da carne é um Filé Duplo')
        print(f'O Filé Duplo de {k}Kg custará R${p}')
        print(f'O tipo de pagamento é {t}')
    elif n=='100' and k >= 5:
        p= qtd * 5.80 
        tot= tot + p
        print('O tipo da carne é um Filé Duplo')
        print(f'O Filé Duplo de {k}Kg custará R${p} ')
        print(f'O tipo de pagamento é {t}')
    elif n=='101' and k <= 5:
        p= qtd * 5.90
        tot= tot + p
        print('O tipo da carne é Alcátra')
        print(f'A Alcátra de {k}Kg custará R${p}') 
        print(f'O tipo de pagamento é {t}') 
    elif n=='101' and k >= 5:
        p= qtd * 6.80
        tot= tot + p
        print('O tipo da carne é Alcátra')
        print(f'A Alcátra de {k}Kg custará R${p}')
        print(f'O tipo de pagamento é {t}')
    elif n=='102' and k <= 5:
        p= qtd * 6.90 
        tot= tot + p
        print('O tipo da carne é Picanha')
        print(f'A Picanha de {k}Kg custará R${p}')
    elif n=='102' and k >= 5:
        p= qtd * 7.80
        tot= tot + p
    print('O tipo da carne é Picanha')
    print(f'A Picanha de {k}Kg custará R${p}')
    print(f'O tipo de pagamento é {t}')
if c==1: 
    d= p + (p* (5/100))
    if n== '100' and k <= 5: 
        p= (qtd *  4.90) - d
        tot= tot + p
        print('O tipo da carne é um Filé Duplo')
        print(f'Com o desconto do cartão Supershow de 5%, o preço será de {p}')
        print(f'O tipo de pagamento é {t}')
    elif n=='100' and k >= 5:
        p= (qtd * 5.80) - d
        tot= tot + p
        print('O tipo da carne é um Filé Duplo')
        print(f'Com o desconto do cartão Supershow de 5%, o preço será de {p}')
        print(f'O tipo de pagamento é {t}')
    elif n=='101' and k <= 5:
        p= (qtd * 5.90) - d
        tot= tot + p
        print('O tipo da carne é Alcátra')
        print(f'Com o desconto do cartão Supershow de 5%, o preço será de {p}')
        print(f'O tipo de pagamento é {t}') 
    elif n=='101' and k >= 5:
        p= (qtd * 6.80) - d
        tot= tot + p
        print('O tipo da carne é Alcátra')
        print(f'Com o desconto do cartão Supershow de 5%, o preço será de {p}')
        print(f'O tipo de pagamento é {t}')
    elif n=='102' and k <= 5:
        p= (qtd * 6.90) - d
        tot= tot + p
        print('O tipo da carne é Picanha')
        print(f'Com o desconto do cartão Supershow de 5%, o preço será de {p}')
        print(f'O tipo de pagamento é {t}')
    elif n=='102' and k >= 5:
        p= (qtd * 7.80) - d
        tot= tot + p
        print('O tipo da carne é Picanha')
        print(f'Com o desconto do cartão Supershow de 5%, o preço será de {p}')
        print(f'O tipo de pagamento é {t}')
        