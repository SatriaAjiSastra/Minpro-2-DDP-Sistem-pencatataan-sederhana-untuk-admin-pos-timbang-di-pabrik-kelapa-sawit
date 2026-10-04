from datetime import datetime

#Buat nyimpan data pengguna(Username, Password, Role)
database_user = {
    "admin": {"password": "123", "role": "admin"},
    "operator": {"password": "456", "role": "operator"}
}

#Buat nyimpan data timbangan 
data_timbangan = []

#Fungsi Program

def login():
    print("   LOGIN SISTEM POS TIMBANG SAWIT")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    
    if username in database_user and database_user[username]["password"] == password:
        role = database_user[username]["role"]
        print(f"Login Berhasil! Selamat datang, {username} ({role.upper()})")
        return username, role
    else:
        print("Login Gagal! Username atau Password salah")
        return None, None

def tambah_data():
    print("INPUT DATA TRUK MASUK (BRUTO)")
    nama = input("Masukkan Nama Supir: ")
    plat = input("Masukkan Nomor Plat Truk: ")
    
    #cek inputan angka bruto
    while True:
        try:
            bruto = int(input("Masukkan Berat Bruto (Kg): "))
            if bruto > 0:
                break
            print("Berat bruto harus lebih besar dari 0!")
        except ValueError:
            print("Input harus berupa angka!")
            
    waktu_masuk = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #masukin data ke dictionary
    truk = {
        "supir": nama,
        "plat": plat,
        "bruto": bruto,
        "tara": 0,
        "netto": 0,
        "waktu": waktu_masuk
    }
    
    data_timbangan.append(truk)
    print("Sukses! Data truk berhasil dicatat ke sistem.")

def lihat_data():
    print("REKAP DATA TIMBANGAN TRUK SAWIT")
    if len(data_timbangan) == 0:
        print("Belum ada data transaksi timbangan.")
    else:
        # perulangan data
        for i in range(len(data_timbangan)):
            t = data_timbangan[i]
            print(f"Data ke-{i + 1}")
            print(f"  - Waktu Masuk : {t['waktu']}")
            print(f"  - Supplier    : {t['supir']}")
            print(f"  - Plat Truk   : {t['plat']}")
            print(f"  - Bruto (Kg)  : {t['bruto']}")
            print(f"  - Tara (Kg)   : {t['tara']}")
            print(f"  - Netto (Kg)  : {t['netto']}")
            print("-" * 35)

def proses_timbang_keluar():
    print("PROSES TIMBANG KELUAR & HITUNG NETTO")
    if len(data_timbangan) == 0:
        print("Belum ada data truk yang bisa diproses.")
        return
        
    for i in range(len(data_timbangan)):
        t = data_timbangan[i]
        print(f"[{i + 1}] Supplier: {t['supir']} | Plat: {t['plat']} | Bruto: {t['bruto']} Kg")
        
    try:
        nomor = int(input("Pilih nomor data truk yang mau ditimbang keluar: "))
        indeks = nomor - 1
        
        if 0 <= indeks < len(data_timbangan):
            data_lama = data_timbangan[indeks]
            
            while True:
                try:
                    tara = int(input("Masukkan Berat Tara / Kosong Truk (Kg): "))
                    if tara >= 0:
                        break
                    print("Berat tara tidak boleh negatif!")
                except ValueError:
                    print("Input harus berupa angka!")
                    
            bruto_lama = data_lama["bruto"]
            netto = bruto_lama - tara
            
            if netto < 0:
                print("Error: Berat tara tidak boleh lebih besar dari bruto!")
            else:
                #Update nilai tara dan netto
                data_timbangan[indeks]["tara"] = tara
                data_timbangan[indeks]["netto"] = netto
                print(f"Sukses! Berat Bersih (Netto) sawit adalah: {netto} Kg")
        else:
            print("Nomor truk tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

def hapus_data():
    print("HAPUS DATA TIMBANGAN")
    if len(data_timbangan) == 0:
        print("Belum ada data untuk dihapus.")
        return
        
    for i in range(len(data_timbangan)):
        t = data_timbangan[i]
        print(f"[{i + 1}] Supplier: {t['supir']} | Plat: {t['plat']}")
        
    try:
        nomor = int(input("Pilih nomor data yang ingin dihapus: "))
        indeks = nomor - 1
        
        if 0 <= indeks < len(data_timbangan):
            data_timbangan.pop(indeks)
            print("Data berhasil dihapus dari sistem.")
        else:
            print("Nomor data tidak ditemukan!")
    except ValueError:
        print("Input harus berupa angka!")

#memanggil semua sistem

def main():
    while True:
        username, role = login()
        if username is not None:
            while True:
                print(f"   SISTEM POS TIMBANG SAWIT ({role.upper()})")
                print("1. Tambah Data Truk Masuk (Timbang Bruto)")
                print("2. Lihat Daftar Rekap Timbangan")
                print("3. Ubah Data & Timbang Keluar (Hitung Netto)")
                
                #Admin
                if role == "admin":
                    print("4. Hapus Data Timbangan")
                    print("5. Logout / Ganti Akun")
                    print("6. Keluar Program")
                    max_menu = 6
                else:
                    print("4. Logout / Ganti Akun")
                    print("5. Keluar Program")
                    max_menu = 5
                
                try:
                    pilihan = int(input(f"Pilih menu (1-{max_menu}): "))
                except ValueError:
                    print("Pilihan tidak valid! Masukkan angka.")
                    continue
                
                if pilihan == 1:
                    tambah_data()
                elif pilihan == 2:
                    lihat_data()
                elif pilihan == 3:
                    proses_timbang_keluar()
                elif role == "admin" and pilihan == 4:
                    hapus_data()
                elif (role == "admin" and pilihan == 5) or (role == "operator" and pilihan == 4):
                    print("Berhasil logout dari akun.")
                    break
                elif (role == "admin" and pilihan == 6) or (role == "operator" and pilihan == 5):
                    print("Program selesai. Terima kasih telah menggunakan sistem pos timbang!")
                    return
                else:
                    print("Pilihan menu tidak valid!")

main()