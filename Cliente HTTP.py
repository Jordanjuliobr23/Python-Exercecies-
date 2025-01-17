import socket
print('=-'*50)
print('CLIENTE HTTP')

porta = 80
DIRETORIO = 'files/'

metodo=input('Digite o método HTTP (GET, POST): ').strip().upper()
host=input('Digite o host: ').strip()
path=(input('Digite o caminho (ex: /image/png): ')).strip()

tcpSock= socket.socket(socket.AF_INET,socket.SOCK_STREAM )
tcpSock.connect((host, porta))

tcpSock.sendall(f"{metodo} {path} HTTP/1.1\r\n".encode()) # enviando o método e o caminho
tcpSock.sendall(f"Host: {host}\r\n".encode()) # solicitando o cabeçalho
tcpSock.sendall("\r\n".encode()) # solicitando a linha branco indicando o fim do cabeçalho

resposta= b'' # recebe a resposta do servidor
while True: 
    dados= tcpSock.recv(4096)
    if not dados:
        print(f'ERRO! Não foram encontrados dados a serem extraidos d servidor {host}!')
    resposta += dados
    resposta= resposta.decode()
    print(resposta)


    tcpSock.close



