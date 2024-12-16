from python_lib import (
    primes_in_range_numpy,
    primes_in_range_numba,
    primes_in_range_python,
)


def run(a: int, b: int) -> None:
    primes_in_range_numpy(a, b)
    primes_in_range_numba(a, b)
    primes_in_range_python(a, b)
