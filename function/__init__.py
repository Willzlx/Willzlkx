from Cmd.verify import *
import os
from time import sleep
import whois

def cadastro(lista):
    print('=-' * 15)
    c = 0
    for i in lista:
        print(f'[{c}] {i}')
        c += 1
    op = isint('Opção: ')
    return op


def cmdcommand():
    while True:
        try:
            command = str(input('Digite o comando (modo não administrador): '))
            if command == 'voltar':
                break
            else:
                os.system(command)
                sleep(0.5)
        except:
            print('Comando invalido ou não tem permissão')


def localizardominio():
    while True:
        url = str(input('URL/IP: ')).lower()
        if url == 'voltar':
            break
        descover = whois.whois(url)
        print(descover.text)