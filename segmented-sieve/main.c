#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

int main() {
    int a = 100;
    int b = 1000;
    int size = (int)ceil(sqrt(b)) - 2;
    int low_primes[size];
    for (int i = 0; i < size; ++i)
        low_primes[i] = i+2;
    for (int i = 0; i < size; ++i) {
        int p = low_primes[i];
        if (p == -1)
            continue;
        for (int j = i+1; j < size; ++j)
            if (low_primes[j] % p == 0)
                low_primes[j] = -1;
    }

    bool high_primes[b - a + 1];
    memset(&high_primes, true, sizeof(high_primes));

    for (int z = 0; z < size; ++z) {
        int p = low_primes[z];
        if (p == -1)
            continue;

        int i = ceil((double)a / p) * p - 1;
        if (a <= p)
            i += p;

        for (int j = i; j < sizeof(high_primes); j += p)
            high_primes[j] = false;
    }
    
    for (int i = 0; i < sizeof(high_primes); ++i)
        if (high_primes[i])
            printf("%d\n", i + a);
}
