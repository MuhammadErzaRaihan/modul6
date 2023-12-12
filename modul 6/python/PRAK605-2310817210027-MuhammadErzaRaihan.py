def ops(n, A, B):
    perkalian = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                perkalian[i][j] += A[i][k] * B[k][j]
    
    return perkalian

n = int(input())
print("Matriks A")
A = [[int(x) for x in input().split()] for i in range(n)]
print("Matriks B")
B = [[int(x) for x in input().split()] for i in range(n)]

perkalian = ops(n, A, B)
print("Matriks AXB")
for baris in perkalian:
    print(baris)