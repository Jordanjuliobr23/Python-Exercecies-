print('='*200)
print('Desempenho do veículo em uma viagem: ')
n=str(input('Digite o modelo do veículo: '))
t=float(input('Por favor o tempo de viagem em minutos: ')) 
l=float(input('Por favor informe a quantidade de litros de combustível gasto em litros: '))
p=float(input('O preço do litro do combustível em R$: '))
d=float(input('Digite a distancia pecorrida em Km/h: '))
h= t * 3.6
vm= d/t 
c= d*p 
dp1= d // l
dp2= l/h
dp3= p /d 
print('Dados de um computador de bordo: ')
print( 'Apresentação do desempenho do veículo {}'.format(n))
print('A velocidade média do veículo durante a viagem foi Km/h ',vm )
print('O custo da viagem foi de R${:.2f}'.format(c))
print('O desempenho do carro na viagem foi de {}Km/l, {}l/h e {}R$/KM'.format(dp1,dp2,dp3)) 
print('='*200)
print('Contatos: ')
print('Gmail pessoal: Jordanjulio325@gmail.com')
print('Gmail academico: Jordan.j@escolar.ifrn.edu.br')
print('Instagram: @jordanjuliofrancelino')