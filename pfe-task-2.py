kullanici_Adi = "omercanclk"    
kullanici_Sifre = "metamorfoz"
siparislerim = []
sepetim_urunler = []


kategori_Elektronik = {"1-Telefon": 900,"2-Laptop": 1500,"3-Kulaklık": 200,"4-Oyun Konsolu": 500,"5-Televizyon": 2500}
kategori_Giysi = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5}
kategori_Mobilya = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5}
kategori_Gıda = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5}
kategori_Oyuncak = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5}

kategori_liste = [kategori_Elektronik,kategori_Giysi,kategori_Mobilya,kategori_Gıda,kategori_Oyuncak]

def kategori_func(x):
    kategori_dict = kategori_liste[x]
    a += 1
    for i in kategori_dict:
        print(-a, i,"-->", kategori_dict[i])
    print("-6 Geri Dön")
    urun_secim = input("Ürün Seçimi Yapınız.")
    if urun_secim == "1":
        pass
    elif urun_secim == "2":
        pass
    elif urun_secim == "3":
        pass
    elif urun_secim == "4":
        pass
    elif urun_secim == "5":
        pass
    elif urun_secim == "6":
        kategoriler_func
    else:
        print("Yanlış giriş yaptınız")
        kategori_func()

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
                anasayfa_func()             
        else:
            print("Kullanıcı adı hatalı. Lütfen tekrar giriniz!")
            continue

# Ekran 2
def anasayfa_func():
    karar_Anasayfa = input("-1 Siparişlerim\n-2 Sepetim\n-3 Alışveriş\n-4 Kullanıcı girişine geri dön\n")

    if karar_Anasayfa == "1":
        siparislerim_func()
    elif karar_Anasayfa == "2":
        sepetim_func()
    elif karar_Anasayfa == "3":
        kategoriler_func()
    elif karar_Anasayfa == "4":
        giris_func()
    else:
        print("Yanlış giriş yaptınız")
        anasayfa_func()

# Ekran 2.1
def siparislerim_func():
    karar_Siparislerim = input("-1 Siparişlerimi görüntüle\n-2 Geri Dön\n")
    if karar_Siparislerim == "1":
        for i in siparislerim:
            print(i)
    elif karar_Siparislerim == "2":
        anasayfa_func()
    else:
        print("Yanlış giriş yaptınız")
        siparislerim_func()

# Ekran 2.2
def sepetim_func():
    karar_Sepetim = input("-1 Sepettekileri listele\n-2 Siparişi onayla\n-3 Geri Dön\n")
    if karar_Sepetim == "1":
        pass
    elif karar_Sepetim == "2":
        pass
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





giris_func()