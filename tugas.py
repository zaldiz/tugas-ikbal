class buku:
    def _init_(self, judul, penulis, genre, status):
        self.judul = judul
        self.penulis = penulis
        self.genre = genre
        self.status = status

        def _str_(self):
            return f"{self.judul} - {self.penulis} - {self.genre} - {self.status}"

class perpustakaan:
    def _init_(self):
        self.koleksi_buku = []

    def tampilkan_buku(self):
        if self.koleksi_buku:
            print("-- Daftar Buku --")
            for buku in self.koleksi_buku:
                print(buku)
        else:
            print("koleksi buku masih kosong!")

    def cari_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                print(buku)
                return
                print(f"Buku dengan judul '{buku.judul}' berhasil dipinjam oleh {anggota.nama}.")
    def cari_buku(self, buku, anggota):
            if buku.status == "Tersedia":
                buku.status = "Dipinjam"
                anggota.buku_pinjaman.append(buku)
                print(f"Buku '{buku.judul}' berhasil dipinjam oleh '{anggota.nama}'")
            else:
                print(f"Buku '{buku.judul}' tidak tersedia untuk dipinjam")

class anggota:
    def _init_(self, nama, ID):
        self.nama = nama
        self.ID = ID
        self.buku_pinjaman = []

    def tampilkan_buku_pinjam(self):
        if self.tampilkan_buku_pinjam:
            print(f"-- Buku pinjam {self.nama} --")
            for buku in self.buku_pinjaman:
                print(buku)
            else:
                print(f"{self.nama} tidak memiliki buku pinjaman!")

    def main():
        # buat beberapa buku
        buku1 = buku("Retorika", "Aristoteles", "Filsafat", "Tersedia")
        buku2 = buku("Economic analysis of law", "Richard Posner", "Ekonomi", "Tersedia")
        buku3 = buku("Pentinya Belajar Coding", "Yeni Mulyani", "Edukasi", "Dipinjam")

        # Buat Perpustakaan dan anggota
        perpustakaan = perpustakaan()
        perpustakaan.koleksi_buku.extend([buku1, buku2, buku3])

        anggota1 = anggota("Andi", 12345)
        anggota2 = anggota("Budi", 56789)

        # Jalankan Program
        print("\n -- Welcome to Perpustakaan --")
        print("1. Tampilkan Daftar Buku")
        print("2. Cari Buku")
        print("3. Pinjam Buku")
        print("4. kembalikan")
        angka = int(input("Pilih Menu :_"))

        if angka == 1:
            perpustakaan.tampilkan_buku();
        elif angka == 2:
            judul = input("input judul buku: ")
            perpustakaan.cari_buku(judul);
        elif angka == 3:
            buku = input("Buku yang di pinjam: ")
            agota = input("Masukan nama anggota: ")
            perpustakaan.pinjam_buku(buku,anggota)
        else:
            print("Anda salah pilih!")
