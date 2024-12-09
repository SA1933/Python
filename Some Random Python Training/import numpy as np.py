import numpy as np
import time
from tkinter import Tk, simpledialog, messagebox

def print_odd_numbers():
    print("Program Menampilkan Angka Ganjil:")
    for angka in range(1, 1001):
        if angka % 2 != 0:
            print(angka)

def create_account():
    print("Program Pembuatan Akun:")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    max_attempts = 3
    attempts = 0

    while True:
        confirm_password = input("Konfirmasi password: ")
        if password == confirm_password:
            print("Selamat, Akun berhasil dibuat!")
            break
        else:
            attempts += 1
            if attempts >= max_attempts:
                print(f"Anda telah mencoba konfirmasi password sebanyak {max_attempts} kali.")
                print("Silahkan buat password baru.")
                password = input("Masukkan password baru: ")
                attempts = 0
            else:
                print(f"Password tidak memenuhi syarat, silakan coba lagi. Sisa percobaan: {max_attempts - attempts}")

def fibonacci_sequence():
    print("Program Urutan Fibonacci:")
    panjang_urutan = int(input("Masukkan panjang urutan Fibonacci: "))
    a, b = 0, 1
    urutan_fibonacci = []
    while len(urutan_fibonacci) < panjang_urutan:


        urutan_fibonacci.append(a)
        a, b = b, a + b
    print("Urutan Fibonacci dengan panjang", panjang_urutan, "adalah:")
    print(urutan_fibonacci)

