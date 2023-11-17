# Nama : Muhamad Nizar Nasruddin
# Kelas : 11 TKJ 2
# Nomor Absen : 20
# Soal : Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan

def hitung_jumlah_digit(bilangan):
    str_bilangan = str(bilangan)

    jumlah_digit = 0 
    for digit in str_bilangan:
        if digit.isdigit():
            jumlah_digit += int(digit)
    
    return jumlah_digit

bilangan_input = int(input("Masukan bilangan: "))
hasil_jumlah_digit = hitung_jumlah_digit(bilangan_input)

print(f"Jumlah digit dari {bilangan_input} adalah: {hasil_jumlah_digit}")