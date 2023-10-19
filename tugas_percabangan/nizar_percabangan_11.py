#nama: muhamd nizar nasruddin
# kelas: XI TKJ 2
#nomor absen: 20
#soal: Buat program Python yang mengambil nilai performa karyawan (1 hingga 5, dengan 5 sebagai performa terbaik) dan menghitung bonus tahunan berdasarkan aturan berikut:
# - Performa 5: Bonus 20% dari gaji tahunan.
# - Performa 4: Bonus 10% dari gaji tahunan.
# - Performa 3: Bonus 5% dari gaji tahunan.
# - Performa 2: Bonus 2% dari gaji tahunan. 
# - Performa 1: Tidak ada bonus.

Performa_Karyawan = input("Berapa performa karyawan 1 - 5 = ")
Gaji_Tahunan_Karyawan = input("Berapa gaji tahunan karyawan = ")

if Performa_Karyawan == 5:
    Bonus= Gaji_Tahunan_Karyawan * 0.20
elif Performa_Karyawan == 4:
    Bonus= Gaji_Tahunan_Karyawan * 0.10
elif Performa_Karyawan == 3:
    Bonus = Gaji_Tahunan_Karyawan * 0.05
elif Performa_Karyawan == 2:
    Bonus = Gaji_Tahunan_Karyawan * 0.02
else:
    Bonus = Gaji_Tahunan_Karyawan * 0


Jumlah_Bonus_Tahunan = (Gaji_Tahunan_Karyawan + Bonus)
print(f"Total Bonus Karyawan adalah {Jumlah_Bonus_Tahunan}")