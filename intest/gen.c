#include <stdio.h>
#include <stdlib.h>
#include <time.h> 

int main() {
    srand(time(NULL));
    FILE *f = fopen("input", "w+");
    int n = 10000000;
    int k = 7;

    fprintf(f, "%d %d\n", n, k);

    for (int i = 0; i < n; ++i) {
        if (i % 1000000 == 0)
            printf("%d\n", i);
        fprintf(f, "%d\n", rand());
    }

    fflush(f);
    fclose(f);
}
