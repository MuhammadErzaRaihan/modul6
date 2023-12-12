row = 2
banyak_row1, banyak_row2 = map(int, input().split())

if banyak_row1 == banyak_row2:
    elemen = [[0] * banyak_row2 for _ in range(row)]

    for i in range(row):
        input_elemen = input().split()
        for j in range(banyak_row1):
            elemen[i][j] = int(input_elemen[j])

    for i in range(row - 1):
        for j in range(banyak_row1):
            if i + 1 < row:
                elemen[i][j] *= elemen[i + 1][j]

    for i in range(row - 1):
        for j in range(banyak_row1):
            print(elemen[i][j], end=" ")
else:
    print("Jumlah tidak sama")
