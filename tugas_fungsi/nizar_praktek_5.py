# Nama : Muhamad Nizar Nasruddin
# Kelas : 11 TKJ 2
# Nomor Absen : 20
# Soal : Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n

def fibonacci(n):
    if n <= 0:
        return "N harus lebih besar dari 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n_input = int(input("Masukan nilai n untuk bilangan Fibonacci: "))
hasil_fibonacci = fibonacci(n_input)

print(f"Bilangan Fibonacci ke {n_input} adalah: {hasil_fibonacci}")