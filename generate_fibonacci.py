#! /bin/env python3

import numpy as np

def fib_dirs(n):
    i = np.arange(n); g = (np.sqrt(5)-1)/2
    z = 1 - 2*(i+0.5)/n; phi = 2*np.pi*np.mod(i*g, 1.0); r = np.sqrt(1-z*z)
    return np.c_[r*np.cos(phi), r*np.sin(phi), z]

def all_x(n): return np.tile([1.0, 0.0, 0.0], (n,1))

np.savetxt("dirs/dirs_fibonacci_2700.txt", fib_dirs(2700), fmt="%.8f")
np.savetxt("dirs/dirs_allX_2700.txt",      all_x(2700),    fmt="%.8f")
