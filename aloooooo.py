import socket
import time

HOST = input('\ndigite um ip ')

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for PORT in range(1, 65535):
    time.sleep(0.1)

    if tcp.connect_ex((HOST, PORT))==0:
	    print('open - ', PORT)
