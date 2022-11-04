import random
import time


class Lab():
    def __init__(self, lab_durum="Kapalı",lab_kapasite=30,program_listesi=["Excel","Word","PowerPoint","PowerBI","Python"],kartus = 10000):

        self.lab_durum=lab_durum
        self.lab_kapasite=lab_kapasite
        self.program_listesi=program_listesi
        self.kartus= kartus

    
    def lab_ac(self):
        if (self.lab_durum == "Kapalı"):
            self.lab_durum = "Açık"
            print("Lab Açılıyor...")
        else:
            print("Lab zaten açık")
    
    def lab_kapa(self):
        if (self.lab_durum == "Açık"):
            self.lab_durum = "Kapalı"
            print("Lab kapanıyor...")
        else:
            print("Lab zaten kapalı")

    def program_ekle(self):
        program = input("Lütfen kurmak istediğiniz program ismini yazınız: ")
        if program in self.program_listesi:
            print("Bu program zaten ekli durumdadır")
        else:
            price = random.randint(4000,8000)
            print(f"Programın fiyatı {price} kadardır.")
            answerr = input("Devam etmek için 1, işlemi iptal etmek için herhangi bir şey yazınız: ")
            if answerr == "1":
                print("Program ekleniyor...")
                time.sleep(1)
                self.program_listesi.append(program)
                print("Program listesi: {}".format(self.program_listesi))
            else:
                pass
    
    def kapasite_artir(self):
        try:
            adet = int(input("Lütfen kaç adet bilgisayar eklemek istediğinizi yazınız: "))
            if adet <= 0:
                print("Hatalı bir sayı girdiniz.")
            else:
                price = random.randint(10000,30000)
                print(f"Bilgisayar/Bilgisayarların fiyatı {price*adet} kadardır.")
                answerr = input("Devam etmek için 1, işlemi iptal etmek için herhangi bir şey yazınız: ")
                if answerr == "1":
                    print("Bilgisayar/Bilgisayarlar ekleniyor...")
                    time.sleep(1)
                    self.lab_kapasite += adet
                    print("Lab Kapasitesi: {}".format(self.lab_kapasite))
                else:
                    pass
        except:
            print("Hatalı bir sayı girdiniz.")

    def cikti(self):
        print("Çıktı alınıyor...")
        time.sleep(1)
        self.kartus -= 1
        print(f"Kalan Kartuş Sayısı: {self.kartus}")

    def __str__(self):
        return "Lab durumu: {}\nLab Kapasite: {}\nProgram listesi: {}\nKalan Kartuş Sayısı: {}".format(self.lab_durum,self.lab_kapasite,self.program_listesi,self.kartus)
        

    def __len__(self):
        return len(self.program_listesi)

print("""

        1. Lab aç
        2. Lab kapat
        3. Kapasite ekle
        4. Program ekle
        5. Program Sayısı
        6. Lab Bilgileri
        7. Çıktı Al

Çıkmak için q'ya bas.

""")
lab=Lab()

while True:
    islem= input("İslem seçiniz: ")

    if islem =="q":
        print("Sonlandırılıyor")
        break 
    elif islem =="1":
        lab.lab_ac()
    
    elif islem=="2":
        lab.lab_kapa()

    elif islem=="3":
        lab.kapasite_artir()
    
    elif islem=="4":
        lab.program_ekle()
    
    elif islem=="5":
        print("Program sayısı: ",len(lab))
    
    elif islem=="6":
        print(lab)

    elif islem=="7":
        lab.cikti()
    
    else:
        print("hatalı Tuşlama")