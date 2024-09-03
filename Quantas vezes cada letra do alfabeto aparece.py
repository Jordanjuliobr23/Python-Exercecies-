try:
    FILENAME=input('Digite o nome d eum arquivo txt (nome_arquivo.txt) ou o caminho (C:\\Users\\JORDAN\\Downloads\\nome_arquivo.txt): ') 
    Fd=open(FILENAME,'r')
    alfabeto= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    contagem= {letra: 0 for letra in alfabeto}
    for linha in Fd:
        for letra in linha:
            if letra in alfabeto:
                contagem[letra] += 1
    Fd.close()
    print('=-'*100)
    print('Contagem de cada letra do arquivo solicitado: ')
    for letra, count in contagem.items():
        print(f'{letra}: {count}')
except FileNotFoundError:
    print('O arquivo não foi enconrtrado pelo programa :(')
