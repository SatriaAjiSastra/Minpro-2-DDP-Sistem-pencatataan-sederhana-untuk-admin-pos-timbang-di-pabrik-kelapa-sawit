Nama:Satria Aji Sastra

Nim:2609116019

Kelas:A_26

Prodi:Sistem Informasi

Fakultas:Teknik

<img width="1007" height="1087" alt="Diagram Minpro drawio" src="https://github.com/user-attachments/assets/22581a43-083f-40a3-bc38-6aee02b53bb6" />

Flowchart Alur Program


Penjelasan kode Program 

Sistem Pencatatan Sederhana untuk admin pos timbang di Pabrik Sawit

<img width="629" height="89" alt="Screenshot 2026-10-04 214935" src="https://github.com/user-attachments/assets/1b9085a5-f5a7-4b3a-b2d7-3441bbc3a75c" />

ini adalah Library datetime: untuk mengambil waktu dan tanggal secara real-time saat truk masuk dicatat ke sistem.

<img width="682" height="143" alt="Screenshot 2026-10-04 215245" src="https://github.com/user-attachments/assets/9eeaca55-7360-4f40-9cdd-8cbd87567ea9" />

ini adalah program untuk menyimpan database user

<img width="368" height="82" alt="Screenshot 2026-10-04 215658" src="https://github.com/user-attachments/assets/45f7e92f-93ec-42db-bc1c-290ca2fa385a" />

ini adalah program untuk menyimpan data timbangan

<img width="1080" height="825" alt="Screenshot 2026-10-04 215845" src="https://github.com/user-attachments/assets/8b24d240-d10d-4b2c-be4e-f6db89967531" />

ini adalah program login() untuk menangani proses masuk (login) pengguna dengan meminta input username dan password, lalu mencocokkannya dengan data di dalam sistem untuk menentukan hak akses (role).
ini adalah program tambah_data() untuk mencatat data truk sawit yang baru masuk ke area pabrik, yang mencakup input nama supir, plat nomor, validasi angka untuk berat bruto menggunakan try-except, serta merekam waktu kedatangan secara otomatis menggunakan library datetime.

<img width="760" height="378" alt="Screenshot 2026-10-05 153927" src="https://github.com/user-attachments/assets/f9a193e5-c23c-4b17-b529-d37eb38cbec5" />

ini adalah program untuk menyimpan data transaksi truk baru ke dalam Dictionary, lalu memasukkannya ke dalam List utama (data_timbangan) agar bisa direkap dan diproses selanjutnya.

<img width="722" height="479" alt="Screenshot 2026-10-05 154214" src="https://github.com/user-attachments/assets/f3d563fa-434b-4d5c-9872-016f6be7cc57" />

ini adalah prograam untuk menampilkan daftar rekap atau riwayat semua data transaksi timbangan truk sawit yang sudah termasuk ke dalam sistem.

<img width="1140" height="813" alt="Screenshot 2026-10-05 154517" src="https://github.com/user-attachments/assets/9257aee6-06ff-446e-9029-64c94096f215" />

ini adalah program untuk melakukan proses timbang keluar kendaraan, memasukkan berat kosong truk (tara), dan menghitung berat bersih (netto) kelapa sawit

<img width="904" height="614" alt="Screenshot 2026-10-05 154722" src="https://github.com/user-attachments/assets/dc0bbdc9-1660-4392-bba6-1642dfacfd9e" />

ini adalah program untuk menghapus data transaksi timbangan truk dari sistem berdasarkan nomor urut yang dipilih oleh pengguna (Menu khusus akun ADMIN)

<img width="1133" height="532" alt="Screenshot 2026-10-05 155026" src="https://github.com/user-attachments/assets/2398cb6a-925a-4b09-91aa-4075377999d3" />
<img width="887" height="757" alt="Screenshot 2026-10-05 155000" src="https://github.com/user-attachments/assets/61cd7fbe-bdb0-43b5-a028-c865adb201ef" />

ini adalah program untuk menjalankan login terus menerus, 
Jika yang login adalah admin, sistem akan menampilkan 6 pilihan menu
Jika yang login adalah operator, sistem hanya menampilkan 5 pilihan menu

*OUTPUT*

<img width="536" height="317" alt="Screenshot 2026-10-05 155702" src="https://github.com/user-attachments/assets/2f4cf616-cf6f-4f1c-8e3b-39cd1ecca7ae" />

ini adalah output pertama untuk login akun dan saya login pakai akun Admin

<img width="553" height="177" alt="Screenshot 2026-10-05 155925" src="https://github.com/user-attachments/assets/7ac00cd2-ce2a-4c71-866d-c52087fd18d4" />

ini adalah menu 1 yaitu menu untuk menginput truk yang masuk, Nama sopir, Plat nomor truk, Berat bruto/Berat kotor

<img width="503" height="265" alt="Screenshot 2026-10-05 160202" src="https://github.com/user-attachments/assets/3da9088c-e221-41e1-82e7-164dfc215215" />

ini adalah menu 2 yang berfungsi untuk menampilkan data data truk yang masuk

<img width="617" height="165" alt="Screenshot 2026-10-05 160349" src="https://github.com/user-attachments/assets/cbdfaf4c-d048-42be-9d21-e67ab7f38c07" />

ini adalah output menu 3 menmproses dan menghitung netto/berat bersih 

<img width="468" height="157" alt="Screenshot 2026-10-05 160602" src="https://github.com/user-attachments/assets/d7cf9bea-5b93-4446-9c71-bc0b982dd8a5" />

ini adalah output menu 4 yang berfungsi untuk menghapus data truk yang ingin di hapus

<img width="652" height="345" alt="Screenshot 2026-10-05 160749" src="https://github.com/user-attachments/assets/ab1bb723-3bca-404b-b8e9-6e708e534c59" />

ini adalah output menu ke yang berfungsi untuk pindah akun, saat aku sudah pindah ke operator semua nya masih sama hanya di kurangi 1 menu yaitu tidak ada menu untuk menghapus data seperti di menu admin

<img width="805" height="89" alt="Screenshot 2026-10-05 161122" src="https://github.com/user-attachments/assets/1654937d-c2da-4908-9c8d-500a9b9af0bc" />

terakhir adalah output menu 5 yaitu keluar dari program.












