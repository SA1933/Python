username = input("Masukkan username: ")
password = input("Masukkan password: ")

max_attempts = 3
attempts = 0

while True:
    confirm_password = input("Konfirmasi password: ")
    if password == confirm_password:
        print("Akun berhasil dibuat!")
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