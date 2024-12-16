import functools
import numpy as np

from src import measure_performance


@functools.lru_cache(None)
def sieve_of_eratosthenes_up_to(limit: int) -> np.ndarray:
    primes = np.ones(limit + 1, dtype=bool)
    primes[0], primes[1] = False, False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            primes[i * i : limit + 1 : i] = False

    return primes


def primes_in_range(a: int, b: int) -> np.ndarray:
    primes_up_to_b = sieve_of_eratosthenes_up_to(b)
    return list(np.nonzero(primes_up_to_b[a:])[0] + a)


@measure_performance
def primes_in_range_numpy(a: int, b: int) -> None:
    print(list(primes_in_range(a, b)))
    return None
