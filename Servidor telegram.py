import socket
import threading
import sys
import requests
import time



API_TOKEN ='/pr20242 - Jordan'  
API_URL = f'https://api.telegram.org/bot{API_TOKEN}/getUpdates'

def broadCastMensage(my_conn, my_addr, msg):
    len_msg = len(msg).to_bytes(2, 'big')
    msg = len_msg+msg
    
    for conn in all_conn:
        if conn != my_conn: #nao manda a msg para o proprio cliente que esta enviando
            try:
                conn.send(msg)
            except:
                print(f"falha no envio a {my_addr}")



def mensagens_telegram ():
      print("procurando novas mensagens")
      resposta = requests.get(f'{API_URL}getUpdates?offset={offset}')
      mensagens = resposta.json().get('result', [])
      for mensagem in mensagens:
            chat_id = mensagem['message']['chat']['id']
            user_name = mensagem['message']['chat']['first_name']
            text = mensagem['message']['text']
            
            print(f"Nova mensagem de {user_name} ({chat_id}): {text}")
            offset = mensagem['update_id'] + 1
      time.sleep(2)

def main():
    print("ligado")
    mensagens_telegram()

main()
    



def client (my_conn, my_addr): #adrr ip e PORT conn = concexao atual
    print(f'Novo cliente conectado: {my_addr
    }')
    all_conn.append(my_conn)
    prefix = f"{my_addr} digitou: ".encode('utf-8')
    
    while True:
        try:
            len_msg = my_conn.recv(2) #2 bytes do tamanho
            len_msg = int.from_bytes(len_msg,'big')
            msg = prefix + my_conn.recv(len_msg)
            broadCastMensage(my_conn, my_addr, msg)
        except:
            print ("Falha no processamento do cliente ", my_addr, "saindo.")
            break
        
    print(f"Cliente {my_addr} desconectado.") 
    all_conn.remove(my_conn)
    my_conn.close()

  
HOST = 'localhost' 
PORT = 8080

all_threads = []
all_conn = []

def startServer():
    try:
        sock = socket.socket() #flexibilidade de endereço
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #definida em socket e reutiliza PORTs ja conectadas (1 true)
        sock.bind((HOST, PORT
        ))
        sock.listen
        ()
        print("Aguardando conexões...")
    except OSError:
        print("Erro, endereço em uso.") #tratamento para o erro de endereço do terminal
        sys.exit(2)
    return sock

def main():
    sock = startServer()

    while True:
        try:
            conn, addr = sock.accept()
            t = threading.Thread(target=client, args=(conn, addr)) #config das all_threads
            all_threads.append(t)
            t.start()
        except: 
            break
        
    for t in all_threads:
        t.join() #recolhe os processors antes de fecha  sock.close()
    sock.close()

main()        