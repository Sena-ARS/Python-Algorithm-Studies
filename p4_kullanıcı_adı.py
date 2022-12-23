#Kullanıcı ismi
#Kullanıcı ismi sadece harf, rakam ve alt çizgi(_) içerebilir.
#Eğer kurallara uygunsa program OK yazar, değilse ilk hatalı karakter yazılır.
KullanıcıAdı = input()
for i in KullanıcıAdı:
    i
    if i.isalnum() == True or i == "_":
        cıktı = "OK"
    else :
        cıktı = i
        print("Geçersiz karakter kullandınız.")
        break
print(cıktı)
