import numpy as np
import time
import tkinter as tk
from tkinter import Tk, simpledialog, messagebox, Text, END

def print_odd_numbers(output_widget):
    output_widget.insert(END, "Program Menampilkan Angka Ganjil:\n")
    for angka in range(1, 1001):
        if angka % 2 != 0:
            output_widget.insert(END, f"{angka}\n")

def create_account(output_widget):
    output_widget.insert(END, "Program Pembuatan Akun:\n")
    username = simpledialog.askstring("Input", "Masukkan username:")
    password = simpledialog.askstring("Input", "Masukkan password:")

    max_attempts = 3
    attempts = 0

    while True:
        confirm_password = simpledialog.askstring("Input", "Konfirmasi password:")
        if password == confirm_password:
            output_widget.insert(END, "Selamat, Akun berhasil dibuat!\n")
            break
        else:
            attempts += 1
            if attempts >= max_attempts:
                output_widget.insert(END, f"Anda telah mencoba konfirmasi password sebanyak {max_attempts} kali.\n")
                output_widget.insert(END, "Silahkan buat password baru.\n")
                password = simpledialog.askstring("Input", "Masukkan password baru:")
                attempts = 0
            else:
                output_widget.insert(END, f"Password tidak memenuhi syarat, silakan coba lagi. Sisa percobaan: {max_attempts - attempts}\n")

def fibonacci_sequence(output_widget):
    output_widget.insert(END, "Program Urutan Fibonacci:\n")
    panjang_urutan = simpledialog.askinteger("Input", "Masukkan panjang urutan Fibonacci:")
    a, b = 0, 1
    urutan_fibonacci = []
    while len(urutan_fibonacci) < panjang_urutan:
        urutan_fibonacci.append(a)
        a, b = b, a + b
    output_widget.insert(END, f"Urutan Fibonacci dengan panjang {panjang_urutan} adalah:\n")
    output_widget.insert(END, f"{urutan_fibonacci}\n")

def calculate_discount(output_widget):
    total_harga = 0
    daftar_barang = []
    while True:
        try:
            nama_barang = simpledialog.askstring("Input", f"Masukkan nama barang ke-{len(daftar_barang) + 1} (atau 'selesai' untuk mengakhiri): ")
            if nama_barang.lower() == 'selesai':
                break
            harga = float(simpledialog.askstring("Input", f"Masukkan harga {nama_barang}: "))
            if harga < 0:
                output_widget.insert(END, "Harga tidak valid. Harap masukkan harga yang benar.\n")
                continue
            total_harga += harga
            daftar_barang.append((nama_barang, harga))
        except ValueError:
            output_widget.insert(END, "Harga tidak valid. Harap masukkan harga yang benar.\n")
    output_widget.insert(END, f"Total harga sebelum diskon: {total_harga:.2f} Rupiah\n")

    if total_harga > 200000:
        diskon = min(total_harga * 0.10, 100000)
    elif total_harga > 40000:
        diskon = min(total_harga * 0.05, 100000)
    else:
        diskon = 0

    total_harga_diskon = total_harga - diskon

    output_widget.insert(END, f"Total harga setelah mendapatkan diskon: {total_harga_diskon:.2f} Rupiah\n")
    output_widget.insert(END, "Daftar Barang:\n")
    for nama, harga in daftar_barang:
        output_widget.insert(END, f"{nama}: {harga:.2f} Rupiah\n")
    output_widget.insert(END, f"Diskon: {diskon:.2f} Rupiah\n")

def is_prime(number, output_widget):
    if number < 2:
        output_widget.insert(END, "Bukan bilangan prima\n")
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            output_widget.insert(END, "Bukan bilangan prima\n")
            return False
    output_widget.insert(END, "Bilangan prima\n")
    return True

def transpose_matrix(output_widget):
    output_widget.insert(END, "Program Transposisi Matriks:\n")
    m = int(simpledialog.askinteger("Input", "Masukkan jumlah baris: "))
    n = int(simpledialog.askinteger("Input", "Masukkan jumlah kolom: "))
    matrix = [[int(simpledialog.askinteger("Input", f"Masukkan elemen di posisi ({i+1}, {j+1}): ")) for j in range(n)] for i in range(m)]

    output_widget.insert(END, "\nMatriks:\n")
    output_widget.insert(END, "\n".join(" ".join(map(str, row)) for row in matrix) + "\n")

    transposed_matrix = [[matrix[j][i] for j in range(m)] for i in range(n)]
    output_widget.insert(END, "\nMatriks Transposisi:\n")
    output_widget.insert(END, "\n".join(" ".join(map(str, row)) for row in transposed_matrix) + "\n")

