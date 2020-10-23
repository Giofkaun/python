import socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '192.168.1.106'
porta = 666
cliente.connect((ip, porta))
try:
    while True:
        msg=input('\ndigite a mensagem ')
        cliente.send(msg.encode('utf-8'))
        resposta = cliente.recv(2048)
        print ('\n', resposta)
        if resposta=='fechar' :
            break
except Exception as error:
    print ('falha ', error)
