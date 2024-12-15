from numba import jit

from src import measure_performance

@jit(nopython=True) # type: ignore
def sieve_of_eratosthenes_up_to(limit: int) -> list[int]:
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    result = []
    for i in range(limit + 1):
        if primes[i]:
            result.append(i)

    return result

@jit(nopython=True) # type: ignore
def primes_in_range(a: int, b: int) -> list[int]:
    primes_up_to_b = sieve_of_eratosthenes_up_to(b)
    return [p for p in primes_up_to_b if p >= a]

@measure_performance
def primes_in_range_numba(a: int, b: int) -> None:
    print(primes_in_range(a, b))
    return None
