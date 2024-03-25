print('ESSE PROGRAMA CÁLCULA A TARIFA DE UM ESTACIONAMENTO PROPORCIONAL AO TEMPO')
t=float(input('Digite os minutos em que o veículo ficou no espaço do estacionamento:  '))
print('O veículo ficou estacionado durante ',t )
h= t // 60
# valor atribuido a primeira hora
if t <= 60: 
    v= 8.00 
    print('De acordo com a política do estacionamento, o cliente pagará ',v)
# valor atribuido a primeira hora ou a fração da segunda hora
elif 61 <= t <= 120: 
    v= 8.00 * 2 
    print('De acordo com a política do estacionamento, o cliente pagará ',v) 
# valor atribuido a segunda hora ou afração da terceira hora
elif 121 <= t <= 180:
    v= 16.0 + 5.0
    print('De acordo com a política do estacionamento, o cliente pagará ',v)
# valor atribuido a terceira hora ou a fração quarta hora 
elif 181 <= t <= 240: 
    v= 16.0 + (5.0 *2)
    print('De acordo com a política do estacionamento,o cliente pagará ', v)
elif 241 <= t <= 660:
    v= (16.0 + 10.0) + 3.0 * (1 + h - 4)
    print('De acordo com a política do estacionamento, o cliente pagará ', v)
elif t >= 720: 
    v= 30.00
    print('De acordo com a política do estacionamento, o cliente pagará ', v)


   

