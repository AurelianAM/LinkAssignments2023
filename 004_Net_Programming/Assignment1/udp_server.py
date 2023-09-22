import socket

# create UDP Socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind server to the IP and port - and listen
server_socket.bind(('127.0.0.1', 21060))
print('[UDP Server]: Listening at: ', server_socket.getsockname())

# while loop - infinite iterations
while True:
    # receive a 'message' from the 'address'
    message, address = server_socket.recvfrom(65535)
    print('[UDP Server]: Received data from address: ', address)

    # decode the message
    message = message.decode('utf-8')
    # build the answer for client
    responseMessage = str(len(message.split(',')))
    # send answer message (in bytes) to the client at 'address'
    server_socket.sendto(bytes(responseMessage, 'utf-8'), address)

server_socket.close()   # just in case we will redefine the while loop
