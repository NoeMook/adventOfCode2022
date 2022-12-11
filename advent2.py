import os

with open('input.txt') as file:
    _input = file.readlines()


def get_score(p1,p2):
    # p1, ord(p1[0])
    # p2[:-1], ord(p2[0]) - 23)
    score = 0
    if ord(p1[0]) == ord(p2[0]) - 23:
        score += 3
    elif (ord(p1[0]) - 65 + 1) % 3 == (ord(p2[0])- 65 - 23):
        score += 6
    print('{} - {}  ---  {} - {}'.format(p1,p2,score,modifier))
    return score + (ord(p2[0])- 64 - 23)

sum = 0
for i in _input:
    modifier = ord(i.split(' ')[1][0]) - 66
    print(str(modifier - 23))
    ans = chr(ord(i.split(' ')[0][0])+modifier)
    print(ans)
    if ans == '[':ans = 'X'
    elif ans == 'W':ans = 'Z'
    sum += get_score(i.split(' ')[0],ans)
print(sum)