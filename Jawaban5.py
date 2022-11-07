nama = input ('NIM: ')
NIM = input ('Nama: ')

def Capuccino ():
    a = int(input ('Masukkan Harga: '))
    b = 0.1*a
    c = a + b
    print (c)

def Teh ():
    a = int (input('angka 1: '))
    b = 0.1*a
    c = a + b
    print (c)

def pilihan ():
    print ('1. Capuccino')
    print ('2. Teh')
    print ('exit')

while True:
    pilihan ()
    pil = int (input('pilihan: '))
    if pil==1:
        Capuccino ()
    elif pil==2:
        Teh ()
    else:
        break
