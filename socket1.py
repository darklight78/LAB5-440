import socket

s= socket.socket()
print("berjaya buat socket")

port = 8888

s.bind(('',port))
print("berjaya bind socket di port: "+ str(port))

s.listen(5)
print("socket tengah menunggu client!")

while True:

	c, addr= s.accept()
	print("dapat capaian dari:" +str (addr))

	c.send(' Terima Kasih!')
	buffer= c.recv(1024)
	print(buffer)

c.close()
