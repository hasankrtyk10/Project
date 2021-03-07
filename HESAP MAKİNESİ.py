import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet HESAP MAKINASI")


print("""
==============================================
1)Toplama Islemi:
2)Cıkarma Islemi:
3)Carpma Islemi:
4)Bolme Islemi:
==============================================
""")
giris = input("Bir Tanesini Seciniz=")

if (giris=="1"):
    print("Toplama Işlemini Sectiniz")
    deger1=float(input("1)Birinci Degeri Giriniz==>"))
    deger2=float(input("2)Ikinci Degeri Giriniz==>"))
    print("===========================")
    print("Sonuc:",deger1 + deger2)
    print("===========================")
elif(giris=="2"):
    print("Cıkarma Islemini Sectiniz")
    deger1=float(input("1)Birinci Degeri Giriniz==>"))
    deger2=float(input("2)Ikinci Degeri Giriniz==>"))
    print("============================")
    print("Sonuc:",deger1 - deger2)
    print("============================")
elif(giris=="3"): 
    print("Carpma Islemi Sectiniz")
    deger1=float(input("1)Birinci Degeri Giriniz==>"))
    deger2=float(input("2)Ikinci Degeri Giriniz==>"))
    print("=============================")
    print("Sonuc:", deger1 * deger2)
    print("=============================")
elif(giris=="4"):
    print("Bolme Islemi Sectiniz")
    deger1=float(input("1)Birinci Degeri Giriniz==>"))
    deger2=float(input("2)Ikinci Degeri Giriniz==>"))
    print("==============================")
    print("Sonuc:", deger1 / deger2)
    print("==============================")
else:
    print("<<<<<<<<Yanlıs Deger Girildi Programdan Cıkılıyor>>>>>>>>")
