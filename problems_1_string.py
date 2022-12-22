#1. Kelime sayısı
#Girilen yazıdaki kelime sayısını bulan programı yazınız.
#Kelimelerin arasında boşluk bulunmaktadır.
 
cml = input()
kelime = (cml.split())
s = len(kelime)
print(s)

# İkinci yol

"""
cml = input()
print(cml.count(" ") + 1)

"""
