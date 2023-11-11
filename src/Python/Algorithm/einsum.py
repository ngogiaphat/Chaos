import numpy as np
from opt_einsum import contract
N = 10
C = np.random.rand(N, N)
I = np.random.rand(N, N, N, N)
%timeit np.einsum('pi,qj,ijkl,rk,sl->pqrs', C, C, I, C, C)
1 loops, best of 3: 934 ms per loop
%timeit contract('pi,qj,ijkl,rk,sl->pqrs', C, C, I, C, C)
1000 loops, best of 3: 324 us per loop