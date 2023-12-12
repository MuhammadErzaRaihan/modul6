#include <stdio.h>
#include <string.h>

int main(){
    char asli[100];
    char palsu[100];
    scanf("%[^\n]%*c", &asli);
    scanf("%[^\n]%*c", &palsu);
    int kode,pesan,a,b=0,c=0;
    kode=strlen(asli);
    pesan=strlen(palsu);
    if(kode !=pesan){
        printf("\nPanjang kalimat berbeda, pesan palsu");}
    else{
        for(a=0; a<kode; a++){
            if(asli[a]==palsu[a]){
                if (asli[a] == ' '){
                    printf(" ");}
                else {
                    printf("*");
                    b++;}
                }
            else{
                printf("#");
                c++;}
        }
    printf("\n* = %d",b);
    printf("\n# = %d",c);
    if(b >= c){
        printf("\nPesan Asli");}
    else{
        printf("\nPesan Palsu");}
    return 0;
    }
}