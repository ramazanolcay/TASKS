class Hayvan():

    def __init__(self, boy, renk, kilo, age, ayak_sayisi):
        self.boy = boy
        self.renk = renk
        self.kilo = kilo
        self.age = age
        self.ayak_sayisi = ayak_sayisi

class Dinozor(Hayvan):
    def __init__(self, boy, renk, kilo, age, ayak_sayisi, dino_tur):
        super().__init__(boy, renk, kilo, age, ayak_sayisi)
        self.dino_tur = dino_tur
    
    def __str__(self):
        return "Boy: {}\nRenk: {}\nKilo: {}\nYaş: {}\nAyak Sayısı: {}\nDinazor Türü: {}".format(self.boy,
        self.renk,self.kilo,self.age,self.ayak_sayisi,self.dino_tur)

class Orkinos(Hayvan):
    def __init__(self, boy, renk, kilo, age, ayak_sayisi, yuzme_hizi):
        super().__init__(boy, renk, kilo, age, ayak_sayisi)
        self.yuzme_hizi = yuzme_hizi
    
    def __str__(self):
        return "Boy: {}\nRenk: {}\nKilo: {}\nYaş: {}\nAyak Sayısı: {}\nYüzme Hızı: {}".format(self.boy,
        self.renk,self.kilo,self.age,self.ayak_sayisi,self.yuzme_hizi)

class Kartal(Hayvan):
    def __init__(self, boy, renk, kilo, age, ayak_sayisi, ucus_hizi):
        super().__init__(boy, renk, kilo, age, ayak_sayisi)
        self.ucus_hizi = ucus_hizi
    
    def __str__(self):
        return "Boy: {}\nRenk: {}\nKilo: {}\nYaş: {}\nAyak Sayısı: {}\nUçma Hızı: {}".format(self.boy,
        self.renk,self.kilo,self.age,self.ayak_sayisi,self.ucus_hizi)


class Ceylan(Hayvan):
    def __init__(self, boy, renk, kilo, age, ayak_sayisi, toynak_sayisi):
        super().__init__(boy, renk, kilo, age, ayak_sayisi)
        self.toynak_sayisi = toynak_sayisi

    def __str__(self):
        return "Boy: {}\nRenk: {}\nKilo: {}\nYaş: {}\nAyak Sayısı: {}\nToynak Sayısı: {}".format(self.boy,
        self.renk,self.kilo,self.age,self.ayak_sayisi,self.toynak_sayisi)


dino1 = Dinozor(4500, "Green", 5500, 18, 2, "T-rex")
dino2 = Dinozor(2500, "Brown", 1000, 7, 2, "Pterozor")
orki1 = Orkinos(3300, "Blue", 688, 7, 0, 65)
karti1 = Kartal(90, "Black", 5.4, 22, 2, 150)
ceycey1= Ceylan(101, "Brown", 38, 13, 4, 2)

print(dino1)
print(dino2)
print(orki1)
print(karti1)
print(ceycey1)