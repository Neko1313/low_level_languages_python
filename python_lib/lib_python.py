import numpy as np
import math

from src import measure_performance

@measure_performance
def sieve_of_atkin_python(limit: int) -> list[int]:
    sieve = np.zeros(limit + 1, dtype=bool)

    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]

            n = 3 * x**2 + y**2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]

            n = 3 * x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]

    for r in range(5, int(math.sqrt(limit)) + 1):
        if sieve[r]:
            sieve[r**2 :: r**2] = False

    primes = [2, 3]
    primes.extend(np.nonzero(sieve[5:])[0] + 5)
    return primes
