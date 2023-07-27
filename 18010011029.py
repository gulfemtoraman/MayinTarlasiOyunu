#Gülfem TORAMAN
#18010011029

from random import shuffle

while True:

    boyut = int(input("istediginiz boyut: "))
    ekran = []
    ekran2 = []
    gizli_ekran = []

    for i in range(boyut):
        ekran.append(["?"] * boyut)

    mayin = int((boyut / 100) * 30)

    for i in range(mayin):
        ekran.pop()

    for i in range(mayin):
        ekran.append(["X"] * boyut)

    for i in range(boyut):
        ekran2 += ekran[i]

    shuffle(ekran2)
    ekran.clear()

    for i in range(boyut):
        ekran.append(ekran2[i:boyut + i])

    mod = int(input("1-GIZLI MOD\n2-ACIK MOD\nsecmek istediginiz mod: "))

    if mod == 1:
        for i in range(boyut):
            gizli_ekran.append(["?"] * boyut)

        for satir in gizli_ekran:
            for sutun in satir:
                print(sutun, sep="\t", end=" ")
            print("\n")

    if mod == 2:
        for satir in ekran:
            for sutun in satir:
                print(sutun, sep="\t", end=" ")
            print("\n")

    puan = 0

    for puan in range(boyut ** 2):
        adet_mayin = 0
        secilen_satir = int(input("satir: "))
        secilen_sutun = int(input("sutun: "))

        if ekran[secilen_satir - 1][secilen_sutun - 1] == 'X':
            for satir in ekran:
                for sutun in satir:
                    print(sutun, sep="\t", end=" ")
                print("\n")
            print("...MAALESEF KAYBETTİNİZ...\npuaniniz=", puan)
            break

        elif ekran[secilen_satir - 1][secilen_sutun - 1] == '?':

            ekran[secilen_satir - 1][secilen_sutun - 1] = '0'

            if mod == 1:
                for satir in gizli_ekran:
                    for sutun in satir:
                        print(sutun, sep="\t", end=" ")
                    print("\n")

            else:
                for satir in ekran:
                    for sutun in satir:
                        print(sutun, sep="\t", end=" ")
                    print("\n")

            if ekran[secilen_satir - 2][secilen_sutun - 2] == 'X':
                adet_mayin += 1
            if ekran[secilen_satir - 2][secilen_sutun - 1] == 'X':
                adet_mayin += 1
            if ekran[secilen_satir - 2][secilen_sutun] == 'X':
                adet_mayin += 1
            if ekran[secilen_satir - 1][secilen_sutun - 2] == 'X':
                adet_mayin += 1
            if ekran[secilen_satir - 1][secilen_sutun] == 'X':
                adet_mayin += 1
            if ekran[secilen_satir][secilen_sutun - 2] == 'X':
                adet_mayin += 1
            if ekran[secilen_satir][secilen_sutun - 1] == 'X':
                adet_mayin += 1
            if ekran[secilen_satir][secilen_sutun] == 'X':
                adet_mayin += 1

            print("cevredeki mayin sayisi=", adet_mayin)

            puan += 1

    if puan == boyut ** 2:
        print("...OYUNU KAZANDINIZ...\npuaniniz=", puan)

    islem = int(input("1-YENI OYUN\n2-CIKIS\nyapmak istediginiz islem: "))

    if islem == 1:
        pass
    elif islem == 2:
        exit(0)
    else:
        print("sectiginiz islem bulunamadi...")
