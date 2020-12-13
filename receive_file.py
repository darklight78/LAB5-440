
#reference:https://www.thepythoncode.com/article/send-recive-files-using-sockets-python
import socket
import tqdm
import os

SERVER_HOST= "192.168.43.44"
SERVER_PORT= 5002
BUFFER_SIZE= 4096
SEPARATOR= "<SEPARATOR>"

s= socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

client_socket, address= s.accept()
print(f"[+] {address} is connected.")

#received file info using client socket not server socket
received= client_socket.recv(BUFFER_SIZE).decode()
filename, filesize= received.split(SEPARATOR)

#remove absolute path if there is
filename= os.path.basename(filename)

#convert to integer
filesize= int(filesize)

#start receiveing the file from socket and write to file stream
progress= tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True,
unit_divisor=1024)
with open(filename, "wb") as f:
   for _ in progress:
   #read 1024 bytes from the socket(receive)
     bytes_read= client_socket.recv(BUFFER_SIZE)
     if not bytes_read:
     #nothing is received file transmitting done
       break

     #write to the file the bytes received
     f.write(bytes_read)
     #update the progress bar
     progress.update(len(bytes_read))

client_socket.close()
s.close()


