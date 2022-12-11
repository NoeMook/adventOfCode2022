import os
from itertools import chain
_fp = 'input.txt'
with open(_fp) as file:
    _input = file.readlines()

def parsing_mov(line):
    sp = line[:-1].split(' ')
    return (int(sp[1]),int(sp[3])-1,int(sp[5])-1)
def parsing_input(inpt):
    return (inpt[:9],inpt[10:])

head, movs = parsing_input(_input)
t = [[a[b] for a in head[:-1] if a[b] != ' '] for b in range(1,34,4)]

for l in movs:
    nbCrates, fromId, toId = parsing_mov(l)
    print('{} - {} - {} - {}'.format(t[fromId][0:nbCrates],nbCrates,fromId,toId))
    t[toId].insert(0, t[fromId][0:nbCrates])
    t[toId] = list(chain(*t[toId]))
    for i in range(nbCrates):
        t[fromId].pop(0)
    for j in t :
        print(''.join(j))

print(''.join([a[0] for a in t]))