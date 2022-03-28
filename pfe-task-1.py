rehber_dict = {}

def get_key(val):
    for key, value in rehber_dict.items():
         if val == value:
             return key
 
    return "There is no such Key"

while True:
    Karar = input("Yapmak istediğiniz işlem nedir?\n-1 Rehbere Kişi Ekle\n-2 Rehberden Kişi Silme\n-3 İsim & Numara Güncelleme\n-4 Rehberi Görüntüle\n")
    
    if Karar == "1":
        isim = input("İsmi giriniz.")
        numara = int(input("Numarayı Giriniz.")) 
        if isim in rehber_dict:
            print("Girdiğiniz isim rehberde bulunmaktadır. Lütfen farklı bir isim giriniz.")
        else:
            rehber_dict[isim] = numara
    
    elif Karar == "2":
        sil_num = input("Silinecek isim veya numarayı giriniz.")
        if sil_num in rehber_dict.keys():
            rehber_dict.pop(sil_num)
            
        elif sil_num in rehber_dict.values():
            rehber_dict.pop(get_key(sil_num)) 
        else:
            print("Girdiğiniz isim veya numara rehberde bulunmamaktadır.")
    
    elif Karar == "3":
        degis_isim = input("Numarasını değiştirmek istediğiniz kişiyi giriniz.")
        degis_num = input("Yeni numarayı giriniz.")
        if degis_isim in rehber_dict:
            rehber_dict.pop(degis_isim)
            rehber_dict[degis_isim] = degis_num
            print("Numara Güncellenmiştir.")
        else:
            print("Girdiğiniz isim rehberde bulunmamaktadır.")
    
    
    elif Karar == "4":
        for i in rehber_dict:
            print(i,"-->", rehber_dict[i])
    
    else:
        print("Yanlış giriş yaptınız.")
        exit()
    