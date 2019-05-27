import os, time, array, sys
from fractions import Fraction


def cls():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


def bl():
    try:
        cls()
        menu()
        a=input('Panjang : ')
        a1=str.replace(a, ',', '.')
        b1=float(a1)
        b=input('Lebar : ')
        a2=str.replace(b, ',', '.')
        b2=float(a2)
        c=input('Tinggi : ')
        a3=str.replace(c, ',', '.')
        b3=float(a3)
        hasil=b1 * b2 * b3
        print('Hasil : %g' % hasil)
    except(TypeError, ValueError):
        val()
        bl()
    backmenu()


def kb():
    try:
        cls()
        menu()
        a=input('Sisi : ')
        a1=str.replace(a, ',', '.')
        a2=float(a1)
        hasil=a2 ** 3
        print ('Hasil : %g' % hasil)
    except (TypeError, ValueError):
        val()
        kb()
    backmenu()


def ps():
    try:
        cls()
        menu()
        a=input('Alas Segitiga : ')
        a1=str.replace(a, ',', '.')
        q=float(a1)
        b=input('Tinggi Segitiga : ')
        a2=str.replace(b, ',', '.')
        w=float(a2)
        c=input('Tinggi Prisma : ')
        a3=str.replace(c, ',', '.')
        e=float(a3)
        hasil=((q * w) / 2) * e
        print('Hasil : %g' % hasil)
    except(TypeError, ValueError):
        val()
        ps()
    backmenu()


def ls():
    try:
        cls()
        menu()
        a=input('Alas Segitiga : ')
        a1=str.replace(a, ',', '.')
        q=float(a1)
        b=input('Tinggi Segitiga : ')
        a2=str.replace(b, ',', '.')
        w=float(a2)
        c=input('Tinggi Limas : ')
        a3=str.replace(c, ',', '.')
        e=float(a3)
        hasil=(q * w / 2) * e / 3
        print('Hasil : %g' % hasil)
    except (TypeError, ValueError):
        val()
        ls()
    backmenu()


def l4():
    try:
        cls()
        menu()
        a=input('Panjang Alas : ')
        a1=str.replace(a, ',', '.')
        q=float(a1)
        b=input('Lebar Alas : ')
        a2=str.replace(b, ',', '.')
        w=float(a2)
        c=input('Tinggi Limas : ')
        a3=str.replace(c, ',', '.')
        e=float(a3)
        hasil=q * w * e / 3
        print('Hasil : %g' % hasil)
    except(TypeError, ValueError):
        val()
        l4()
    backmenu()


def tb():
    try:
        cls()
        menu()
        a=input('Jari - jari Lingkaran : ')
        a1=str.replace(a, ',', '.')
        c=float(a1)
        b=input('Tinggi Tabung : ')
        b1=str.replace(b, ',', '.')
        d=float(b1)
        hasil=phi() * c ** 2 * d
        print('Hasil : %g' % hasil)
    except(TypeError, ValueError):
        val()
        tb()
    backmenu()


def bo():
    try:
        cls()
        menu()
        a=input('Jari - jari Bola : ')
        b=str.replace(a, ',', '.')
        c=float(b)
        hasil=phi() * b ** 3 * 4 / 3
        print('Hasil : %g' % hasil)
    except(TypeError, ValueError):
        val()
        bo()
    backmenu()


def kr():
    try:
        cls()
        menu()
        a=input('Jari - jari Lingkaran : ')
        a1=str.replace(a, ',', '.')
        a2=float(a1)
        b=input('Tinggi Kerucut : ')
        b1=str.replace(b, ',', '.')
        b2=float(b1)
        hasil=(phi() * a2 ** 2) * b2 / 3
        print('Hasil : %g' % hasil)
    except (TypeError, ValueError):
        val()
        kr()
    except (KeyboardInterrupt, KeyError):
        print('Have a Nice Day ~')
        time.sleep(1)
        os._exit(1)


def angka():
    try:
        cls()
        menu()
        a1=input('Masukkan Bilangan Pertama : ')
        a=str.replace(a1, ',', '.')
        x=float(a)
        a2=input('Masukkan Bilangan Kedua : ')
        b=str.replace(a2, ',', '.')
        y=float(b)
    except (TypeError, ValueError):
        val()
        angka()
    try:
        opr=input('+ , - , * , / : ')
        if (opr == '+'):
            hasil=(x + y)
        elif (opr == '-'):
            hasil=(x - y)
        elif (opr == '*'):
            hasil=(x * y)
        elif (opr == '/'):
            try:
                hasil=(x / y)
            except ZeroDivisionError:
                print('Tidak bisa Dibagi 0')
                time.sleep(1)
                angka()
        else:
            print('Pilih operasi dengan benar')
            time.sleep(1)
            angka()
        print('Hasil : %g' % hasil)
        backmenu()
    except (KeyboardInterrupt, KeyError):
        print('Have a Nice Day ~')
        time.sleep(1)
        os._exit(1)


