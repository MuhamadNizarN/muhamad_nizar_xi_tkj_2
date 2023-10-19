#nama: muhamd nizar nasruddin
# kelas: XI TKJ 2
#nomor absen: 20
#soal: Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek
# tersebut dapat diluncurkan. Jika status persiapan "Siap," program harus mencetak "Proyek
# diluncurkan." Jika status persiapan "Tunda," program harus mencetak "Proyek ditunda."

status_persiapan_proyek = input("apakah proyek tersebut siap diluncurkan? (siap/tunda)")

if status_persiapan_proyek == "siap":
    print("Proyek dilucurkan")
elif status_persiapan_proyek == "tunda":
    print("Proyek ditunda")
    
else : print("DATA YANG ANDA MASUKAN SALAH, MASUKKAN (siap atau tunda)!")