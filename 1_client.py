import socket


# Create TCP client

sock = socket.socket(socket.AF_INET  , socket.SOCK_STREAM)

server = ('127.0.0.1', 9003)

print('[+]Connecting to Server : {} \nPort:{}'.format(*server))

sock.connect(server)


try:
    mssg = b'Hello Server :-)'
    print('[+]Sending Message : {}'.format(mssg))

    sock.sendall(mssg)

    amt_recv = 0

    amt_except = len(mssg)

    while amt_recv < amt_except:

        data = sock.recv(16)

        amt_recv += len(data)

        print("Recevied {!r}".format(data))
        


finally:

    print('[+] Connection Close')
    sock.close()
          

    




