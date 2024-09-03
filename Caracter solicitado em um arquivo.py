try:
    FILENAME=input('Digite o nome do arquivo (nome_arquivo.txt) ou (C:\\Users\\JORDAN\\Downloads\\nome_arquivo.txt): ')
    Fd=open(FILENAME,'r')
    user=input('Digte qualquer caracter para o programa procurar no arquivo: ')
    contador=0
    for linha in Fd:
        for caracteres in linha:
            if caracteres in user:
                contador += 1 
    Fd.close() 
    print(f'O caracter {user} aparece {contador}x no arquivo solicitado!')
except FileNotFoundError:
    print('O arquivo solicitado não existe :(')
