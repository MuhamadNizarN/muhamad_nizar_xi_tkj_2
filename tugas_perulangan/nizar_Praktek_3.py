#nama: muhamd nizar nasruddin
# kelas: XI TKJ 2
#nomor absen: 20
#soal: Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi melebihi 20.000 dollar.

investasi_awal = 10000 
target_investasi = 20000  
tahun = 0 

while investasi_awal <= target_investasi:
    investasi_awal = investasi_awal + (investasi_awal * 0.06)  
    tahun += 1

print(f"Dibutuhkan {tahun} tahun agar nilai investasi melebihi {target_investasi} dollar.")
