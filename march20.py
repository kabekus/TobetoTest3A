# 1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

'''
boy = float(input("Boyunu giriniz (Metre cinsinden yazınız): "))

kilo = float(input("Kilonuzu giriniz: "))
vki = kilo/(boy*boy)

print(vki)

'''

# 2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

'''
maas = float(input("Maaş: "))

zamOrani = float(input("Zam Oranı: "))
zamliMaas = maas + (maas*(zamOrani/100))

print(zamliMaas)

'''

# 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

'''
num1 = int(input("1. Sayıyı girin: "))
num2 = int(input("2. Sayıyı girin: "))
num3 = int(input("3. Sayıyı girin: "))

bigNum = 0

if num1 > num2 :
   bigNum = num1
else :
   bigNum = num2   


if num3 > bigNum:
   bigNum = num3 
else:
   bigNum = bigNum 

print(bigNum)

'''

# 4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

# Alan: 3.14*(r*r)    Çevre: 2*3.14*r

'''
yaricap = float(input("Yarıçap giriniz: "))

alan = 3.14 * (yaricap * yaricap)
print(f"Alan: {alan}")

cevre = 2 * 3.14 * yaricap 
print(f"Çevre : {cevre}")

'''

# 5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

number = int(input("Bir sayı giriniz: "))

def palindrom_mu(number):
    numberStr = str(number)
    reverseNumber = numberStr[::-1]
    return numberStr == reverseNumber

if palindrom_mu(number):
    message =" Girdiğiniz Sayı Palindrom"
else:
    message ="Girdiğiniz Sayı Palindrom Değil"    

print(message)