def calculate_grades(output_widget):
    output_widget.insert(END, "Program Perhitungan Nilai, Grade, dan Status:\n")
    while True:
        try:
            tugas = float(simpledialog.askstring("Input", "Masukkan nilai Tugas: "))
            uts = float(simpledialog.askstring("Input", "Masukkan nilai UTS: "))
            uas = float(simpledialog.askstring("Input", "Masukkan nilai UAS: "))
 
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

            output_widget.insert(END, f"Nilai Akhir: {nilai:.2f}\n")
            output_widget.insert(END, f"Grade: {grade}\n")
            output_widget.insert(END, f"Status: {status}\n")

        except ValueError:
            output_widget.insert(END, "Masukan tidak valid. Harap masukkan lagi nilai tugas, uts, dan uas\n")
    
        lanjutkan = simpledialog.askstring("Input", "Apakah Anda ingin memasukkan angka lagi? (ya/tidak): ")
        if lanjutkan.lower() != "ya":
            break

def simple_calculator(output_widget):
    hasil = None

    while True:
        try:
            if hasil is None:
                angka1 = float(simpledialog.askstring("Input", "Masukkan angka pertama: "))
            else:
                angka1 = hasil

            operasi = simpledialog.askstring("Input", "Masukkan operasi (+, -, *, /) atau '=' untuk mengakhiri: ")

            if operasi == '=':
                output_widget.insert(END, f"Hasil akhir: {hasil}\n")
                break

            angka2 = float(simpledialog.askstring("Input", "Masukkan angka kedua: "))

            if operasi == '+':
                hasil = angka1 + angka2
            elif operasi == '-':
                hasil = angka1 - angka2
            elif operasi == '*':
                hasil = angka1 * angka2
            elif operasi == '/':
                if angka2 == 0:
                    output_widget.insert(END, "Tidak dapat membagi dengan nol\n")
                    hasil = None
                else:
                    hasil = angka1 / angka2
            else:
                output_widget.insert(END, "Operasi tidak valid. Silakan coba lagi.\n")
                hasil = None

            if hasil is not None:
                output_widget.insert(END, f"Hasil: {hasil}\n")
        except ValueError:
            output_widget.insert(END, "Masukan tidak valid. Silakan coba lagi.\n")
            hasil = None

def segitiga_pagar(output_widget):
    tinggi = int(simpledialog.askinteger("Input", "Masukkan tinggi segitiga: "))
    for i in range(1, tinggi + 1):
        output_widget.insert(END, "#" * i + "\n")

def array_acak(output_widget):
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

    output_widget.insert(END, "\nA: \n")
    output_widget.insert(END, f"{a}\n")
    invers_a = np.linalg.inv(a)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_a: \n")
    output_widget.insert(END, f"{invers_a}\n")

    output_widget.insert(END, "\nB: \n")
    output_widget.insert(END, f"{b}\n")
    invers_b = np.linalg.inv(b)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_b: \n")
    output_widget.insert(END, f"{invers_b}\n")

    output_widget.insert(END, "\nC: \n")
    output_widget.insert(END, f"{c}\n")
    invers_c = np.linalg.inv(c)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_c: \n")
    output_widget.insert(END, f"{invers_c}\n")

    output_widget.insert(END, "\nD: \n")
    output_widget.insert(END, f"{d}\n")
    invers_d = np.linalg.inv(d)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_d: \n")
    output_widget.insert(END, f"{invers_d}\n")

    output_widget.insert(END, "\nE: \n")
    output_widget.insert(END, f"{e}\n")
    invers_e = np.linalg.inv(e)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_e: \n")
    output_widget.insert(END, f"{invers_e}\n")

    output_widget.insert(END, "\nF: \n")
    output_widget.insert(END, f"{f}\n")
    invers_f = np.linalg.inv(f)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_f: \n")
    output_widget.insert(END, f"{invers_f}\n")

    output_widget.insert(END, "\nG: \n")
    output_widget.insert(END, f"{g}\n")
    invers_g = np.linalg.inv(g)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_g: \n")
    output_widget.insert(END, f"{invers_g}\n")

    output_widget.insert(END, "\nH: \n")
    output_widget.insert(END, f"{h}\n")
    invers_h = np.linalg.inv(h)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_h: \n")
    output_widget.insert(END, f"{invers_h}\n")

    output_widget.insert(END, "\nI: \n")
    output_widget.insert(END, f"{i}\n")
    invers_i = np.linalg.inv(i)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_i: \n")
    output_widget.insert(END, f"{invers_i}\n")

    output_widget.insert(END, "\nJ: \n")
    output_widget.insert(END, f"{j}\n")
    invers_j = np.linalg.inv(j)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_j: \n")
    output_widget.insert(END, f"{invers_j}\n")

    output_widget.insert(END, "\nK: \n")
    output_widget.insert(END, f"{k}\n")
    invers_k = np.linalg.inv(k)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_k: \n")
    output_widget.insert(END, f"{invers_k}\n")

    output_widget.insert(END, "\nL: \n")
    output_widget.insert(END, f"{l}\n")
    invers_l = np.linalg.inv(l)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_l: \n")
    output_widget.insert(END, f"{invers_l}\n")

    output_widget.insert(END, "\nM: \n")
    output_widget.insert(END, f"{m_arr}\n")
    invers_m_arr = np.linalg.inv(m_arr)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_m: \n")
    output_widget.insert(END, f"{invers_m_arr}\n")

    output_widget.insert(END, "\nN: \n")
    output_widget.insert(END, f"{n_arr}\n")
    invers_n_arr = np.linalg.inv(n_arr)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_n: \n")
    output_widget.insert(END, f"{invers_n_arr}\n")

    output_widget.insert(END, "\nO: \n")
    output_widget.insert(END, f"{o}\n")
    invers_o = np.linalg.inv(o)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_o: \n")
    output_widget.insert(END, f"{invers_o}\n")

    output_widget.insert(END, "\nP: \n")
    output_widget.insert(END, f"{p}\n")
    invers_p = np.linalg.inv(p)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_p: \n")
    output_widget.insert(END, f"{invers_p}\n")

    output_widget.insert(END, "\nQ: \n")
    output_widget.insert(END, f"{q}\n")
    invers_q = np.linalg.inv(q)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_q: \n")
    output_widget.insert(END, f"{invers_q}\n")

    output_widget.insert(END, "\nR: \n")
    output_widget.insert(END, f"{r}\n")
    invers_r = np.linalg.inv(r)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_r: \n")
    output_widget.insert(END, f"{invers_r}\n")

    output_widget.insert(END, "\nS: \n")
    output_widget.insert(END, f"{s}\n")
    invers_s = np.linalg.inv(s)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_s: \n")
    output_widget.insert(END, f"{invers_s}\n")

    output_widget.insert(END, "\nT: \n")
    output_widget.insert(END, f"{t}\n")
    invers_t = np.linalg.inv(t)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_t: \n")
    output_widget.insert(END, f"{invers_t}\n")

    output_widget.insert(END, "\nU: \n")
    output_widget.insert(END, f"{u}\n")
    invers_u = np.linalg.inv(u)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_u: \n")
    output_widget.insert(END, f"{invers_u}\n")

    output_widget.insert(END, "\nV: \n")
    output_widget.insert(END, f"{v}\n")
    invers_v = np.linalg.inv(v)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_v: \n")
    output_widget.insert(END, f"{invers_v}\n")

    output_widget.insert(END, "\W: \n")
    output_widget.insert(END, f"{w}\n")
    invers_w = np.linalg.inv(w)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_w: \n")
    output_widget.insert(END, f"{invers_w}\n")

    output_widget.insert(END, "\nX: \n")
    output_widget.insert(END, f"{x_arr}\n")
    invers_x_arr = np.linalg.inv(x_arr)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_x: \n")
    output_widget.insert(END, f"{invers_x_arr}\n")

    output_widget.insert(END, "\nY: \n")
    output_widget.insert(END, f"{y_arr}\n")
    invers_y_arr = np.linalg.inv(y_arr)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_y: \n")
    output_widget.insert(END, f"{invers_y_arr}\n")

    output_widget.insert(END, "\nZ: \n")
    output_widget.insert(END, f"{z}\n")
    invers_z = np.linalg.inv(z)
    np.set_printoptions(precision=2, suppress=True)
    output_widget.insert(END, "\ninvers_z: \n")
    output_widget.insert(END, f"{invers_z}\n")

