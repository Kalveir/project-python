#usr/env/bin/python3
pilih = 'y'
while pilih=='y':
    print('script menghitung suku dan deret')
    print('silahkan pilih operasi yang digunakan')
    print('1. mencari suku ke-n (Sn)')
    print('2. Mencari nilai beda dan suku pertama')
    print('3. mencari suku tengah')
    print('4. operasi kompleks')
    choice = input('silahkan masukan nomer operasinya : ')
    if choice == '1':
        lagi = 'y'
        while lagi=='y':
            suku1 = input('masukan suku pertama : ')
            beda = input('masukan nilai beda : ')
            SukuNilai = input('masukan suku yang akan dicari : ')
            selisih = int(SukuNilai) - (1)
            beda2 = int(selisih) * int(beda)
            hasil = int(suku1) + int(beda2)
            print('hasilnya adalah' ,hasil)
            lagi = input('ingin menghitung kembali..? [y/n]' )
    elif choice == '2':
        lagi = 'y'
        while lagi=='y':
            Sb = input('suku terbesar ke-')
            Nb = input('Nilainya adalah : ')
            Sk = input('suku terkecil ke-')
            Nk = input('Nilainya adalah :')
            if int(Sb) > int(Sk) and int(Nb) > int(Nk):
                #menentukan nilai bedanya
                Ssn = (int(Sb) - (1)) - (int(Sk) - (1))
                Nn = int(Nb) - int(Nk)
                beda = int(Nn) // int(Ssn)
                print('berarti bedanya adalah : ' ,beda)
                #menentukan suku pertama
                sukup = int(Nk) - (int(Sk) - (1)) * int(beda)
                print('jadi suku pertamanya adalah' ,sukup)
                lagi = input('ingin menghitung kembali..? [y/n]' )
            else :
                print('maaf suku/nilai yang terbesar lebih kecil dari suku/nilai yang terkecil')
    elif choice == '3':
        lagi = 'y'
        while lagi=='y':
            Suku1 = input('masukan suku pertama : ')
            Beda = input('masukan nilai bedanya :')
            Sn = input('masukan jumlah sukunya : ')
            St = int(Suku1) + int(Beda) // (2) * (int(Sn) - (1))
            print('Jadi suku tengah dari adalah' ,St)
            lagi = input('ingin menghitung kembali...? [y/n] ')
    elif choice == '4':
        lagi = 'y'
        while lagi=='y':
            Suku_Besar = input('masukan suku yang terbesar ke-')
            Nilai_Besar = input('masukan nilai sukunya : ')
            Suku_Kecil = input('masukan suku yang terkecil ke-')
            Nilai_Kecil = input('masukan nilai sukunya : ')
            Suku_dicari = input('Mencari nilai Suku ke-')
            if int(Suku_Besar) and int(Nilai_Besar) > int(Suku_Kecil) and int(Nilai_Kecil):
                beda = (int(Nilai_Besar) - int(Nilai_Kecil)) // (int(Suku_Besar) - int(Suku_Kecil))
                print('Nilai bedanya : ' ,beda)
                suku1 = int(Nilai_Kecil) - (int(Suku_Kecil) - (1)) * int(beda)
                print('Suku pertamanya adalah : ' ,suku1)
                Suku2 = int(suku1) + (int(Suku_dicari) - (1)) * int(beda)
                Suku2 = print('jadi nilai sukunya adalah' ,Suku2)
                lagi = input('ingin menghitung kembali...? [y/n] ')
            else :
                print('maaf suku/nilai yang terbesar lebih kecil dari suku/nilai yang terkecil')
    else :
        print('operator salah')       
    pilih = input('atau menggunakan operasi lain..? [y/n]')
print('god bye motherfucker')
