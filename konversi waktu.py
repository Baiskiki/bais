detik = int(input("masukan jumlah detik yang ingin di hitung : "))

jam         = detik // 3600;
sisa_detik  = detik  % 3600;
menit       = sisa_detik // 60;
detik       = sisa_detik % 60;

print(detik," detik = ",jam," jam, ",menit," menit, ",detik," detik")


 