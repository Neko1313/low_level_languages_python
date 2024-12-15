#include <stdbool.h>
#include <Python.h>

static PyObject* sieve_of_eratosthenes_up_to(PyObject* self, PyObject* args) {
    int limit;
    if (!PyArg_ParseTuple(args, "i", &limit)) {
        return NULL;
    }

    bool* primes = (bool*)malloc((limit + 1) * sizeof(bool));
    for (int i = 0; i <= limit; ++i) {
        primes[i] = true;
    }
    primes[0] = primes[1] = false;

    for (int i = 2; i * i <= limit; ++i) {
        if (primes[i]) {
            for (int j = i * i; j <= limit; j += i) {
                primes[j] = false;
            }
        }
    }

    PyObject* result = PyList_New(0);
    for (int i = 2; i <= limit; ++i) {
        if (primes[i]) {
            PyList_Append(result, PyLong_FromLong(i));
        }
    }

    free(primes);
    return result;
}

static PyMethodDef MyMethods[] = {
    {"sieve_of_eratosthenes_up_to", sieve_of_eratosthenes_up_to, METH_VARARGS, "Find all primes up to a given limit"},
    {NULL, NULL, 0, NULL}
};

// Описание модуля
static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "c_lib",
    "A simple C module",
    -1,
    MyMethods
};

PyMODINIT_FUNC PyInit_mymodule(void) {
    return PyModule_Create(&mymodule);
}
