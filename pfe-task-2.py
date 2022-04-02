kullanici_Adi = "a"    
kullanici_Sifre = "b"
siparislerim = []
sepetim_Urunler = []
sepetim_Toplam = []

kategori_Elektronik = {"Telefon": 900,"Laptop": 1500,"Kulaklık": 200,"Oyun Konsolu": 500,"Televizyon": 2500}
kategori_Giysi = {"Tişört": 100,"Pantolon": 250,"Sweatshirt": 300,"Etek": 100,"Mont": 650}
kategori_Mobilya = {"Koltuk": 1000,"Sandalye": 500,"Masa": 2000,"Yatak": 4500,"Dolap": 1500}
kategori_Gıda = {"Et": 125,"Yağ": 200,"Un": 50,"Balık": 100,"Çikolata": 25}
kategori_Enstruman = {"Gitar": 3500,"Piano": 25000,"Keman": 4000,"Bateri": 7500,"Akordeon": 15000}

kategori_liste = [kategori_Elektronik,kategori_Giysi,kategori_Mobilya,kategori_Gıda,kategori_Enstruman]


def giris_func():   
    while True:
        ka = input("Kullanıcı Adı: ") 
        if ka == kullanici_Adi:
            pw = input("Şifre: ")
            if pw == kullanici_Sifre:
                print("Kullanıcı Adı ve Şifre Doğrulandı. Giriş Başarılı.")
                anasayfa_func()
            else:
                print("Şifre hatalı. Lütfen tekrar giriniz!")  
                giris_func()            
        else:
            print("Kullanıcı adı hatalı. Lütfen tekrar giriniz!")
            continue

# Ekran 2
def anasayfa_func():
    karar_Anasayfa = input("-1 Siparişlerim\n-2 Sepetim\n-3 Alışveriş\n-4 Kullanıcı girişine geri dön\n-5 Çıkış Yap\n")

    if karar_Anasayfa == "1":
        siparislerim_func()
    elif karar_Anasayfa == "2":
        sepetim_func()
    elif karar_Anasayfa == "3":
        kategoriler_func()
    elif karar_Anasayfa == "4":
        giris_func()
    elif karar_Anasayfa == "5":
        exit()
    else:
        print("Yanlış giriş yaptınız")
        anasayfa_func()

# Ekran 2.1
def siparislerim_func():
    karar_Siparislerim = input("-1 Siparişlerimi görüntüle\n-2 Geri Dön\n")
    if karar_Siparislerim == "1":
        for i in siparislerim:
            print(i)
        siparislerim_func()
    elif karar_Siparislerim == "2":
        anasayfa_func()
    else:
        print("Yanlış giriş yaptınız")
        siparislerim_func()

# Ekran 2.2
def sepetim_func():
    karar_Sepetim = input("-1 Sepettekileri listele\n-2 Siparişi onayla\n-3 Geri Dön\n")
    b = 0
    
    if karar_Sepetim == "1":
        for i in range(len(sepetim_Urunler)):
            print("-",i+1, sepetim_Urunler[i],"-->",sepetim_Toplam[i])
        for i in sepetim_Toplam:
            b += int(i)
        print("Sepetin Toplam Tutarı:", b)
        karar_Sepetim2 = input("-1 Çıkartılacak Ürünü Seçiniz\n-2 Geri Dön\n")
        if karar_Sepetim2 == "1":
            for i in range(len(sepetim_Urunler)):
                print("-",i+1,sepetim_Urunler[i],"-->",sepetim_Toplam[i])
            karar_cıkarma = int(input("Hangi Ürünü Çıkarmak İstiyorsunuz?"))
            sepetim_Urunler.pop(karar_cıkarma-1)
            sepetim_Toplam.pop(karar_cıkarma-1)
            print("Ürün Çıkartılmıştır.")
            sepetim_func()
        elif karar_Sepetim2 == "2":
            sepetim_func()
    elif karar_Sepetim == "2":
        for i in sepetim_Urunler:
            siparislerim.append(i)
        print("Satın alma başarılı!")
        sepetim_Urunler.clear()
        sepetim_func()
    elif karar_Sepetim == "3":
        anasayfa_func()
    else:
        print("Yanlış giriş yaptınız")
        sepetim_func()

# Ekran 2.3
def kategoriler_func():
    karar_Kategoriler = input("Kategoriler:\n-1 Kategori1\n-2 Kategori2\n-3 Kategori3\n-4 Kategori4\n-5 Kategori5\n-6 Geri Dön\n")

    if karar_Kategoriler == "1":
        kategori_func(0)
    elif karar_Kategoriler == "2":
        kategori_func(1)
    elif karar_Kategoriler == "3":
        kategori_func(2)
    elif karar_Kategoriler == "4":
        kategori_func(3)
    elif karar_Kategoriler == "5":
        kategori_func(4)
    elif karar_Kategoriler == "6":
        anasayfa_func()
    else:
        print("Yanlış giriş yaptınız")
        kategoriler_func()

# Ekran 2.3.1,2,3,4,5

def kategori_func(x):
    kategori_dict = kategori_liste[x]
    a = 1
    for i in kategori_dict:
        print(-a, i,"-->", kategori_dict[i])
        a += 1
    print("-6 Geri Dön")
    while True:
        urun_secim = input("Ürün Seçimi Yapınız.")
        if urun_secim == "1":
            sepetim_Urunler.append(list(kategori_dict.keys())[0])
            print("Sepete ekleme başarılı.")
            sepetim_Toplam.append((list(kategori_dict.values())[0]))
        elif urun_secim == "2":
            sepetim_Urunler.append(list(kategori_dict.keys())[1])
            print("Sepete ekleme başarılı.")
            sepetim_Toplam.append((list(kategori_dict.values())[1]))
        elif urun_secim == "3":
            sepetim_Urunler.append(list(kategori_dict.keys())[2])
            print("Sepete ekleme başarılı.")
            sepetim_Toplam.append((list(kategori_dict.values())[2]))
        elif urun_secim == "4":
            sepetim_Urunler.append(list(kategori_dict.keys())[3])
            print("Sepete ekleme başarılı.")
            sepetim_Toplam.append((list(kategori_dict.values())[3]))
        elif urun_secim == "5":
            sepetim_Urunler.append(list(kategori_dict.keys())[4])
            print("Sepete ekleme başarılı.")
            sepetim_Toplam.append((list(kategori_dict.values())[4]))
        elif urun_secim == "6":
            kategoriler_func()
        else:
            print("Yanlış giriş yaptınız")
            kategori_func(x)
    return sepetim_Toplam






giris_func()