import os
import numpy as np
def isContained(panels):
    return ((panels[0][0] >= panels[1][0]) and (panels[0][1] <= panels[1][1])) or ((panels[0][0] <= panels[1][0]) and (panels[0][1] >= panels[1][1]))
def isOverlaped(panels):
    if (panels[0][0] > panels[1][1]) or (panels[1][0] > panels[0][1]):
        return False
    return True

_fp = 'input.txt'
with open(_fp) as file:
    _input = file.readlines()
c = 0
for line in _input:
    line = line[:-1]
    panels = line.split(',')
    for p in range(len(panels)):
        panels[p] = [int(a) for a in panels[p].split('-')]
    if isOverlaped(panels):
        c += 1

print(c)