def fizz_buzz(output_widget):
    x = int(simpledialog.askinteger("Input", "Masukkan batas bawah: "))
    y = int(simpledialog.askinteger("Input", "Masukkan batas atas: "))
    for angka in range(x, y+1):
        if angka % 3 == 0 and angka % 5 == 0:
            output_widget.insert(END, "FizzBuzz\n")
        elif angka % 3 == 0:
            output_widget.insert(END, "Fizz\n")
        elif angka % 5 == 0:
            output_widget.insert(END, "Buzz\n")
        else:
            output_widget.insert(END, f"{angka}\n")

def luas_persegi_panjang(output_widget):
    a = int(simpledialog.askinteger("Input", "Masukkan nilai panjang: "))
    b = int(simpledialog.askinteger("Input", "Masukkan nilai tinggi: "))

    luas = a * b

    output_widget.insert(END, "Luas persegi: \n")
    output_widget.insert(END, f"{luas}\n")

def waktu(output_widget):
    def tampilkan_jam_berulang():
        while True:
            saat_ini = time.localtime()
            jam = saat_ini.tm_hour
            menit = saat_ini.tm_min
            detik = saat_ini.tm_sec

            output_widget.insert(END, f"Sekarang jam: {jam:02d}:{menit:02d}:{detik:02d}\n")

            time.sleep(1)

def run_program(program_number, output_widget):
    if program_number == 1:
        print_odd_numbers(output_widget)
    elif program_number == 2:
        create_account(output_widget)
    elif program_number == 3:
        fibonacci_sequence(output_widget)
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

    output_text = Text(root, height=20, width=50)
    output_text.pack(pady=10)

    def run_selected_program():
        selected_program = int(selected_program_var.get())
        output_text.delete(1.0, END)
        run_program(selected_program, output_text)

    label = tk.Label(root, text="Pilih program:")
    label.pack(pady=10)

    selected_program_var = tk.StringVar()
    program_choices = [str(i) for i in range(1, 14)] + ["0"]
    program_menu = tk.OptionMenu(root, selected_program_var, *program_choices)
    program_menu.pack(pady=10)

    run_button = tk.Button(root, text="Jalankan Program", command=run_selected_program)
    run_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()