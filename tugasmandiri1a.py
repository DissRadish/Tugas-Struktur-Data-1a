# TUGAS MANDIRI 1A - STRUKTUR DATA 
# Nama  : RADISH AL SUDAIS
# NIM   : 12550110956
# Prodi : Teknik Informatika
# Kelas : Semester 3, Kelas B


from collections import deque

class SistemAkademik:
    def __init__(self):
        # 1. Array / List : Penyimpanan data berurutan
        self.data_berurutan = []
        
        # 2. Stack : Fitur Undo (LIFO)
        self.undo_stack = []
        
        # 3. Queue : Sistem Antrean Layanan (FIFO)
        self.antrean_layanan = deque()
        
        # 4. Hash Table / Dictionary : Pencarian berdasarkan Key (NIM)
        self.mahasiswa_by_key = {}

    # --- 1. ARRAY & STACK ---
    def tambah_data_berurutan(self, nama_mhs):
        self.data_berurutan.append(nama_mhs)
        self.undo_stack.append(("TAMBAH_DATA", nama_mhs)) # Stack Push O(1)
        print(f"\n[Success] '{nama_mhs}' berhasil ditambahkan ke Array.")

    def undo_aksi(self):
        if not self.undo_stack:
            print("\n[Stack Undo] Tidak ada aksi yang dapat di-undo.")
            return
        
        # Stack Pop O(1) - LIFO
        aksi_terakhir, nilai = self.undo_stack.pop()
        if aksi_terakhir == "TAMBAH_DATA":
            self.data_berurutan.remove(nilai)
            print(f"\n[Stack Undo] Aksi dibatalkan! '{nilai}' dihapus dari Array.")

    def tampilkan_array(self):
        print(f"\n[Array Data Berurutan]: {self.data_berurutan}")

    # --- 2. QUEUE ---
    def tambah_antrean(self, nama_mhs):
        # Queue Enqueue O(1)
        self.antrean_layanan.append(nama_mhs)
        print(f"\n[Queue] '{nama_mhs}' masuk ke antrean.")

    def proses_antrean(self):
        if self.antrean_layanan:
            # Queue Dequeue O(1) - FIFO
            diproses = self.antrean_layanan.popleft()
            print(f"\n[Queue] Memproses antrean mahasiswa: '{diproses}'")
        else:
            print("\n[Queue] Antrean saat ini kosong.")

    def tampilkan_antrean(self):
        print(f"\n[Queue Antrean Layanan]: {list(self.antrean_layanan)}")

    # --- 3. HASH TABLE / DICTIONARY ---
    def simpan_mahasiswa_key(self, nim, nama, prodi):
        # Hash Table Insertion O(1)
        self.mahasiswa_by_key[nim] = {"Nama": nama, "Prodi": prodi}
        print(f"\n[Hash Table] Data NIM '{nim}' berhasil disimpan.")

    def cari_mahasiswa_by_key(self, nim):
        # Hash Table Searching O(1)
        hasil = self.mahasiswa_by_key.get(nim)
        if hasil:
            print(f"\n[Hash Table Result] Data Ditemukan!")
            print(f" -> NIM   : {nim}")
            print(f" -> Nama  : {hasil['Nama']}")
            print(f" -> Prodi : {hasil['Prodi']}")
        else:
            print(f"\n[Hash Table Result] NIM '{nim}' TIDAK DITEMUKAN!")

# MENU INPUT OPTION INTERAKSI UTAMA (COMMAND LINE INTERFACE)

def main():
    sistem = SistemAkademik()
    
    while True:
        print("\n" + "="*50)
        print("     SISTEM AKADEMIK - DEMO STRUKTUR DATA")
        print("="*50)
        print("1. [Array]  Tambah Data Mahasiswa Berurutan")
        print("2. [Array]  Tampilkan Semua Data Berurutan")
        print("3. [Stack]  Undo Aksi Terakhir (LIFO)")
        print("4. [Queue]  Tambah Mahasiswa ke Antrean Layanan")
        print("5. [Queue]  Proses Antrean Terdepan (FIFO)")
        print("6. [Queue]  Tampilkan Daftar Antrean")
        print("7. [Hash]   Simpan Data Mahasiswa (Key: NIM)")
        print("8. [Hash]   Cari Data Mahasiswa Berdasarkan NIM")
        print("0. Keluar Program")
        print("="*50)
        
        pilihan = input("Pilih menu (0-8): ").strip()

        if pilihan == "1":
            nama = input("Masukkan Nama Mahasiswa: ").strip()
            if nama: sistem.tambah_data_berurutan(nama)
        elif pilihan == "2":
            sistem.tampilkan_array()
        elif pilihan == "3":
            sistem.undo_aksi()
        elif pilihan == "4":
            nama = input("Masukkan Nama Mahasiswa Antrean: ").strip()
            if nama: sistem.tambah_antrean(nama)
        elif pilihan == "5":
            sistem.proses_antrean()
        elif pilihan == "6":
            sistem.tampilkan_antrean()
        elif pilihan == "7":
            nim = input("Masukkan NIM   : ").strip()
            nama = input("Masukkan Nama  : ").strip()
            prodi = input("Masukkan Prodi : ").strip()
            if nim and nama: sistem.simpan_mahasiswa_key(nim, nama, prodi)
        elif pilihan == "8":
            nim = input("Masukkan NIM yang dicari: ").strip()
            if nim: sistem.cari_mahasiswa_by_key(nim)
        elif pilihan == "0":
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()