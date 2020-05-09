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
    baglanti.close()

bagla()
kabul_et()
