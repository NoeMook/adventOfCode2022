import os
import numpy as np

with open('input.txt') as file:
    _input = file.readlines()

def get_common_letter(s1,s2):
    for l1 in s1:
        for l2 in s2:
            if (l1 == l2):
                return l1
    return ''
def get_common_letter(s1,s2,s3):
    for l1 in s1:
        for l2 in s2:
            if (l1 == l2):
                for l3 in s3:
                    return l1
    return ''
def get_ascii_prio(l):
    prio = ord(l.lower()) - 96
    
    prio += 26 if (l.upper() == l) else 0
    print(l + ' - ' +str(prio))
    return prio


sum = 0
i = 0
for item in range(0,len(_input),3):
# for item in range(0,6,3):
    s1, s2, s3 = (_input[item],_input[item+1],_input[item+2])
    print(s1 + s2 + s3)
    l = get_common_letter(s1[:-1],s2[:-1],s3[-1])
    i += 1
    sum += get_ascii_prio(l)
print(i)
print(sum)
