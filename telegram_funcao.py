import socket
import threading
import sys
import requests
import time

API_TOKEN = "8046038346:AAFs3zVmGc3kF_c9BSWoTRMghZOFNh1nxcY"  # Substitua pelo seu token da API do Telegram
API_URL = f"https://api.telegram.org/bot{API_TOKEN}/"

def mensagens_telegram ():
    offset = 0
    while True:
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
    
