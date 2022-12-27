#mengitung kecepatan
def hitung_kecepatan():
    print("hitung kecepatan ready!")
    jarak = float(input('masukan jarak: '))
    waktu = float(input('masukan waktu: '))
    kecepatan = jarak  * waktu
    print('kecepatan:', kecepatan, '\n')
#menghitung luas_segitiga
def hitung_luas_segitiga():
    print("hitung luas segitiga ready!")
    alas = float(input('masukan alas: '))
    tinggi = float(input('masukan tinggi: '))
    luas = 0.5 * (alas * tinggi)
    print('luas segitiga adalah :', luas, '\n')
#luas balok
def hitung_luas_balok():
    print("hitung luas balok ready!")
    panjang = float(input('masukan panjang: '))
    lebar = float(input('masukan lebar: '))
    tinggi = float(input('masukan tinggi: '))
    luas = (2*panjang * lebar) + (2*panjang * tinggi) + (2*lebar * tinggi)
    print('luas balok adalah :', luas, '\n')
#luas bola
def hitung_luas_bola():
    print("hitung luas bola ready!")
    r = float(input('masukan jari-jari: '))
    luas = 4 * 3.14 * (r**2)
    print('luas bola adalah :', luas, '\n')

while True:
    userInput = float(input(   
        'pilih rumus yang akan dipakai: \n\n1.hitung kecepatan\n2.luas segitiga\n3. luas_balok\n4.luas_bola\n\npilih nomor berapa: '))
    if(userInput == 1):   
        hitung_kecepatan() 
    elif(userInput == 2):   
        hitung_luas_segitiga() 
    elif(userInput == 3):   
        hitung_luas_balok()
    elif(userInput == 4):   
        hitung_luas_bola() 
    else:
        break

root.mainloop()