def calculate_discount():
    total_harga = 0
    daftar_barang = []
    while True:
        try:
            nama_barang = input(f"Masukkan nama barang ke-{len(daftar_barang) + 1} (atau 'selesai' untuk mengakhiri): ")
            if nama_barang.lower() == 'selesai':
                break
            harga = float(input(f"Masukkan harga {nama_barang}: "))
            if harga < 0:
                print("Harga tidak valid. Harap masukkan harga yang benar.")
                continue
            total_harga += harga
            daftar_barang.append((nama_barang, harga))
        except ValueError:
            print("Harga tidak valid. Harap masukkan harga yang benar.")
    print(f"Total harga sebelum diskon: {total_harga:.2f} Rupiah")

    if total_harga > 200000:
        diskon = min(total_harga * 0.10, 100000)
    elif total_harga > 40000:
        diskon = min(total_harga * 0.05, 100000)
    else:
        diskon = 0

    total_harga_diskon = total_harga - diskon

    print(f"Total harga setelah mendapatkan diskon: {total_harga_diskon:.2f} Rupiah")
    print("Daftar Barang:")
    for nama, harga in daftar_barang:
        print(f"{nama}: {harga:.2f} Rupiah")
    print(f"Diskon: {diskon:.2f} Rupiah")

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def transpose_matrix():
    print("Program Transposisi Matriks:")
    m, n = int(input("Masukkan jumlah baris: ")), int(input("Masukkan jumlah kolom: "))
    matrix = np.array([[int(input(f"Masukkan elemen di posisi ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)])

    print("\nMatriks:")
    print("\n".join(" ".join(map(str, row)) for row in matrix))

    transposed_matrix = np.transpose(matrix)
    print("\nMatriks Transposisi:")
    print("\n".join(" ".join(map(str, row)) for row in transposed_matrix))

def calculate_grades():
    print("Program Perhitungan Nilai, Grade, dan Status:")
    while True:
        try:
            tugas = float(input("Masukkan nilai Tugas: "))
            uts = float(input("Masukkan nilai UTS: "))
            uas = float(input("Masukkan nilai UAS: "))
 
            nilai = (0.4 * tugas) + (0.3 * uts) + (0.3 * uas)
 
            if nilai > 85:
                grade = "A"
            elif nilai > 80:
                grade = "AB"
            elif nilai > 75:
                grade = "B"
            elif nilai > 70:
                grade = "BC"
            elif nilai > 65:
                grade = "C"
            elif nilai > 60:
                grade = "CD"
            elif nilai > 55:
                grade = "D"
            else:
                grade = "E"
 
            if nilai > 60:
                status = "Lulus"
            else:
                status = "Tidak Lulus"

            print("Nilai Akhir: %0.2f" % nilai)
            print("Grade: {}".format(grade))
            print("Status: {}".format(status))

        except ValueError:
            print("Masukan tidak valid. Harap masukkan lagi nilai tugas, uts, dan uas")
    
        lanjutkan = input("Apakah Anda ingin memasukkan angka lagi? (ya/tidak): ")
        if lanjutkan.lower() != "ya":
            break

def simple_calculator():
    hasil = None

    while True:
        try:
            if hasil is None:
                angka1 = float(input("Masukkan angka pertama: "))
            else:
                angka1 = hasil

            operasi = input("Masukkan operasi (+, -, *, /) atau '=' untuk mengakhiri: ")

            if operasi == '=':
                print("Hasil akhir: ", hasil)
                break

            angka2 = float(input("Masukkan angka kedua: "))

            if operasi == '+':
                hasil = angka1 + angka2
            elif operasi == '-':
                hasil = angka1 - angka2
            elif operasi == '*':
                hasil = angka1 * angka2
            elif operasi == '/':
                if angka2 == 0:
                    print("Tidak dapat membagi dengan nol")
                    hasil = None
                else:
                    hasil = angka1 / angka2
            else:
                print("Operasi tidak valid. Silakan coba lagi.")
                hasil = None

            if hasil is not None:
                print("Hasil:", hasil)
        except ValueError:
            print("Masukan tidak valid. Silakan coba lagi.")
            hasil = None

def segitiga_pagar():
    tinggi = int(input("Masukkan tinggi segitiga: "))
    for i in range(1, tinggi + 1):
        print("#" * i)

def array_acak():
    def random_array(m, n, x, y):
        return np.random.randint(x, y, size=(m, n))

    m = 4
    n = 4
    x = 0
    y = 10

    a = random_array(m, n, x, y)
    b = random_array(m, n, x, y)
    c = random_array(m, n, x, y)
    d = random_array(m, n, x, y)
    e = random_array(m, n, x, y)
    f = random_array(m, n, x, y)
    g = random_array(m, n, x, y)
    h = random_array(m, n, x, y)
    i = random_array(m, n, x, y)
    j = random_array(m, n, x, y)
    k = random_array(m, n, x, y)
    l = random_array(m, n, x, y)
    m_arr = random_array(m, n, x, y)
    n_arr = random_array(m, n, x, y)
    o = random_array(m, n, x, y)
    p = random_array(m, n, x, y)
    q = random_array(m, n, x, y)
    r = random_array(m, n, x, y)
    s = random_array(m, n, x, y)
    t = random_array(m, n, x, y)
    u = random_array(m, n, x, y)
    v = random_array(m, n, x, y)
    w = random_array(m, n, x, y)
    x_arr = random_array(m, n, x, y)
    y_arr = random_array(m, n, x, y)
    z = random_array(m, n, x, y)

    print("\n")
    print("A: ")
    print(a)
    invers_a = np.linalg.inv(a)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_a: ")
    print(invers_a, "\n")

    print("B: ")
    print(b)
    invers_b = np.linalg.inv(b)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_b: ")
    print(invers_b, "\n")

    print("C: ")
    print(c)
    invers_c = np.linalg.inv(c)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_c: ")
    print(invers_c, "\n")

    print("D: ")
    print(d)
    invers_d = np.linalg.inv(d)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_d: ")
    print(invers_d, "\n")

    print("E: ")
    print(e)
    invers_e = np.linalg.inv(e)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_e: ")
    print(invers_e, "\n")

    print("F: ")
    print(f)
    invers_f = np.linalg.inv(f)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_f: ")
    print(invers_f, "\n")

    print("G: ")
    print(g)
    invers_g = np.linalg.inv(g)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_g: ")
    print(invers_g, "\n")

    print("H: ")
    print(h)
    invers_h = np.linalg.inv(h)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_h: ")
    print(invers_h, "\n")

    print("I: ")
    print(i)
    invers_i = np.linalg.inv(i)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_i: ")
    print(invers_i, "\n")

    print("J: ")
    print(j)
    invers_j = np.linalg.inv(j)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_j: ")
    print(invers_j, "\n")

    print("K: ")
    print(k)
    invers_k = np.linalg.inv(k)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_k: ")
    print(invers_k, "\n")

    print("L: ")
    print(l)
    invers_l = np.linalg.inv(l)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_l: ")
    print(invers_l, "\n")

    print("M: ")
    print(m_arr)
    invers_m_arr = np.linalg.inv(m_arr)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_m: ")
    print(invers_m_arr, "\n")

    print("N: ")
    print(n_arr)
    invers_n_arr = np.linalg.inv(n_arr)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_n: ")
    print(invers_n_arr, "\n")

    print("O: ")
    print(o)
    invers_o = np.linalg.inv(o)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_o: ")
    print(invers_o, "\n")

    print("P: ")
    print(p)
    invers_p = np.linalg.inv(p)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_p: ")
    print(invers_p, "\n")

    print("Q: ")
    print(q)
    invers_q = np.linalg.inv(q)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_q: ")
    print(invers_q, "\n")

    print("R: ")
    print(r)
    invers_r = np.linalg.inv(r)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_r: ")
    print(invers_r, "\n")

    print("S: ")
    print(s)
    invers_s = np.linalg.inv(s)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_s: ")
    print(invers_s, "\n")

    print("T: ")
    print(t)
    invers_t = np.linalg.inv(t)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_t: ")
    print(invers_t, "\n")

    print("U: ")
    print(u)
    invers_u = np.linalg.inv(u)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_u: ")
    print(invers_u, "\n")

    print("V: ")
    print(v)
    invers_v = np.linalg.inv(v)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_v: ")
    print(invers_v, "\n")

    print("W: ")
    print(w)
    invers_w = np.linalg.inv(w)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_w: ")
    print(invers_w, "\n")

    print("X: ")
    print(x_arr)
    invers_x_arr = np.linalg.inv(x_arr)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_x: ")
    print(invers_x_arr, "\n")

    print("Y: ")
    print(y_arr)
    invers_y_arr = np.linalg.inv(y_arr)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_y: ")
    print(invers_y_arr, "\n")

    print("z: ")
    print(z)
    invers_z = np.linalg.inv(z)
    np.set_printoptions(precision=2, suppress=True)
    print("invers_z: ")
    print(invers_z, "\n")

def fizz_buzz():
    x = int(input("masukan batas bawah: "))
    y = int(input("masukan batas atas: "))
    for angka in range(x, y+1):
        if angka % 3 == 0:
            print("FizzBuzz")
        elif angka % 5 == 0:
            print("FizzBuzz")
        else:
            print(angka)

def luas_persegi_panjang():
    a = int(input("masukan nilai panjang: "))
    b = int(input("masukan nilai tinggi: "))

    luas = a * b

    print("Luas persegi: ")
    print(luas)

def waktu():
    def tampilkan_jam_berulang():
        while True:
            saat_ini = time.localtime()
            jam = saat_ini.tm_hour
            menit = saat_ini.tm_min
            detik = saat_ini.tm_sec

            print(f"Sekarang jam: {jam:02d}:{menit:02d}:{detik:02d}")

            time.sleep(1) 

    if __name__ == "__main__":
        tampilkan_jam_berulang()

def run_program(program_number):
    if program_number == 1:
        print_odd_numbers()
    elif program_number == 2:
        create_account()
    elif program_number == 3:
        fibonacci_sequence()
    elif program_number == 4:
        calculate_discount()
    elif program_number == 5:
        number_to_check = simpledialog.askinteger("Input", "Masukkan angka untuk dicek:")
        if is_prime(number_to_check):
            messagebox.showinfo("Hasil", f"{number_to_check} adalah bilangan prima.")
        else:
            messagebox.showinfo("Hasil", f"{number_to_check} bukan bilangan prima.")
    elif program_number == 6:
        transpose_matrix()
    elif program_number == 7:
        calculate_grades()
    elif program_number == 8:
        simple_calculator()
    elif program_number == 9:
        segitiga_pagar()
    elif program_number == 10:
        array_acak()
    elif program_number == 11:
        fizz_buzz()
    elif program_number == 12:
        luas_persegi_panjang()
    elif program_number == 13:
        waktu()
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")

def create_gui():
    root = Tk()
    root.title("Program Selector")

    def run_selected_program():
        selected_program = int(selected_program_var.get())
        run_program(selected_program)

    label = Tk.Label(root, text="Pilih program:")
    label.pack(pady=10)

    selected_program_var = Tk.StringVar()
    program_choices = [str(i) for i in range(1, 14)] + ["0"]
    program_menu = Tk.OptionMenu(root, selected_program_var, *program_choices)
    program_menu.pack(pady=10)

    run_button = Tk.Button(root, text="Jalankan Program", command=run_selected_program)
    run_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()