"""
import datetime
sonuc = dir(datetime)
print(sonuc)
"""
from datetime import timedelta
from datetime import datetime
#sonuc = dir(datetime)
#print(sonuc)

simdi = datetime.now()
print(simdi)
simdi1 = datetime.today()
print(simdi1)

sonuc = datetime.now()
sonuc = simdi.year
print(sonuc)
sonuc1 = simdi.month
print(sonuc1)
sonuc2 = simdi.day
print(sonuc2)
sonuc3 = simdi.hour
print(sonuc3)
sonuc4 = simdi.minute
print(sonuc4)
sonuc5 = simdi.second
print(sonuc5)

sonuc6 = datetime.ctime(simdi)
print(sonuc6)

sonuc7 = datetime.strftime(simdi, "%Y") #yıl
print(sonuc7)
sonuc8 = datetime.strftime(simdi, "%X") #zaman
print(sonuc8)
sonuc9 = datetime.strftime(simdi, "%d") #ayın kaçı olduğu
print(sonuc9)
# %A dediğimizde günü yazıyla
# googleye datetime python yazdığımızda orda X Y gibi kısaltmaların anlamları yazıyor.
sonuc10 = datetime.strftime(simdi, "%Y %B %A") 
print(sonuc10)

birthday = datetime(1999,10,10,14,30,50)
print(birthday)

sonuc11 = datetime.timestamp(birthday)#saniye
print(sonuc11)

sonuc12 = simdi - birthday
print(sonuc12)
sonuc13 = sonuc12.seconds
print(sonuc13)

sonuc14 = simdi + timedelta(10)# şimdinin zamanına 10 gün ekliyor
print(sonuc14)

sonuc15 = simdi + timedelta(days=500, minutes=20)
print(sonuc15)

sonuc16 = simdi - timedelta(days=10)
print(sonuc16)
