print('=-'*100)
print('IMC - INDICE DE MASSA CORPORAL')
p=float(input('Digite seu peso: '))
h=float(input('Digite sua altura: '))
imc= p/(h**2)
if imc < 16.9:
    print('Seu peso corresponderá a {}KG, sua altura a {}m e um índice de massa corporal de {:.2f}'.format(p,h,imc))
    print('Preocupante! Suas estatísticas corresponde a classificação abaixo do peso!')
if 17 <= imc <= 24.9:
    print('Seu peso corresponderá a {}KG, sua altura a {}m e um índice de massa corporal de {:.2f}'.format(p,h,imc))
    print('Ótimo! Suas estatísticas lhe classificam com peso normal!')
if 25 <= imc <= 29.9:
    print('Seu peso corresponderá a {}KG, sua altura a {}m e um índice de massa corporal de {:.2f}'.format(p,h,imc))
    print('Bom! Suas estatísticas lhe classificam como acima do peso!')
if 30 <= imc <= 34.9:
    print('Seu peso corresponderá a {}KG, sua altura a {}m e um índice de massa corporal de {:.2f}'.format(p,h,imc))
    print('Cuidado! Suas estatísticas lhe classificam com obesideade grau I')
if 35 <= imc <= 40:
    print('Seu peso corresponderá a {}KG, sua altura {}m e um índice de massa corporal de {:.2f}'.format(p,h,imc))
    print('Preocupante! Suas estatísticas lhe classificam com obesidade grau II!')
if imc > 40: 
    print('Seu peso corresponderá a {}KG, sua altura {}m e um índice de massa corporal de {:.2f}'.format(p,h,imc))
    print('Muito preocupante! Suas estatísticas lhe classificam com obesidade grau III!')
print('=-'*100)
print('Meus contatos: ')
print('Gmail pessoal: Jordanjulio325@gmail.com')
print('Gamil Acadmeico: Jordan.j@escolar.edu.ifrn.br')
print('GitHub: Jordanbr23')
print('Instagram: @jordanjuliofrancelino')
