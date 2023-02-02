import socket, sys


for porta in range(1, 65535):
    meusocker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = meusocker.connect_ex((sys.argv[1], porta))
    if(res == 0):
        print('Porta aberta: {porta}')
        meusocker.close()

