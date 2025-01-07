## **Project UAS**

## ** NAMA : LENI**
## ** KELAS : TI.24.A5**
## ** NIM : 312410442**

penjelasan bagaimana program ini dirancang dan cara kerjanya sesuai dengan permintaan:

### **1. Tiket.py (Model Data)**
File ini berfungsi sebagai *data model* yang mendefinisikan struktur dan operasi dasar untuk mengelola data tiket.  

#### **Komponen Utama**
1. **Class Tiket**  
   - **Tujuan:** Merepresentasikan satu tiket dengan atribut:
     - `kode_tiket`: Kode unik tiket (misal, A123).
     - `jam_berangkat`: Waktu keberangkatan dalam format jam (HH:MM).
     - `harga_tiket`: Harga tiket dalam bentuk angka (misal, 150000).
   - **Contoh:** 
     ```python
     tiket = Tiket("A123", "09:00", 150000)
     ```

2. **Class DataTiket**  
   - Menyediakan *list* (`data_tiket`) untuk menyimpan objek tiket.
   - Metode:
     - `tambah_tiket(tiket)`: Menambah tiket baru ke dalam list.
     - `hapus_tiket(kode_tiket)`: Menghapus tiket berdasarkan `kode_tiket`.
     - `tampilkan_semua_tiket()`: Mengembalikan semua tiket dalam bentuk list.
     - `cari_tiket(kode_tiket)`: Mencari tiket berdasarkan `kode_tiket`. Jika tidak ditemukan, mengembalikan `None`.

---

### **2. Tiket_view.py (Tampilan Data)**
File ini bertanggung jawab untuk menampilkan data tiket dalam format tabel yang rapi menggunakan library `tabulate`.

#### **Komponen Utama**
1. **Class TiketView**
   - Metode:
     - `tampilkan_tiket(data_tiket)`: Menampilkan semua tiket dalam format tabel. Jika tidak ada data tiket, mencetak pesan "Tidak ada data tiket."
     - `tampilkan_detail_tiket(tiket)`: Menampilkan informasi detail satu tiket (kode, jam, dan harga).

#### **Tabulate**
- Library ini digunakan untuk membuat tabel teks yang rapi di terminal.
- **Contoh Output Tabel:**
  ```
  +-------------+-----------------+-------------+
  | Kode Tiket  | Jam Berangkat   | Harga Tiket |
  +-------------+-----------------+-------------+
  | A123        | 09:00           | 150000      |
  +-------------+-----------------+-------------+
  ```

---

### **3. Tiket_process.py (Proses Input Data)**
File ini mengelola input data dari pengguna. 

#### **Komponen Utama**
1. **Class TiketProcess**
   - Metode:
     - `input_tiket()`: 
       - Meminta pengguna untuk memasukkan `kode_tiket`, `jam_berangkat`, dan `harga_tiket`.
       - **Validasi:** Jika harga tiket tidak berupa angka (misalnya pengguna memasukkan huruf), akan muncul pesan kesalahan dan data tidak disimpan.

#### **Validasi Input**
- Dilakukan untuk memastikan input sesuai format yang diinginkan, seperti:
  - Harga tiket harus berupa angka.
  - Format kode tiket bisa diperiksa lebih lanjut jika diperlukan.

---

### **4. Main.py (Program Utama)**
File ini adalah titik masuk (entry point) program yang menyediakan menu interaktif kepada pengguna.

#### **Fungsi Utama**
1. **Menu Utama**
   - Terdapat pilihan:
     - Tambah Data Tiket
     - Hapus Data Tiket
     - Tampilkan Semua Data Tiket
     - Keluar dari program

2. **Alur Program**
   - **Tambah Data Tiket:**
     - Memanggil `input_tiket()` dari `TiketProcess` untuk mendapatkan input pengguna.
     - Data tiket ditambahkan ke list menggunakan `tambah_tiket()` dari `DataTiket`.

   - **Hapus Data Tiket:**
     - Meminta pengguna memasukkan `kode_tiket`.
     - Menghapus tiket dengan memanggil `hapus_tiket()` dari `DataTiket`.

   - **Tampilkan Semua Data Tiket:**
     - Memanggil `tampilkan_tiket()` dari `TiketView` untuk menampilkan semua tiket dalam bentuk tabel.

   - **Keluar:**
     - Program akan berhenti.

---

### **Contoh Alur Program**
1. **Menambah Tiket**
   - Input:  
     ```
     Masukkan kode tiket: A123
     Masukkan jam berangkat (HH:MM): 09:00
     Masukkan harga tiket: 150000
     ```
   - Output:  
     ```
     Tiket berhasil ditambahkan.
     ```

2. **Menampilkan Semua Tiket**
   - Output:  
     ```
     +-------------+-----------------+-------------+
     | Kode Tiket  | Jam Berangkat   | Harga Tiket |
     +-------------+-----------------+-------------+
     | A123        | 09:00           | 150000      |
     +-------------+-----------------+-------------+
     ```

3. **Menghapus Tiket**
   - Input:  
     ```
     Masukkan kode tiket yang ingin dihapus: A123
     ```
   - Output:  
     ```
     Tiket berhasil dihapus.
     ```

4. **Tampilan Setelah Tiket Dihapus**
   - Output:  
     ```
     Tidak ada data tiket.
     ```

---

### **Keunggulan Program**
1. **Modular dan Terorganisir:** 
   - Tiap file memiliki tanggung jawab yang spesifik, memudahkan pengembangan dan debugging.
   
2. **Validasi Input:** 
   - Menjamin data yang dimasukkan sesuai dengan format yang diharapkan.

3. **Output Rapi:** 
   - Data ditampilkan dalam bentuk tabel menggunakan library `tabulate`.

4. **Mudah Dipahami:** 
   - Menggunakan alur sederhana dengan operasi CRUD (Create, Read, Update, Delete).
  

## Link YT
[Youtube - PROJECT UAS](https://youtu.be/2houbTw_eDI)




