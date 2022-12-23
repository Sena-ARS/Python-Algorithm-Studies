#3. Palindrom yazı
#Girilen yazı palindrom ise Evet, değilse Hayır yazan programı yazınız.
#Yazıdaki boşluklar hesaba katılmayacak.
#Palindrom: soldan sağa ve sağdan sola okunduğunda aynı olan yazıdır.

yazi = input()
yazi = yazi.split()
yazi = "".join(yazi)
yazi = yazi.lower()
tyazi = yazi[::-1]
if tyazi == yazi :
    print("Evet")
else:
    print("Hayır")
