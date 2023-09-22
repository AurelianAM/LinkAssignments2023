import socket
import time
import random
import string


# function to build a random string (with lots of ',')
def randomString():
    return ','.join(random.choice(string.printable) for i in range(random.randint(50, 500)))
def speakWithServer(client_socket, message):
    t0 = time.time() # get the time wright before sending the message
    # send message to the server (in bytes)
    for i in range(nbrOfRequests):
        ti = time.time()
        client_socket.sendto(bytes(message, 'utf-8'), ('127.0.0.1', 21060))
        # receive message from server
        answerMessage, address = client_socket.recvfrom(65535)
        # decode the message
        answerMessage = answerMessage.decode('utf-8')
        # print the message and the time needed by the server (in miliseconds)
        print(f'[CLIENT]:[{(time.time() - ti)*1000:.2f}ms] response from server is: {answerMessage}')
    print(f'Average response time: {(time.time() - t0)*1000/nbrOfRequests:.2f}ms')
    # create UDP Socket object


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nbrOfRequests = 10
hardCodedMessage = 'Hello, server, it is me, the client!'

speakWithServer(client_socket, randomString())

speakWithServer(client_socket, hardCodedMessage)

client_socket.close() # close the connection