def val():
    print('Angka tidak Valid')
    time.sleep(1)


def pp():
    try:
        cls()
        menu()
        a=input('Panjang : ')
        c=str.replace(a, ',', '.')
        g=float(c)
        b=input('Lebar : ')
        d=str.replace(b, ',', '.')
        h=float(d)
        hasil=g * h
        print('Hasil : %g' % hasil)
    except (TypeError, ValueError):
        val()
        pp()
    backmenu()


def ps():
    try:
        cls()
        menu()
        a1=input('Sisi : ')
        b1=str.replace(a1, ',', '.')
        a=float(b1)
        hasil=a ** 2
        print('Hasil : %g' % hasil)
    except (TypeError, ValueError):
        val()
        ps()
    backmenu()


def s3():
    try:
        cls()
        menu()
        a=input('Alas : ')
        c=str.replace(a, ',', '.')
        g=float(c)
        b=input('Tinggi : ')
        d=str.replace(b, ',', '.')
        h=float(d)
        hasil=g * h / 2
        print('Hasil : %g' % hasil)
    except (TypeError, ValueError):
        val()
        s3()
    backmenu()


def jg():
    try:
        cls()
        menu()
        a=input('Alas : ')
        c=str.replace(a, ',', '.')
        g=float(c)
        b=input('Tinggi : ')
        d=str.replace(b, ',', '.')
        h=float(d)
        hasil=g * h
        print('Hasil : %g' % hasil)
    except (TypeError, ValueError):
        val()
        jg()
    backmenu()


def tr():
    try:
        cls()
        menu()
        a=input('Sisi Atas  : ')
        c=str.replace(a, ',', '.')
        g=float(c)
        b=input('Sisi Bawah : ')
        d=str.replace(b, ',', '.')
        h=float(d)
        e=input('Tinggi     : ')
        f=str.replace(e, ',', '.')
        i=float(f)
        hasil=(g + h) * i / 2
        print('Hasil : %g' % hasil)
    except (TypeError, ValueError):
        val()
        tr()
    backmenu()


def ll():
    try:
        cls()
        menu()
        a=input('Diagonal Pertama : ')
        a1=str.replace(a, ',', '.')
        q=float(a1)
        b=input('Diagonal Kedua : ')
        a2=str.replace(b, ',', '.')
        w=float(a2)
        hasil=(q * w) / 2
        print('Hasil : %g' % hasil)
    except (TypeError, ValueError):
        val()
        ll()
    backmenu()


def l():
    try:
        cls()
        menu()
        a=input('Jari - jari : ')
        a1=str.replace(a, ',', '.')
        b=float(a1)
        hasil=phi() * b ** 2
        print('Hasil : %g' % hasil)
    except TypeError:
        val()
        l()
    backmenu()


def backmenu():
    time.sleep(1)
    q=input('Ingin Menghitung Kembali ( y / n ) : ')
    if (q.lower() == 'y'):
        cls()
        menu()
        home()
    elif (q.lower() == 'n'):
        print('Have a Nice Day ~')
        time.sleep(0.5)
        cls()
        os._exit(1)
    else:
        print('Pilihan Anda tidak Valid')
    backmenu()


def phi():
    return 22 / 7


def luas():
    print('\n1. Persegi Panjang \n2. Persegi \n3. Segitiga \n4. Jajar Genjang'
          '\n5. Trapesium \n6. Layang - Layang atau Belah Ketupat \n7. Lingkaran')
    q=input('Pilih Salah Satu Angka : ')
    if (q == '1'):
        pp()
    elif (q == '2'):
        ps()
    elif (q == '3'):
        s3()
    elif (q == '4'):
        jg()
    elif (q == '5'):
        tr()
    elif (q == '6'):
        ll()
    elif (q == '7'):
        l()
    else:
        val()
        luas()


def volume():
    print('1. Balok \n2. Kubus \n3. Prisma Segitiga \n4. Limas Segitiga'
          '\n5. Limas Segiempat \n6. Tabung \n7. Bola \n8. Kerucut')
    q=input('Pilih Salah satu angka : ')
    if (q == '1'):
        bl()
    elif (q == '2'):
        kb()
    elif (q == '3'):
        ps()
    elif (q == '4'):
        ls()
    elif (q == '5'):
        l4()
    elif (q == '6'):
        tb()
    elif (q == '7'):
        bo()
    elif (q == '8'):
        kr()
    else:
        val()
        volume()


