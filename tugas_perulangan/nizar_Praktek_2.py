#nama: muhamd nizar nasruddin
# kelas: XI TKJ 2
#nomor absen: 20
#soal: Seorang petani memiliki 100 ekor ayam di peternakannya. Setiap bulan, jumlah ayam bertambah 5% dari jumlah ayam pada bulan sebelumnya. Buatlah program yang menghitung berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor.

jarak_awal = 5  
target_jarak = 10  
minggu = 0  

while jarak_awal <= target_jarak:
    penjumlahan = jarak_awal * 0.10  
    jarak_awal = jarak_awal + penjumlahan
    minggu += 1

print(f"Dibutuhkan {minggu} minggu agar pelari dapat berlari lebih dari {target_jarak} kilometer.")
