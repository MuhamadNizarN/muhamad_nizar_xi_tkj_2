#nama: muhamd nizar nasruddin
# kelas: XI TKJ 2
#nomor absen: 20
#soal: Buat program Python yang memeriksa apakah suatu file sudah ada di direktori server. Jika file sudahada, program harus mencetak "File sudah ada," jika tidak, program harus mencetak "File belum ada."

nama_file = "data.txt"
daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

if nama_file in daftar_file_di_server:
    print("File sudah ada")
else:
    print("File belum ada")
    
    