from python_lib import sieve_of_atkin_numba, sieve_of_atkin_python
from c_lib import sieve_of_atkin_c

n = 1_000_000
mi = 2
len_prost = 0
while n > len_prost:
    mi += 10_000
    len_prost = len(sieve_of_atkin_numba(mi))
    print(len_prost)
    print(len(sieve_of_atkin_c(mi)))
