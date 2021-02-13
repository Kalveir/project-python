import calendar
tahun = int(input('masukan tahun : '))
if int(tahun) % 100== 0:
    if int(tahun) % 400== 0:
        print(tahun, 'adalah tahun kabisat')
    else:
        print(tahun, 'bukan tahun kabisat')
elif int(tahun) % 4== 0:
    print(tahun, 'adalah tahun kabisat')
else:
    print(tahun, 'bukan tahun kabisat')
print('')
print(calendar.month(int(tahun), 2))



