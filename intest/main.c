#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

int main() {
    int size = 1024 * 1024 * 4;
    char *buf = malloc(size);
    setvbuf(stdin, buf, _IOFBF, size);

    int n, k;
    fscanf(stdin, "%d %d\n", &n, &k);

    int res = 0;

    for (int i = 0; i < n; ++i) {
        char buf[15] = {0};
        fgets_unlocked(buf, 15, stdin);
        int x = atoi(buf);

        if (x % k == 0)
            ++res;
    }

    printf("%d\n", res);
}
