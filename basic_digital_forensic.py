import os
import re
from datetime import datetime

def cari_pola_log(file_path, pola):
    """Cari dan tampilkan baris yang cocok dengan pola regex dari file log."""
    laporan = []
    pattern = re.compile(pola)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, start=1):
                if pattern.search(line):
                    laporan.append(f"[Baris {line_number}] {line.strip()}")
        if laporan:
            print(f"=== Temuan pola '{pola}' di file {file_path} ===")
            for item in laporan:
                print(item)
        else:
            print(f"Tidak ditemukan baris dengan pola '{pola}' di file {file_path}.")
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")
    return laporan

def cari_file_tersembunyi(directory):
    """Cari file tersembunyi (dimulai dengan titik) di direktori."""
    hasil = []
    try:
        for root, dirs, files in os.walk(directory):
            for name in files:
                if name.startswith('.'):
                    path = os.path.join(root, name)
                    hasil.append(path)
        if hasil:
            print(f"\n=== File tersembunyi ditemukan di direktori {directory} ===")
            for file in hasil:
                print(file)
        else:
            print(f"Tidak ditemukan file tersembunyi di direktori {directory}.")
    except Exception as e:
        print(f"Error saat mencari file tersembunyi: {e}")
    return hasil

def tampilkan_metadata_file(file_path):
    """Tampilkan metadata lengkap dari file."""
    try:
        stat = os.stat(file_path)
        size = stat.st_size
        mod_time = datetime.fromtimestamp(stat.st_mtime)
        access_time = datetime.fromtimestamp(stat.st_atime)
        create_time = datetime.fromtimestamp(stat.st_ctime)
        metadata = (
            f"Metadata file: {file_path}\n"
            f"  Ukuran file       : {size} bytes\n"
            f"  Terakhir dimodifikasi: {mod_time}\n"
            f"  Terakhir diakses  : {access_time}\n"
            f"  Waktu pembuatan   : {create_time}\n"
        )
        print("\n=== Informasi Metadata File ===")
        print(metadata)
        return metadata
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")
        return None

def simpan_laporan(filename, content):
    """Simpan laporan analisis ke file teks."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Laporan disimpan ke file: {filename}")

if __name__ == "__main__":
    # Tentukan file dan pola untuk dicari
    path_log = 'auth.log'  # ganti dengan file log yang Anda punya
    pola_gagal_login = r'Failed password'

    # Analisis file log
    laporan_log = cari_pola_log(path_log, pola_gagal_login)

    # Cari file tersembunyi di direktori saat ini
    file_tersembunyi = cari_file_tersembunyi('.')

    # Ambil metadata file log
    metadata_log = tampilkan_metadata_file(path_log)

    # Gabungkan hasil laporan semua analisis
    isi_laporan = "\n".join(laporan_log) + "\n\n" + "File tersembunyi:\n" + "\n".join(file_tersembunyi) + "\n\n" + (metadata_log or "")

    # Simpan laporan ke file
    simpan_laporan("laporan_forensik.txt", isi_laporan)
