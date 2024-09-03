try:
    vogais='aeiouAEIOU'
    FILENAME=input('Digite o nome do arquivo (nome_arquivo.txt) ou o caminho para o arquivo (C:\\Users\\JORDAN\\Downloads\\nome_arquivo.txt): ') 
    Fd=open(FILENAME,'r')
    count=0
    for linha in Fd:
        for caractere in linha:
            if caractere in vogais:
                count += 1 
    Fd.close() 
    print(f'O arquivo solicitado possui {count} vogais.') 
except FileNotFoundError:
    print('O arquivo não foi encontrado. Verifique novamente')