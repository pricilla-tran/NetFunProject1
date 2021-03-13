#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM) # Create TCP Socket
# Prepare a server socket
#Fill in start
# Identifier for a message/request: browser will assume port 80 and the webpage will be shown if your server is listening at port 80
serverPort = 6789
serverName = '10.0.0.32' # The destination, add IP address here
serverSocket.bind((serverName, serverPort)) # Assign serverPort to TCP socket
serverSocket.listen(1) # To listen for at most one connection at a time (TCP requests)
print('Ready to serve...')

#Fill in end
while True:
    #Establish the connection
    # Server waits on accept() for incoming requests
    connectionSocket, addr =  serverSocket.accept() #Fill in start              #Fill in end
    try:
         # To recieve data from socket, the buffer size is 1024 bytes
         # Read bytes from socket
         message =  connectionSocket.recv(1024) #Fill in start          #Fill in end
         # Extract path of request object from the message
         filename = message.split()[1]

         # Open requested object from the second character since first is '\' since it is looking into the path
         f = open(filename[1:])
         # Read the file and store the all the content from the requested file
         outputdata = f.read() #Fill in start       #Fill in end

        #Send one HTTP header line into connection socket
        # HTTP/1.1 *sucessful-request* \r\n\r\n
        # b stands for bytes
        # \r\n\r\n is a line separator
        # Fill in start
         connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')
        # Fill in end
        # Send the content of the requested file to the connection socket and encode it
         for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode()) # Sends each character of outputdata
         connectionSocket.send("\r\n".encode()) # Sends encoded string to socket object
         # Output message when the file is found
         print('Success!')
         connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        print ('404 Not Found')
        connectionSocket.send(b'HTTP/1.1 404\r\n\r\n')
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()
sys.exit()# Terminate the program after sending the corresponding data
