from random import randint
from time import sleep
pc= randint (0,5)
print('Pensarei em um número de 0 a 5, tente adivinhar....')
print('---'*20)
player=int(input('Em que número pensei?...'))
print('PROCESSANDO....')
sleep(3)
if player == pc:
    print('VOCE ME VENCEU!, me esforçarei mais no nosso próximo duelo....')
else:
    print('I WIN! Tente de novo quando tiver mais sorte!')