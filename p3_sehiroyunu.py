#Şehir oyunu
#Programa birinci şehir ismi girilir ve daha sonra ikinci şehir ismi girilir.
#Birinci şehrin son harfi ile ikinci şehrin ilk harfi aynı ise yeni şehir okumaya devam edilir.
#Daha önceki ikinci şehir birinci gibi kabul edilir ve son girilen şehir ikinci şehir olur.
#Böylece Kural sağlandığı sürece şehir ismi girilmeye devam edilir.
#Kural bozulduğu zaman en son girilen şehir, yani kuralı bozan şehir yazılır.
import time
sehir1 = input()
sehir2 = input()
sehir1 = sehir1.lower()   
sehir2 = sehir2.lower()
while sehir1[-1] == sehir2[0] :
    temp = input()
    sehir1 = sehir2
    sehir2 = temp
print("değerlendiriliyor...")
time.sleep(1)
print("Oyunu bozan kelime :", sehir2)
