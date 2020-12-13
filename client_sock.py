import socket

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 8889

s.connect(('192.168.43.44', port))

s.sendall(b'Hi, saya client. terima kasih!');

data= s.recv(1024)

print(data)

s.close()
