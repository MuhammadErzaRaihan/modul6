def hitung(ruangan, jumlah_zetsu):
    hasil = [zetsu * (i + 1) for i, zetsu in enumerate(jumlah_zetsu)]
    return hasil

def main():
    ruangan = int(input())
    jumlah_zetsu = list(map(int, input().split()))

    if len(jumlah_zetsu) != ruangan:
        print("error!")
        return

    tiap_ruangan = hitung(ruangan, jumlah_zetsu)

    for jumlah in tiap_ruangan:
        print(jumlah, end=" ")

if __name__ == "__main__":
    main()
