#nama: muhamd nizar nasruddin
# kelas: XI TKJ 2
#nomor absen: 20
#soal: Buat program Python yang mengambil total belanjaan dan status anggota (biasa atau premium).Berikan diskon berdasarkan aturan berikut:
# - Anggota premium: Jika total belanjaan lebih dari 500.000, berikan diskon 15%. Jika tidak,berikan diskon 10%.
# - Anggota biasa: Jika total belanjaan lebih dari 300.000, berikan diskon 7%. Jika tidak, berikadiskon 0%.

total_belanjaan = float(input("Masukkan total belanjaan: "))
status_anggota = input("Masukkan status anggota (premium/tidak): ").lower()
diskon = 0

if status_anggota == "premium":
    if total_belanjaan > 500000:
        diskon = 0.15
    else:
        diskon = 0.10
elif status_anggota == "tidak":
    if total_belanjaan > 300000:
        diskon = 0.07  

jumlah_bayar = total_belanjaan - (total_belanjaan * diskon)

print("Jumlah yang harus dibayar: Rp", jumlah_bayar)