def pec():
    cls()
    menu()
    print('Format Bilangan  =  A/B >> 1/2')
    print('----------------------------')
    try:
        a=input('Bilangan Pertama : ')
        A=Fraction(a)
        b=input('Bilangan Kedua   : ')
        B=Fraction(b)
        c=input('+ , - , * , / : ')
        if (c == '+'):
            print('Hasil : ', A + B)
        elif (c == '-'):
            print('Hasil : ', A - B)
        elif (c == '*'):
            print('Hasil : ', A * B)
        elif (c == '/'):
            print('Hasil : ', A / B)
        else:
            print('Operator tidak Valid')
            time.sleep(1)
            pec()
    except(ValueError, TypeError):
        val()
        pec()
    except ZeroDivisionError:
        print('Tidak Bisa Dibagi Nol')
        time.sleep(1)
        pec()
    backmenu()


def menu():
    print('   ___|         |      ')
    print('  |       _` |  |   __|')
    print('  |      (   |  |  (   ')
    print(' \____| \__,_| _| \___|')
    print(time.strftime('%a, %d-%m-%Y %H:%M', time.localtime(time.time())))
    print('-------------------------')


def konv():
    cls()
    menu()
    print('1. Desimal')
    print('2. Biner')
    print('3. Oktal')
    print('4. Heksadesimal')
    a=input('Pilih Dengan Angka : ')
    if a == '1':
        try:
            aa=int(input('Angka : '))
            a1=bin(aa)
            a2=str.replace(a1, '0b', '')
            b1=oct(aa)
            b2=str.replace(b1, '0o', '')
            c1=hex(aa)
            c2=str.replace(c1, '0x', '')
            print('Biner        : ', a2)
            print('Oktal        : ', b2)
            print('Heksadesimal : ', c2)
            backmenu()
        except (ValueError, TypeError):
            val()
            konv()
    elif a == '2':
        try:
            aa=input('Angka : ')
            bb=int('0b' + aa, 2)
            c1=oct(bb)
            c2=hex(bb)
            d1=str.replace(c1, '0o', '')
            d2=str.replace(c2, '0x', '')
            print('Desimal      : ', bb)
            print('Oktal        : ', d1)
            print('Heksadesimal : ', d2)
            time.sleep(1)
            backmenu()
        except (ValueError, TypeError):
            val()
            konv()
    elif a == '3':
        try:
            aa=input('Angka : ')
            bb=int('0o' + aa, 8)
            c1=bin(bb)
            c2=hex(bb)
            d1=str.replace(c1, '0b', '')
            d2=str.replace(c2, '0x', '')
            print('Desimal      : ', bb)
            print('Biner        : ', d1)
            print('Heksadesimal : ', d2)
            time.sleep(1)
            backmenu()
        except (ValueError, TypeError):
            val()
            konv()
    elif (a == '4'):
        try:
            aa=input('Angka : ')
            b=int('0x' + aa, 16)
            c1=bin(b)
            c2=oct(b)
            d1=str.replace(c1, '0o', '')
            d2=str.replace(c2, '0x', '')
            print('Desimal      : ', b)
            print('Biner        : ', d1)
            print('Oktal        : ', d2)
            time.sleep(1)
            backmenu()
        except (ValueError, TypeError):
            val()
            konv()


def home():
    print('1. Menghitung Angka ( Bulat & Desimal )')
    print('2. Menghitung Angka ( Pecahan )')
    print('3. Bangun Datar')
    print('4. Bangun Ruang')
    print('5. Konversi (Desimal, Biner, Oktal, Heksadesimal)')
    print('6. Menghitung Rata - rata')
    print('0. Keluar')
    a=input('Pilih Salah satu Angka : ')
    if (a == '1'):
        angka()
    elif (a == '2'):
        pec()
    elif (a == '3'):
        luas()
    elif (a == '4'):
        volume()
    elif (a == '5'):
        konv()
    elif (a == '6'):
        rata()
    elif (a == '0'):
        print("Sampai Jumpa ~")
        time.sleep(3)
        os._exit(0)
    else:
        val()
        home()


def rata():
    try:
        cls()
        menu()
        a=int(input('Masukkan Banyak Data :'))
        q=1
        b=array.array('f', [])
        while q <= a:
            try:
                x=input("Data :")
                x1=str.replace(x, ',', '.')
                x2=float(x1)
                q+=1
                b.extend([x2])
            except (ValueError, TypeError):
                val()
                rata()
        print("Hasil : ", sum(b) / a)
        backmenu()
    except(ValueError, TypeError):
        val()
        rata()


menu()
home()
