from setuptools import setup, Extension

module = Extension('c_lib', sources=['primes.c'])

setup(
    name='c_lib',
    version='1.0',
    description='A simple C module',
    ext_modules=[module],
)
