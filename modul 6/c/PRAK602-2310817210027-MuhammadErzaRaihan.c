#include <stdio.h>

void hitung(int ruangan, int jumlah_zetsu[]) {
    int hasil[ruangan];
    for (int i = 0; i < ruangan; i++) {
        hasil[i] = jumlah_zetsu[i] * (i + 1);
    }

    for (int i = 0; i < ruangan; i++) {
        printf("%d ", hasil[i]);
    }
}

int main() {
    int ruangan;
    scanf("%d", &ruangan);

    int jumlah_zetsu[ruangan];
    for (int i = 0; i < ruangan; i++) {
        scanf("%d", &jumlah_zetsu[i]);
    }

    if (ruangan != sizeof(jumlah_zetsu) / sizeof(jumlah_zetsu[0])) {
        printf("error!\n");
        return 1;
    }

    hitung(ruangan, jumlah_zetsu);

    return 0;
}
