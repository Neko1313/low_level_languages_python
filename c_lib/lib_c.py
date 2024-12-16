import ctypes
from pathlib import Path
import platform

from src import measure_performance


def _get_name_export(name: str) -> Path:
    lib_file = f"{name}.so"
    if platform.architecture() == ("64bit", "WindowsPE"):
        lib_file = f"{name}_64.dll"

    if platform.architecture() == ("32bit", "WindowsPE"):
        lib_file = f"{name}_32.dll"

    return Path(__file__).resolve().parent / lib_file


def fn_sieve_of_atkin_c() -> ctypes.CDLL:
    lib_path = _get_name_export('libsieve_of_atkin')
    lib = ctypes.cdll.LoadLibrary(str(lib_path))
    lib.sieve_of_atkin.argtypes = [
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_int),
        ctypes.POINTER(ctypes.c_int),
    ]
    lib.sieve_of_atkin.restype = None
    return lib

@measure_performance
def sieve_of_atkin_c(limit: int) -> list[int]:
    primes = (ctypes.c_int * (limit // 2))()
    prime_count = ctypes.c_int(0)
    lib = fn_sieve_of_atkin_c()
    lib.sieve_of_atkin(limit, primes, ctypes.byref(prime_count))

    return list(primes[: prime_count.value])
