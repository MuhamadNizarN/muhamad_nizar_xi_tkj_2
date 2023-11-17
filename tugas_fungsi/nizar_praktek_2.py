# Nama : Muhamad Nizar Nasruddin
# Kelas : 11 TKJ 2
# Nomor Absen : 20
# Soal : buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan

def hitungan_faktorial(n):
    if n < 0:
        return "faktorial tidak terdefinisi untuk bilangan negatif"
    elif n == 0 or n == 1:
        return 1
    else:
        faktorial = 1
        for i in range(2, n + 1):
            faktorial *= i
        return faktorial
    
bilangan = int(input("Masukan bilangan untuk dihitung faktorial: "))
hasil_faktorial = hitungan_faktorial(bilangan)

print(f"Faktorial daro {bilangan} adalah: {hasil_faktorial}")