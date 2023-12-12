asli = input()
palsu = input()

kode = len(asli)
pesan = len(palsu)

a = 0
b = 0
c = 0

if kode != pesan:
    print("\nPanjang kalimat berbeda, pesan palsu")
else:
    for a in range(kode):
        if asli[a] == palsu[a]:
            if asli[a] == ' ':
                print(" ", end='')
            else:
                print("*", end='')
                b += 1
        else:
            print("#", end='')
            c += 1

    print("\n* = {}".format(b))
    print("# = {}".format(c))

    if b >= c:
        print("Pesan Asli")
    else:
        print("Pesan Palsu")
