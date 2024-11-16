username = input("Masukkan username: ")
password = input("Masukkan password: ")

max_attempts = 3
attempts = 0

while True:
    confirm_password = input("Konfirmasi password: ")
    
    if password == confirm_password and password.isalnum():
        print("Akun berhasil dibuat!")
        break
    else:
        attempts += 1
        if attempts >= max_attempts:
            print(f"Anda telah mencoba konfirmasi password sebanyak {max_attempts} kali.")
            print("Silakan buat password baru.")
            password = input("Masukkan password baru: ")
            attempts = 0
        else:
            if not password.isalnum():
                print("Password tidak memenuhi syarat. Gunakan huruf dan angka saja.")
            else:
                print(f"Password dan konfirmasi password tidak cocok. Sisa percobaan: {max_attempts - attempts}")