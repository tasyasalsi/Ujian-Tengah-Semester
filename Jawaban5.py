NIM = input ('NIM: ')
nama = input ('Nama: ')

def Capuccino ():
    a = int(input ('Masukkan Harga: '))
    b = 0.1*a
    c = a + b
    print ('Jumlah yang harus dibayar: ', c)

def Teh ():
    a = int (input('angka 1: '))
    b = 0.1*a
    c = a + b
    print ('Jumlah yang harus dibayar: ', c)

def pilihan ():
    print ('1. Capuccino')
    print ('2. Teh')
    print ('exit')

def data ():
    print ('NIM: ', NIM)
    print ('Nama: ', nama)

while True:
    data ()
    pilihan ()
    pil = int (input('pilihan: '))
    if pil==1:
        Capuccino ()
    elif pil==2:
        Teh ()
    else:
        break
