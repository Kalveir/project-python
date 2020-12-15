#usr/bin/env/python3
nomor = int(input('masukan bilangannya :'))
if int(nomor) > 1:
    for i in range(2 ,nomor):
        if (nomor % i)== 0:
            print(nomor, 'bukan bilangan prima')
            break
    else:
        print(nomor, 'bilangan prima')