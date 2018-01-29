#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int main() {
    long n = 600851475143;
    long res = 1;
    //int n = 13195;

    for (int p = 2; p < n/2; ++p) {
        bool isPrime = true;

        for (int i = 3; i < sqrt(p); ++i)
            if (p % i == 0) {
                isPrime = false;
                break;
            }

        if (isPrime)
            if (n % p == 0) {
                res *= p;
                printf("%d\n", p);
            }

        if (res == n)
            break;
    }
}
