# Nama : Muhamad Nizar Nasruddin
# Kelas : 11 TKJ 2
# Nomor Absen : 20
# Soal : Buatlah sebuah fungsi python yang menghitung nilai pangkat dari suatu bilangan dengan eksponen tertentu

def hitung_pangkat(bilangan, eksponen):
    return bilangan ** eksponen

bilangan_input = float(input("Masukan bilangan: "))
eksponen_input = int(input("Masukan komponen: "))

hasil_pangkat = hitung_pangkat(bilangan_input, eksponen_input)
print(f"Hasil {bilangan_input}^{eksponen_input} adalah: {hasil_pangkat} ")