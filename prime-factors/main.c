#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

void timespec_diff(struct timespec *start, struct timespec *stop,
                   struct timespec *result)
{
    if ((stop->tv_nsec - start->tv_nsec) < 0) {
        result->tv_sec = stop->tv_sec - start->tv_sec - 1;
        result->tv_nsec = stop->tv_nsec - start->tv_nsec + 1000000000;
    } else {
        result->tv_sec = stop->tv_sec - start->tv_sec;
        result->tv_nsec = stop->tv_nsec - start->tv_nsec;
    }

    return;
}

int main() {
    struct timespec start, end; 
    clock_gettime(CLOCK_MONOTONIC, &start);

    long n = 600851475143;
    //long n = 13195;
    long res = 1;

    if (n % 2 == 0) {
        printf("2\n");
        res *= 2;
    }

    for (int p = 3; p < n/2; p += 2) {
        bool isPrime = true;

        for (int i = 3; i < sqrt(p); i += 22)
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

    clock_gettime(CLOCK_MONOTONIC, &end);

    struct timespec diff;
    timespec_diff(&start, &end, &diff);

    printf("%ld sec, %f msec\n", diff.tv_sec, ((double)diff.tv_nsec)/1000/1000);
}
