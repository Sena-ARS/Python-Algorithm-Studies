#2. En uzun kelime
#Girilen yazıdaki en uzun kelimeyi ve uzunluğunu yazan programı yazınız.

cml1 = input()
cml1 = cml1.split()
sayı = 0
for i in cml1 :
    if sayı < len(i) :
        sayı = len(i)
for k in cml1:
    if sayı == len(k):
        print(k,sayı)
