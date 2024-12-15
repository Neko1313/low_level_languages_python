import functools

from src import measure_performance

@functools.lru_cache(None)
def sieve_of_eratosthenes_up_to(limit: int) -> list[int]:
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    return [i for i, is_prime in enumerate(primes) if is_prime]


def primes_in_range(a: int, b: int)  -> list[int]:
    primes_up_to_b = sieve_of_eratosthenes_up_to(b)
    return [p for p in primes_up_to_b if p >= a]

@measure_performance
def primes_in_range_python(a: int, b: int) -> None:
    print(primes_in_range(a, b))
    return None

