def main():
    baris, kolom = map(int, input().split())
    matriks = [[0]*kolom for _ in range(baris)]
    
    elemen = list(map(int, input().split()))
    
    index = 0
    for a in range(baris):
        for b in range(kolom):
            matriks[a][b] = elemen[index]
            index += 1
    
    for a in range(baris):
        for b in range(kolom):
            print(matriks[a][b], end=' ')
        print()
main()