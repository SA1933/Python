def is_valid_password(password):
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_lowercase and has_uppercase and has_digit

def create_account():
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        confirm_password = input("Konfirmasi password: ")

        if password == confirm_password and is_valid_password(password):
            print("Akun berhasil dibuat!")
            break
        else:
            print("Password tidak memenuhi syarat. Pastikan password mengandung huruf besar, huruf kecil, dan angka, dan konfirmasi password cocok. Coba lagi.")
            
create_account()