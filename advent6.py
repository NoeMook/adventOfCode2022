

_fp = 'input.txt'
with open(_fp) as file:
    _input = file.readlines()[0]

def isHeterogenous(s):
    for l in range(len(s)):
        for l2 in range(l+1,len(s)):
            if s[l] == s[l2]:
                return False
    return True

seq = 14
i = seq
for index in range(len(_input[:-1])-(seq-1)):
    if isHeterogenous(_input[index:index+seq]):
        print('{} - {}'.format(_input[index:index+seq],i))
        break
    else:
        print(_input[index:index+seq])
    i += 1