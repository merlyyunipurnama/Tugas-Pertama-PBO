# Contoh Program Pemrograman Fungsional:

# Fungsi untuk menghitung luas lingkaran
def hitung_luas_lingkaran(jari_jari):
    return 3.14 * (jari_jari ** 2)

# Fungsi untuk mengubah list menjadi string
def list_ke_string(lst):
    return ", ".join(str(x) for x in lst)

# Fungsi untuk mengambil bilangan genap dari sebuah list
def ambil_bilangan_genap(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

# Fungsi utama
def main():
    # Menghitung luas lingkaran dengan jari-jari 7
    luas = hitung_luas_lingkaran(7)
    print("Luas lingkaran dengan jari-jari 7 adalah", luas)

    # Mengubah list menjadi string
    angka = [1, 2, 3, 4, 5]
    angka_str = list_ke_string(angka)
    print("List:", angka_str)

    # Mengambil bilangan genap dari list
    angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bilangan_genap = ambil_bilangan_genap(angka)
    bilangan_genap_str = list_ke_string(bilangan_genap)
    print("Bilangan genap dari list:", bilangan_genap_str)

if __name__ == '__main__':
    main()

# Contoh Program Pemrograman Berorientasi Objek: 

# Definisikan kelas Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = []

    def tambah_nilai(self, nilai):
        self.nilai.append(nilai)

    def rata_rata_nilai(self):
        if len(self.nilai) == 0:
            return 0
        else:
            return sum(self.nilai) / len(self.nilai)

# Buat objek dari kelas Mahasiswa
mhs1 = Mahasiswa("John Doe", "123456", "Informatika")

# Tambahkan nilai untuk mahasiswa pertama
mhs1.tambah_nilai(80)
mhs1.tambah_nilai(90)
mhs1.tambah_nilai(85)

# Cetak nama, nim, jurusan, dan rata-rata nilai mahasiswa pertama
print("Nama    :", mhs1.nama)
print("NIM     :", mhs1.nim)
print("Jurusan :", mhs1.jurusan)
print("Rata-rata Nilai :", mhs1.rata_rata_nilai())
