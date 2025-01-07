# Tiket.py
class Tiket:
    def __init__(self, kode_tiket, jam_berangkat, harga_tiket):
        self.kode_tiket = kode_tiket
        self.jam_berangkat = jam_berangkat
        self.harga_tiket = harga_tiket

class DataTiket:
    def __init__(self):
        self.data_tiket = []

    def tambah_tiket(self, tiket):
        self.data_tiket.append(tiket)

    def hapus_tiket(self, kode_tiket):
        self.data_tiket = [tiket for tiket in self.data_tiket if tiket.kode_tiket != kode_tiket]

    def tampilkan_semua_tiket(self):
        return self.data_tiket

    def cari_tiket(self, kode_tiket):
        for tiket in self.data_tiket:
            if tiket.kode_tiket == kode_tiket:
                return tiket
        return None
