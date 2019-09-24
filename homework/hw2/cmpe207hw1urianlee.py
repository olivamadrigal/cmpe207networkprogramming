import socket

#tcp_ip = '94.142.241.111'
tcp_ip = '127.0.0.1'
#tcp_port = 23
tcp_port = 65432


buffer_size = 1024
message = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((tcp_ip, tcp_port))
i = 0
print("started")
while(i < 999):
    # s.send(message.encode('utf-8'))
    data = s.recv(buffer_size)
    f = open("hw2output.txt", "a")
    f.write(data.decode('utf-8'))
    f.close()
    # print("Received data:", data)
    i = i + 1
