import os
import numpy as np

_fp = 'input.txt'
with open(_fp) as file:
    _input = file.readlines()

val_l = []
c = 0

for i,l in enumerate(_input):
    if l[:-1] == "":
        val_l.append(c)
        c = 0
    else:
        c += int(l[:-1])
print(sum(sorted(val_l)[-3:]))

