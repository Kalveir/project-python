#usr/bin/env/python3
angka = int(input('masukan angkanya :'))
if int(angka) > 1:
    for ulang in range(2 ,angka):
        if (angka % ulang)== 0:
            print(angka, 'bukan bilangan prima')
            print('karena' ,ulang, 'x' ,angka//ulang, '=' ,angka)
            break
    else:
        print(angka, 'bilangan prima')
else:
    print('maaf angka tidak boleh 1')
