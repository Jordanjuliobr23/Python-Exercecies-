print('=-'*100)
try: 
    try: 
        num=int(input('Digite um número inteiro: '))
    except ValueError:
        print('ERRO! Por favor, digite um número INTEIRO válido!')
    try:  
        n=float(input('Digite um número decimal: '))
    except ValueError:
        print('ERRO! Por favor, digite um número DECIMAL válido!')
except ValueError:
        print('ERRO! Por favor, digite um valor válido!')
print(f'O número decimal digitado foi {n} e o inteiro foi {num} ')