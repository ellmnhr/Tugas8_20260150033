# 1. Variabel konstanta bertipe Tuple
LOKASI = ("Kampung Anggur Plumbungan", -7.828, 110.378)
AMBANG_KRITIS = (35.0, 40.0) #(Suhu Max 35.0 C, Kelembaban Min 40.0%)

def hitung_tren(data_slice):
    """
    Menerima list berisi tuple (suhu, kelembaban) yang sudah di-slice.
    Mengembalikan rata-ata suhu dan rata-rata kelembaban dari data tersebut.
    """
    if not data_slice:
        return 0.0, 0.0

    total_suhu = 0.0
    total_lembab = 0.0
    jumlah_data = len(data_slice)

    #Looping untuk menjumlahkan nilai dari tuple dalam list
    for suhu, lembab in data_slice:
        total_suhu += suhu
        total_lembab += lembab

    rata_suhu = total_suhu / jumlah_data
    rata_lembab = total_lembab / jumlah_data

    return rata_suhu, rata_lembab

def evaluasi_irigasi(rata_suhu, rata_lembab, tuple_kritis):
    """
    Mengevaluasi kelayakan irigasi berdasarkan rata-rata suhu & kelembaban
    dibandingkan dengan ambang batas kritis.
    """
    suhu_max = tuple_kritis[0]
    lembab_min = tuple_kritis[1]

    #Logika evaluasi: jika suhu > max ATAU kelembaban < min
    if rata_suhu > suhu_max or rata_lembab < lembab_min:
        return "KRITIS: Nyalakan Pompa Irigasi!"
    else:
        return "NORMAL: Pompa Mati."