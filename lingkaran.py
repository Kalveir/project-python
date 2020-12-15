#usr/bin/env/python3
jari = int(input('masukan panjang jarinya : '))
if int(jari) >= 7:
        if (jari % 7)== 0:
            LR = (int(jari) // (7)) * int(jari)
            Lr2 = float(LR) * (22)
            print('jadi luas lingkaran tersebut : ' ,Lr2)
        else:
            LRT = (3.14) * int(jari) * int(jari)
            print(' jadi luas lingkaran tersebut : ' ,LRT)
else:
    print('maaf bilangan terkecil jari-jari lingkaran hanyalah 7')
