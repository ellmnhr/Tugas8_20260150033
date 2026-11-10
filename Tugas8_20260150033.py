import modul_sensor

#1. Struktur Data Utama: List kosong untuk menyimpan log sensor (suhu, kelembaban)
log_kebun = []

def input_sensor():
    """
    Fungsi validasi input menggunakan try-except dan while True agar tidak crash saat
    input huruf dan memastikan rentang rasional (0-100).
    """
    print("\n--- Masukkan Data Sensor IoT ---")

    #Validasi Suhu Udara
    while True:
        try:
            suhu = float(input("Masukkan Suhu Udara (C, rentang 0-100): "))
            if 0.0 <= suhu <= 100.0:
                break
            else:
                print("Nilai suhu tidak rasional! Harap masukkan angka antara 0 hingga 100.")
        except ValueError:
            print("Input tidak valid! Harap masukkan angka yang benar.")

    #Validasi Kelembaban Tanah
    while True:
        try:
            lembab = float(input("Masukkan Kelembaban Tanah (%, rantang 0-100): "))
            if 0.0 <= lembab <= 100.0:
                break
            else:
                print("Nilai kelembaban tidak rasional! Harap masukkan angka antara 0 hingga 100.")
        except ValueError:
            print("Input tidak valid! Harap masukkan angka yang benar.")

    #Mengembalikan data dalam bentuk Tuple
    return (suhu, lembab)

#Menampilkan informasi lokasi dari konstanta modul
print("=" * 60)
print(f" SISTEM MONITORING PRESISI IoT - {modul_sensor.LOKASI[0]}")
print(f" Koordinat: Latitude {modul_sensor.LOKASI[1]}, Longtitude {modul_sensor.LOKASI[2]}")
print("=" * 60)

#Pengulangan Menu Utama
while True:
    print("\n--- MENU UTAMA ---")
    print("[1] Rekam Data Sensor")
    print("[2] Analisis Tren (3 Data Terakhir)")
    print("[3] Keluar")

    pilihan = input("Pilih menu (1/2/3): ").strip()

    if pilihan == '1':
        #Panggil fungsi validasi dan simpan tuple ke dalam list log_kebun
        data_baru = input_sensor()
        log_kebun.append(data_baru)
        print(f"Data berhasil direkam! Total data saat ini: {len(log_kebun)}")

    elif pilihan == '2':
        #Periksa apakah data sudah ada
        if len(log_kebun) == 0:
            print("Belum ada data sensor yang direkam. Silakan pilih menu [1] terlebih dahulu.")
            continue

        print("\n--- ANALISIS TREN (3 DATA TERAKHIR) ---")

        #Gunakan Slicing untuk mengambil maksimal 3 data terakhir
        data_terakhir = log_kebun[-3:]

        print("Detail 3 Data Terakhir yang Masuk:")
        for idx, (suhu, lembab) in enumerate(data_terakhir, start=1):
            print(f"  {idx}. Suhu: {suhu}C | Kelembaban: {lembab}%")

        #Panggil fungsi dari modul untuk menghitung rata-rata
        rata_suhu, rata_lembab = modul_sensor.hitung_tren(data_terakhir)

        print(f"\nHasil Perhitungan Rata-rata:")
        print(f"- Rata-rata Suhu    : {rata_suhu:.2f}C")
        print(f"- Rata-rata Lembab  : {rata_lembab:.2f}%")

        #Evaluasi status pompa irigasi
        status_pompa = modul_sensor.evaluasi_irigasi(rata_suhu, rata_lembab, modul_sensor.AMBANG_KRITIS)
        print(f"Status Sistem                 : {status_pompa}")

    elif pilihan == '3':
        print("\nTerima kasih telah mengguna Sistem Monitoring IoT Kampung Plumbungan.")
        print("Keluar dari program...")
        break
    else:
        print("Pilihan tidak valid! Silakan masukkan angka 1, 2, atau 3.")