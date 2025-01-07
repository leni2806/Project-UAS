# Tiket_view.py
from tabulate import tabulate

class TiketView:
    def tampilkan_tiket(self, data_tiket):
        if not data_tiket:
            print("Tidak ada data tiket.")
            return
        
        table = []
        for tiket in data_tiket:
            table.append([tiket.kode_tiket, tiket.jam_berangkat, tiket.harga_tiket])
        
        print(tabulate(table, headers=["Kode Tiket", "Jam Berangkat", "Harga Tiket"], tablefmt="grid"))
    
    def tampilkan_detail_tiket(self, tiket):
        if tiket:
            print(f"Kode Tiket: {tiket.kode_tiket}")
            print(f"Jam Berangkat: {tiket.jam_berangkat}")
            print(f"Harga Tiket: {tiket.harga_tiket}")
        else:
            print("Tiket tidak ditemukan.")
