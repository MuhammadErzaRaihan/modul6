#include <stdio.h>

int main()
{
    int row, banyak_row1, banyak_row2;
    row = 2;
    scanf("%d %d", &banyak_row1, &banyak_row2);
    if (banyak_row1 == banyak_row2)
    {
        int elemen[row][banyak_row2]; 

        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < banyak_row1; j++)
            {
                scanf("%d",&elemen[i][j]);
            }
        }
        for (int i = 0; i < row-1; i++)
        {
            for (int j = 0; j < banyak_row1; j++)
            {
                if (i + 1 < row) {
                    elemen[i][j] = elemen[i][j] * elemen[i + 1][j];
                }
            }
        }  
        for (int i = 0; i < row-1; i++)
        {
            for (int j = 0; j < banyak_row1; j++)
            {
                printf("%d ", elemen[i][j]);
            }
        }
    }   
    else{
    printf("Jumlah tidak sama");
    }
    return 0;
}