from .lib_python import primes_in_range_python
from .lib_numpy import primes_in_range_numpy
from .lib_numba import primes_in_range_numba

__all__ = [
    "primes_in_range_numpy",
    "primes_in_range_numba",
    "primes_in_range_python"
]
