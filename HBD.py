from datetime import datetime as dt
import os

os.system('cls')
print("SELAMAT DATANG")
nama = input("Kamu siapa coba masukkin namamu : ")
print("HALLO", nama)
print(input())
print("Kenalin, Aku program yang dibuat FARIZ")
print('')

tglskrng =dt.now().strftime('%Y')
a = int(input("Coba Masukkan tahun kelahiranmu : "))
print("Ciee udah umur ",int(tglskrng)-a, "Tahun")
print(input())
umur = int(tglskrng)-a
if umur > 16:
    print("Makin Tua Yakin Masih Mau Jadi Beban Keluarga?")
elif umur < 17:
    print("Semangat Ya Masih Muda")
else:
    print("Tidak dikenali")

x = input("Hari Ini Kamu Ulang Tahun Ya? (y/n)")
while x != 'y':
    ultah = input("Boong mulu, ngaku aja")
    break
i = int(input("Mau Diucapin Berapa Kali : "))
for i in range(i):
    print("-----🎉🥳 HAPPY BIRTHDAY 🥳🎉-----")
print("Selamat Ulang Tahun yang ke",umur, nama)
print(input())

