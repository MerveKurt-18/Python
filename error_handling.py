while True:
    try:

        a = int(input("a :"))
        b = int(input("b :"))
        print(a/b) 

    except ZeroDivisionError as e:
        print("b sayısı 0 olamaz.")
        print(e) #buradaki e proğramcıya ne hatası ile karşılaştığını gönderir

    except ValueError:
        print("sadece sayısal veri giriniz.")

    except Exception:
        print("bilinmeyen bir hata oluştu")
    else:
        break
    finally:
        print("finaly bloğu çalıştı")#her durumda çalışır


    #except (ZeroDivisionError, ValueError):
    #   print("hata oluştu")     şeklinde deyapabiliriz.