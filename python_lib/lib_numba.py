import math
from numba import jit
from src import measure_performance


@measure_performance
@jit(nopython=True)  # type: ignore
def sieve_of_atkin_numba(limit: int) -> list[int]:
    sieve = [False] * (limit + 1)

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
            for multiple in range(r**2, limit + 1, r**2):
                sieve[multiple] = False

    # List of primes
    primes = [2, 3]
    for i in range(5, limit + 1):
        if sieve[i]:
            primes.append(i)

    return primes
