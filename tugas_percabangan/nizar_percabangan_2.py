#nama: muhamd nizar nasruddin
# kelas: XI TKJ 2
#nomor absen: 20
#soal: Buat program Python yang mengambil estimasi waktu selesai proyek dan tanggal target selesai. Jika estimasi waktu selesai lebih awal atau sama dengan tanggal target, program harus mencetak "Tepatwaktu," jika tidak, program harus mencetak "Terlambat.

estimasi_selesai = input("Masukkan estimasi waktu selesai proyek (Tahun-Bulan-Tanggal): ")
tanggal_target_selesai = input("Masukkan tanggal target selesai (Tahun-Bulan-Tanggal): ")


if estimasi_selesai <= tanggal_target_selesai:
    print("Tepat waktu")
else:
    print("Terlambat")