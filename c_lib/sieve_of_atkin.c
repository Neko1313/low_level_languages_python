#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void sieve_of_atkin(int limit, int* primes, int* prime_count) {
    int* sieve = (int*)calloc(limit + 1, sizeof(int));
    
    for (int x = 1; x * x <= limit; x++) {
        for (int y = 1; y * y <= limit; y++) {
            int n;

            // 4x^2 + y^2
            n = 4 * x * x + y * y;
            if (n <= limit && (n % 12 == 1 || n % 12 == 5)) {
                sieve[n] = !sieve[n];
            }

            // 3x^2 + y^2
            n = 3 * x * x + y * y;
            if (n <= limit && n % 12 == 7) {
                sieve[n] = !sieve[n];
            }

            // 3x^2 - y^2
            n = 3 * x * x - y * y;
            if (x > y && n <= limit && n % 12 == 11) {
                sieve[n] = !sieve[n];
            }
        }
    }

    for (int r = 5; r * r <= limit; r++) {
        if (sieve[r]) {
            for (int k = r * r; k <= limit; k += r * r) {
                sieve[k] = 0;
            }
        }
    }

    *prime_count = 0;
    if (limit > 2) {
        primes[*prime_count] = 2;
        (*prime_count)++;
    }
    if (limit > 3) {
        primes[*prime_count] = 3;
        (*prime_count)++;
    }
    for (int n = 5; n <= limit; n++) {
        if (sieve[n]) {
            primes[*prime_count] = n;
            (*prime_count)++;
        }
    }

    free(sieve);
}
