"""! @file profiling.py
@brief Profiling tool calculating deviation using the math library
@author xhnato00, xlanro00, xmacho12, xslivk03
"""

import math_library as mlib

avg = 0

_NUMBERS = input().split()
for i in _NUMBERS:
    avg = mlib.add(avg, float(i))

avg = mlib.divide(avg, len(_NUMBERS))
s = 0

for i in _NUMBERS:
    s = mlib.add(s, mlib.exponentiate(float(i), 2))

s = mlib.subtract(s, mlib.multiply(len(_NUMBERS), mlib.exponentiate(avg, 2)))
s = mlib.divide(s, mlib.subtract(len(_NUMBERS), 1))
s = mlib.root(s, 2)
print(s)
