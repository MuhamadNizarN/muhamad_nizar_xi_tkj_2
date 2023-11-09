#nama: muhamd nizar nasruddin
# kelas: XI TKJ 2
#nomor absen: 20
#soal: Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa apel kurang dari 20 buah.

jumlah_apel = 100  
sisa_minimal = 20  
hari = 0  

while jumlah_apel > sisa_minimal:
    jumlah_terjual = jumlah_apel * 0.10 
    jumlah_apel -= jumlah_terjual  
    hari += 1

print(f"Dibutuhkan {hari} hari agar sisa apel kurang dari {sisa_minimal} buah.")

