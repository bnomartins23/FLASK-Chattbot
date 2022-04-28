import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} ffffff {os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} ffffff {os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} ffffff {os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} ffffff {os.linesep}')
    else:
        print(f'{os.linesep}{nome} Digite apenas 1,2,3,4 {os.linesep}')


def start():
    print('Olá! Seja bem vindo')

    nome = input('Digite o seu nome: ')
    while True:
            
        resposta = input(f'O que vc gostaria de aprender hoje? {os.linesep}[1] - Opção n 1 {os.linesep}[2] - Opção n 2 {os.linesep}[3] - Opção n 3')
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
