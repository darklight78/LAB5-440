import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 #send 4096 bytes each time step

host= "192.168.43.44" #ip address of server, the receiver
port= 5002

filename= "file.txt" #name of the file that want to send
filesize= os.path.getsize(filename)

s=socket.socket()
s.connect((host,port))
print("connected")

s.send(f"{filename}{SEPARATOR}{filesize}".encode("utf-8"))
#send the filename and file size
progress= tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, 
unit_divisor=1024)
with open(filename, "rb") as f:
   for _ in progress:
     bytes_read= f.read(BUFFER_SIZE)
     if not bytes_read:
      break

     s.sendall(bytes_read)
     progress.update(len(bytes_read)) #update the progress bar

s.close()
