# Main.py
from Data.Tiket import Tiket, DataTiket
from View.Tiket_View import TiketView
from Process.Tiket_Process import TiketProcess

def main():
    data_tiket = DataTiket()
    tiket_view = TiketView()
    tiket_process = TiketProcess()

    while True:
        print("\nMenu:")
        print("1. Tambah Data Tiket")
        print("2. Hapus Data Tiket")
        print("3. Tampilkan Semua Data Tiket")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':  # Tambah Data Tiket
            kode_tiket, jam_berangkat, harga_tiket = tiket_process.input_tiket()
            if kode_tiket and jam_berangkat and harga_tiket:
                tiket_baru = Tiket(kode_tiket, jam_berangkat, harga_tiket)
                data_tiket.tambah_tiket(tiket_baru)
                print("Tiket berhasil ditambahkan.")
        
        elif pilihan == '2':  # Hapus Data Tiket
            kode_tiket = input("Masukkan kode tiket yang ingin dihapus: ")
            tiket = data_tiket.cari_tiket(kode_tiket)
            if tiket:
                data_tiket.hapus_tiket(kode_tiket)
                print("Tiket berhasil dihapus.")
            else:
                print("Tiket tidak ditemukan.")
        
        elif pilihan == '3':  # Tampilkan Semua Data Tiket
            tiket_view.tampilkan_tiket(data_tiket.tampilkan_semua_tiket())
        
        elif pilihan == '4':  # Keluar
            print("Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
