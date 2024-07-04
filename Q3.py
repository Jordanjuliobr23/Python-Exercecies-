print('=-'*100)
# Aluno: Jordan Júlio Francelino da Silva
# Matrícula: 20241014050014
# Questão 3 - Fatores comuns de um número primo 
# 1- Criação de uma variável que solicite ao usuário que ele digite um número qualquer 
num=int(input('Solicite um número qualquer para serem obtidos seus fatores primos: '))
# 2- Criação da variável soma para armazenar e somar os fatores primos do número solicitado pelo usuário
soma= 0
# 3 - Criação da variável div, recebendo o valor 2 inicialmente. A função dessa variável é servir como uma condição aos números candidatos a serem divisores para provar se eles são divisiveis pelo divisor atual, divisor esse que iniciará do valor 2 até o número solicitado pelo usuário. Se caso eles forem divisiveis pelo divisor atual, ele será considerado um fator primo.
div = 2
# 4- Criação de um laço de repetição while para iniciar o processo de seleção dos fatores primos do número solicitado.
# 4.5 - Criação de uma variável separada para não influenciar o número digitado pelo usuário anteriormente.
n= num 
while n > 1:
    # 5- Criação da condição que irá selecionar os fatores primos. Se o número digitado pelo usuário for divisível pelo atual divisor (inicialmente é 2), ele será armazenado na variável soma.
    while n % div == 0: 
        soma= soma + div
    # 6- Divide-se o numero pelo divisor para reduzir o número e encontrar novos divisores. 
        n= n // div 
    # 7 - Por fim, haverá a adição do 1 na variável div para que o programa venha a testar o possível divisor seguinte. Assim, após o programa ter trabalho até então com o divisor 2, agora ele seguirá para o divisor 3. 
    div= div + 1
print(f'A soma dos fatores primos do número {num} corresponde a: {soma} ')