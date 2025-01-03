import socket 
import os  

server= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1" 
porta= 1234
server_address= (ip, porta)
DIRETORIO= 'files/'

server.bind(server_address) 

print(f'Servidor aguardando solicitações em {ip}:{porta}')
 
try:
    while True:
        filename, client_address = server.recvfrom(2048)
        filename = filename.decode()
        path = os.path.join(DIRETORIO, filename)

        if os.path.isfile(path):
            tam = os.path.getsize(path)
            print(f'Enviando o tamanho do arquivo {filename} ({tam} bytes) ao cliente {client_address}')
            server.sendto(str(tam).encode(), client_address)

            with open(path, 'rb') as file:
                while chunk := file.read(2048):
                    server.sendto(chunk, client_address)
            print(f'Arquivo {filename} enviado com sucesso para {client_address}')
        else:
            print(f'O arquivo {filename} não foi encontrado no diretório {DIRETORIO}')
            server.sendto(b'0', client_address)

except Exception as e:
    print(f"Erro no servidor: {e}")
finally:
    server.close()
            




        