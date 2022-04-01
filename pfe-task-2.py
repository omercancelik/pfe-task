kullanici_Adi = "omercanclk"    
kullanici_Sifre = "metamorfoz"
siparis_Listesi = []

def ekran2():
    secenek = int(input("1- Siparişlerim\n2- Sepetim\n3- Alışveriş"))
def siparis_Liste():
    siparis_Listesi

while True:
    ka = input("Kullanıcı Adı: ")
    
    if ka == kullanici_Adi:
        pw = input("Şifre: ")
        if pw == kullanici_Sifre:
            print("Kullanıcı Adı ve Şifre Doğrulandı. Giriş Başarılı.")
            break
        else:
            print("Şifre hatalı. Lütfen tekrar giriniz!")
                    
    else:
        print("Kullanıcı adı hatalı. Lütfen tekrar giriniz!")
        continue

print("Ana sayfaya Hoşgeldiniz!")



