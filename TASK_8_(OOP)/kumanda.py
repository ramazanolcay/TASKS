import time
import random

class Kumanda():

    def __init__(self, tv_durum="Kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT"):

        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal= kanal

    def tv_ac(self):

        if (self.tv_durum  == "Kapalı"):
            print("Tv açılıyor")
            self.tv_durum="Açık"
        else:
            print("Tv zaten acik")

    def tv_kapat(self):
        
        if (self.tv_durum  == "Kapalı"):
            print("Tv zaten kapalı")
        
        else:
            print("Tv  kapanıyor...")
            self.tv_durum="Kapalı"
    

    def ses_ayari(self):

        while True:

            cevap=input("Sesi artır: > \nSesi azalt: < \nÇıkış: q ")

            if (cevap=='>'):
                if self.tv_ses>=100:
                    print("Max Ses")
                else:
                    self.tv_ses+=1
                    print("Tv Sesi: {}".format(self.tv_ses))
            
            elif (cevap=="<"):
                if (self.tv_ses<=0):
                    print("Min ses")
                
                else:
                    self.tv_ses-=1
                    print("tv_ses: {}",format(self.tv_ses))
            elif (cevap=="q"):
                break
            else:
                print("hatalı tuşlama")

    def kanal_ekle(self,kanal):
        
        if kanal in self.kanal_listesi:
            print("Bu kanal zaten ekli durumdadır")
        else:
            print("Kanal ekleniyor...")
            time.sleep(1)

            self.kanal_listesi.append(kanal)

            print("Kanal listesi: {}".format(self.kanal_listesi))

    def kanal_sec(self):

        rastgele=random.randint(0,len(self.kanal_listesi)-1)

        self.kanal=self.kanal_listesi[rastgele]
        print(self.kanal)
    
    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return "Tv_durum: {}\ntv_ses: {}\nkanal listesi: {}\nkanal:{}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

    def oto_kapanma(self):
        if (self.tv_durum  == "Açık"):
            try:
                sleep_time = int(input("Lütfen televizyonun kaç saniye sonra kapanacağını yazınız: "))
                time.sleep(sleep_time)
                kumanda.tv_kapat()
            except:
                print("Hatalı bir değer girdiniz.")
        else:
            print("TV zaten kapalı")
    
    def kanal_degis(self):
        kanal = input("Lütfen açmak istediğiniz kanalı yazınız: ")
        if kanal in self.kanal_listesi:
            self.kanal = kanal
            print(f"Açılan kanal: {self.kanal}")
        else:
            print("Olmayan bir kanal ismi girdiniz.")

    def mute(self):
        if self.tv_ses != 0:
            self.tv_ses = 0
            print("Ses Sıfırlandı")
        else:
            print("Ses zaten sıfır")

        
            

print("""

        1. TV aç
        2. TV kapat
        3. Ses Ayarları
        4. Kanal Ekle
        5. Açık Kanalı Öğren
        6. Kanal Sayısı
        7. TV Bilgileri
        8. Otomatik Kapatıcı
        9. Kanal Değiş
        10. Mute

Çıkmak için q'ya bas.

""")
kumanda=Kumanda()


while True:
    islem= input("İslem seçiniz: ")

    if islem =="q":
        print("Sonlandırılıyor")
        break 
    elif islem =="1":
        kumanda.tv_ac()
    
    elif islem=="2":
        kumanda.tv_kapat()

    elif islem=="3":
        kumanda.ses_ayari()
    
    elif islem=="4":

        kanal_isimleri=input("Kanal isimlerini lütfen , ile ayırarak giriniz: ")

        x=kanal_isimleri.split(",")

        for i in x:
            kumanda.kanal_ekle(i)
    
    elif islem=="5":
        kumanda.kanal_sec()

    elif islem=="6":
        print("Kanal sayısı: ",len(kumanda))
    
    elif islem=="7":
        print(kumanda)
    
    elif islem =="8":
        kumanda.oto_kapanma()

    elif islem =="9":
        kumanda.kanal_degis()

    elif islem =="10":
        kumanda.mute()
    
    else:
        print("hatalı Tuşlama")



    
