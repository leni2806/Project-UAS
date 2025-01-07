# Tiket_process.py
class TiketProcess:
    def input_tiket(self):
        try:
            kode_tiket = input("Masukkan kode tiket: ")
            jam_berangkat = input("Masukkan jam berangkat (HH:MM): ")
            harga_tiket = float(input("Masukkan harga tiket: "))
            return kode_tiket, jam_berangkat, harga_tiket
        except ValueError:
            print("Input tidak valid! Pastikan harga tiket berupa angka.")
            return None, None, None
