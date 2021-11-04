import os
import sys


class rumus(int):
    def tambah(a, b):
        return a + b

    def kurang(a, b):
        return a - b

    def kali(a, b):
        return a * b

    def bagi(a, b):
        return a / b

    def kuadrat(a, b):
        return a ^ 2

    def kubik(a, b):
        return a ^ 3


class main:
    print("""CalCli
[ Calculator Command Line Interface ]
1. Pertambah
2. Pengurangan
3. Perkalian
4. Pembagian
5. Pankat 2
6. Pangkat 3""")

    x = input("Pilih Menu (1-6) : ")
    a = input("\nNilai 1 : ")
    b = input("NIlai 2 : ")
    if x == 1:
        print("Hasil = ", rumus.tambah(a,b))
    elif x == 2:
        print("Hasil = ", rumus.kurang(a,b))
    elif x == 3:
        print("Hasil = ", rumus.kali(a,b))
    elif x == 4:
        print("Hasil = ", rumus.bagi(a,b))
    elif x == 5:
        print("Hasil = ", rumus.bagi(a))
    elif x == 6:
        print("Hasil = ", rumus.bagi(a))
    else:
        print("Syntax Error")


answer = str(input('Run again? (y/n): '))

if answer == 'n':
     quit()
elif answer == 'y':
    os.execl(sys.executable, sys.executable, *sys.argv)
else:
    print
    'Invalid input.'
