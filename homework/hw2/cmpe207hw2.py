import socket
import sys


HOST = '127.0.0.1'
PORT = 55555

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print(sys.stderr, 'connection from', client_address)

        # Receive data in small chunks and retransmit it
        while True:
            connection.sendall("How are you?")
    finally:
        # Clean up the connection
        connection.close()
