data=input('Digite uma data no formato 00/00/0000: ')
dia=data[0: 2]
ano=data[6: ] 
mes=data[3: 5] 
if mes == '01':
    print(f'{dia} de Janeiro de {ano}') 
if mes == '02':
    print(f'{dia} de Fevereiro de {ano}')
if mes == '03':
    print(f'{dia} de março de {ano} ')
if mes == '04':
    print(f'{dia} de Abril de {ano} ') 
if mes == '05':
    print(f'{dia} de Maio de {ano} ')
if mes == '06':
    print(f'{dia} de Junho de {ano} ')
if mes == '07':
    print(f'{dia} de Julho de {ano} ')
if mes == '08':
    print(f'{dia} de Agosto de {ano} ')
if mes == '09':
    print(f'{dia} de Setembro de {ano} ')
if mes == '10':
    print(f'{dia} de Outubro de {ano} ')
if mes == '11':
    print(f'{dia} de Novembro de {ano} ')
if mes == '12':
    print(f'{dia} de Dezembro de {ano} ')