#nama: muhamd nizar nasruddin
# kelas: XI TKJ 2
#nomor absen: 20
#soal: Buat program Python yang mengambil informasi pembaruan perangkat lunak dan menentukanapakah sistem perlu di-restart. Jika pembaruan mengharuskan restart, program harus mencetak "Sistem perlu di-restart." Jika tidak, program harus mencetak "Sistem tidak perlu di-restart."
 
informasi_restart = input("apakah sistem harus direstart? (iya/tidak)")

if informasi_restart == "iya":
    print("Sistem perlu di-restart")
else : 
    print("Sistem tidak perlu di-restart")