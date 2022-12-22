s = "Bilgisayar Mühendisi"
print("y" in s)
print("k" in s) # var mı yok mu
print("k" not in s)

print(s.find("s")) # Baştaki s in indedxi
print(s.rfind("s")) # sondaki s in indexi

print(s.replace("ü" , "u")) #değiştir
print(s.count("i")) #tekrar sayısı

print(s.startswith("B")) # Başlma harfi B mi ?
print(s.startswith("K")) # Başlma harfi K mı ?

print(s.endswith("i")) #Bitiş harfi i mi?
print(s.endswith("a")) #Bitiş harfi a mı?

print("923748984".isdigit()) # bütün karakterler sayı mı ?
print("29375208rucdsa14".isdigit())

print("3284yhdks".isalpha())
print (s.isalpha())
print("sjkahfjks".isalpha()) #Bütün karakterler harf mi?

print(s.isalnum())
print("ajsb84e89ı8f40ıvno".isalnum()) #Bütün karakterler sayı veya harf mi ?

a = "   BilGİsayaR  "
print(a.lower())
print(a.upper())
print(a.strip()) #boşluk siler sağ istersen r ekle solda l yaz

b = "Sena Arslan"
c = ""
d = ['Sena', 'Arslan']
print(b.ljust(30,"*"))
print(b.rjust(30,"*"))
print(bool(b)) #list dolu mu 
print(bool(c))
print(b.split())
print(b.split("a"))
print(b.split("n"))
print("-".join(d)) # birleştirir
print("**".join(d))

print(list("Bilgi sayar"))

isim = "Sena Arslan"
yas = 19
print("Adım "+isim+" ve ben "+str(yas)+" yaşındayım.")
print(f"Adım {isim} ve ben {yas} yaşındayım.")
print(f"Pi sayısı - {(22/7):.12f}")
print(f"Pi sayısı - {(22/7):.2f}")

print(dir(str)) # bütün kütüphaneler

