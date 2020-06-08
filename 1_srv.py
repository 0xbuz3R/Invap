import socket

srv_host = '127.0.0.1'

srv_port = 9003


# Create TCP SERVER

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

print('[+]Connecting to the Server :')

sock.bind((srv_host , srv_port))

sock.listen(1)

while True:

    try:
        print('[+]Waiting for client to connect')

        connection , port  = sock.accept()
        print('[+]Connected to the Client Server:{} \nPort:{}'.format(connection , port))

 

        data = connection.recv(16)
        print('Rececived {!r}'.format(data))
        
        if data:

            print('sending all data to client')
            connection.sendall(data)

        else:
            print('No data')
            break
            
 

    except socket.error as error:
        sock.close()

        

