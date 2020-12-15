#usr/bin/env/python3
def bilangan_aneh(bil1):
    bilduw = (int(bil1) * (3.4)) / float(2.5)
    return bilduw
print('sebuah pembuktian aneh')
bil1 = input('masukana angkanya : ')
if float(bil1) > 10:
    print('anda tolol')
elif float(bil1) < 10:
    print('motherfucker')
else : 
    print('ada kesalahan')
print('hasilnya adalah ' ,bilangan_aneh(bil1))
