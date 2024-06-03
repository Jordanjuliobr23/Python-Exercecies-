print('=-'*100)
print('ÁREA DO RETANGULO')
def area (altura, largura):
    return altura * largura 

h=float(input('Digite a  altura do retangulo em cm: '))
l=float(input('Digite a largura do triangulo em cm: '))
r= area (h,l)
print('A área do retangulo de {}cm de altura e {}cm de largura será de aproximadamente: {:.2f}cm  '.format(h,l,r))

