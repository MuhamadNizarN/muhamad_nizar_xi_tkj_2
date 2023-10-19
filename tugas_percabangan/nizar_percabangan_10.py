#nama: muhamd nizar nasruddin
# kelas: XI TKJ 2
#nomor absen: 20
#soal: Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis pinjaman berdasarkan aturan berikut:
# - Peminjaman 7 hari atau kurang: "Peminjaman Pendek"
# - Peminjaman lebih dari 7 hari hingga 30 hari: "Peminjaman Menengah"
# - Peminjaman lebih dari 30 hari: "Peminjaman Panjang"

durasi = float(input("berapa hari anda meminjam buku = "))

if durasi <= 7:
    print("Peminjaman Pendek")
elif durasi <= 30 :
    print("Peminjaman Menengah")
    
else : print("Peminjaman Panjang")