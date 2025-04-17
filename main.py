
import module

sonuc = module.password
print(sonuc)

sonuc1 = module.sayilar[0]
print(sonuc1)

sonuc2 = module.user
print(sonuc2)

sonuc3 = module.user["notlar"]
print(sonuc3)

sonuc4 = module.ortalama(100,50)
print(sonuc4)

import module as md1 #modülü artık module diye değil md1 olarak çağırıyoruz.

sonuc5 = md1.sayilar
print(sonuc5)

from module import user, ortalama
sonuc6 = user
print(sonuc6)
sonuc7 = ortalama(200,300)
print(sonuc7)

from module import * #bunu dediğimizde modulenin içindeki herşeye ulaşıyoruz.