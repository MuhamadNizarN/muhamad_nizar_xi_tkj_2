#nama: muhamd nizar nasruddin
# kelas: XI TKJ 2
#nomor absen: 20
#soal: Buat program Python yang mengambil nilai tugas (skala 0-100) dan nilai ujian (skala 0-100) seorangsiswa dan menentukan nilai akhirnya. Jika nilai tugas lebih dari 70 dan nilai ujian lebih dari 60, siswalulus dengan nilai "Lulus". Jika tidak, siswa gagal dengan nilai "Gagal".

jumlah_ayam = 100  
target_ayam = 200  
bulan = 0  

while jumlah_ayam <= target_ayam:
    Penjumlahan = jumlah_ayam * 0.05  
    jumlah_ayam = jumlah_ayam + Penjumlahan
    bulan += 1

print(f"Dibutuhkan {bulan} bulan agar jumlah ayam melebihi {target_ayam} ekor.")

