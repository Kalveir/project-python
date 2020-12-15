#usr/bin/env/python3
print('hello world')
print('ini adalah prog12ram untuk menghitung suhu')
print('ini percobaan')

def Celcius_Reamur(Celcius):
	Celre = (int(Celcius) / (5)) * int(4)
	return Celre
def Reamur_Celcius(Reamur): 
	Remcel = (int(Reamur) / (4)) * int(5)
	return Remcel
def Celcius_Farenheit(Celcius):
	Celfar = (int(Celcius) / (5)) * int(9) + int(32)
	return Celfar
def Reamur_Farenheit(Reamur):
	Reamfar = (int(Reamur) / (4)) * int(9) + int(32)
	return Reamfar
def Farenheit_Celcius(Farenheit):
        Farcel = (int(Farenheit) / (9)) * int(5) - int(32)
        return Farcel
def Farenheit_Reamur(Farenheit):
        Farem = (int(Farenheit) / (9)) * int(5) - int(32)
        return Farem
def Celcius_Kelvin(Celcius):
        Celkel = int(Celcius) + int(273)
        return Celkel
def Reamur_Kelvin(Reamur):
        Remkel = (int(Reamur) / (4)) * int(5) + int(273)
        return Remkel
def Kelvin_Celcius(Kelvin):
        Kevcel = int(Kelvin) - int(273)
        return Kevcel
def Kelvin_Reamur(Kelvin):
    	Kelre = (int(Kelvin) / (4)) * int(5) - int(273)
    	return Kelre
print('silahkan pilih konverensi suhunya')
print('1. Celcius -----------------> Reamur')
print('2. Reamur ------------------> Celcius')
print('3. Celcius -----------------> Farenheit')
print('4. Reamur ------------------> Farenheit')
print('5. Farenheit ---------------> Celcius')
print('6. Farenheit ---------------> Reamur')
print('7. Celcius -----------------> Kelvin')
print('8. Reamur ------------------> Kelvin')
print('9. Kelvin ------------------> Celcius')
print('10.Kelvin ------------------> Reamur')

choice = input('silahkan pilih nomernya : ')

if choice == '1':
    print('Celcius -----------------> Reamur')
    Celcius = input('masukan besar suhu Celciusnya : ')
    print('hasilnya adalah : ',Celcius_Reamur(Celcius))

elif choice == '2':
    print('Reamur ------------------> Celcius')
    Reamur = input('masukan besar suhu Reamurnya : ')
    print('hasilnya adalah : ',Reamur_Celcius(Reamur))

elif choice == '3':
    print('Celcius -----------------> Farenheit')
    Celcius = input('masukan besar Celciusnya : ')
    print('hasilnya adalah : ',Celcius_Farenheit(Celcius))

elif choice == '4':
    print('Reamur ------------------> Farenheit')
    Reamur = input('masukan besar suhu Reamurnya : ')
    print('hasilnya adalah : ',Reamur_Farenheit(Reamur))

elif choice == '5':
    print('Farenheit ---------------> Celcius')
    Farenheit = input('masukan besar suhu Farenheitnya : ')
    print('hasilnya adalah : ',Farenheit_Celcius(Farenheit))

elif choice == '6':
    print('Farenheit ---------------> Reamur')
    Farenheit = input('masukan besar suhu Farenheitnya : ')
    print('hasilnya adalah : ',Farenheit_Reamur(Farenheit))

elif choice == '7':
    print('Celcius -----------------> Kelvin')
    Celcius = input('masukan besar suhu Celciusnya : ')
    print('hasilnya adalah : ',Celcius_Kelvin(Celcius))

elif choice == '8':
    print('Reamur ------------------> Kelvin')
    Reamur = input('masukan besar suhu Reamurnya : ')
    print('hasilnya adalah : ',Reamur_Kelvin(Reamur))

elif choice == '9':
    print('Kelvin ------------------> Celcius')
    Kelvin = input('masukan besar suhu Kelvinnya : ')
    print('hasilnya adalah : ',Kelvin_Celcius(Kelvin))

elif choice == '10':
    print('10.Kelvin ------------------> Reamur')
    Kelvin = input('masukan besar suhu Kelvinnya : ')
    print('hasilnya adalah : ',Kelvin_Reamur(Kelvin))

else :
    print('inputan salah')
