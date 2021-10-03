"""
The MIT License (MIT)

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
#usr/env/bin/python3
import os
ls_barang = []
ls_jumlah = []
ls_harga = []
ls_hasil = []

class toko:
    def __init__(self, barang, jumlah, harga, hasil) :
        self.barang = barang
        ls_barang.append(barang)
        self.jumlah = jumlah
        ls_jumlah.append(jumlah)
        self.harga = harga
        ls_harga.append(harga)
        self.hasil = hasil
        ls_hasil.append(hasil)
    def pembayaran(self) :
        os.system('clear')
        n = 0
        print("List Total harga barang")
        for i in range(x) :
            n+=1
            print("-"*32)
            print(n,"." ,ls_barang[i], "=", ls_jumlah[i], "*", ls_harga[i],"=",  ls_hasil[i])
             

x = 0
ya = "y"
while ya == "y":
    in_barang = input("masukan nama barang : ")
    in_jumlah = int(input("masukan jumlah barang : "))
    in_harga = int(input("masukan harga barangnya : "))
    in_hasil = (in_jumlah) * (in_harga)
    pembeli = toko(in_barang, in_jumlah, in_harga, in_hasil)
    x+=1
    ya = input("ingin menambahkan barang lagi..?[y/n] ")
pembeli.pembayaran()
print("-"*32)
print("total harga : ", sum(ls_hasil))        