
liste = [1,2,3,4]
print(len(liste))

isim = "Merve Kurt"
print(len(isim))

class Urun:
    def __init__(self,urunKodu,urunAdı,fiyati):
        self.urunKodu = urunKodu
        self.urunAdı = urunAdı
        self.fiyati = fiyati

    def __len__(self):
        return self.fiyati
    
    def __str__(self):
        return f"{self.urunKodu}, {self.urunAdı} ürün listelendi"
    
    def __repr__(self):
        return f"{self.urunKodu}, {self.urunAdı} ürün listelendi"
    
    def __del__(self):
        print("Ürün objesi silindi.")


urun1 = Urun("246854523","TV",5000)
print(len(urun1))
print(str(urun1))
print(repr(urun1))
del urun1