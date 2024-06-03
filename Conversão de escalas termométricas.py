print('=-'*100)
print('Conversor de temperaturas personalizado')
def temperatura (celsius,fahrenheit):
    return celsius * (fahrenheit * 1.8) + 32 
t=float(input('Digite a temperatura em Celsius para ser convertido para Fahrenheit:  '))
resultado= temperatura ()
print('A temperatura de {}C, corresponde a {:.2f}F'.format(t,resultado))