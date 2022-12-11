import os
import numpy as np

_fp = 'input.txt'
with open(_fp) as file:
    _input = file.readlines()

def getScenicScore(north,south,west,east,val):
    score = np.zeros(4)
    for i in north[::-1]:
        score[0]+=1
        if i >= val:
            break
    for i in south:
        score[1]+=1
        if i >= val:
            break
    for i in west[::-1]:
        score[2]+=1
        if i >= val:
            break
    for i in east:
        score[3]+=1
        if i >= val:
            break
    print('north, south, west, east')
    print(score)
    return np.prod(score)


grid = [list(a)[:-1] for a in _input]
grid = np.array(grid,dtype=int)

_max = 0
nb_visible = 0
for row in range(grid.shape[0]):
    for col in range(grid.shape[1]):
        # three conditions : border, vertically visible & horizontally visible
        value = grid[row][col]
        print('({},{}) - {} \t {}'.format(row,col,value,nb_visible))
        if (row in [0,98]) or (col in [0,98]):
            nb_visible+=1
        else:
            north = grid[0:row,col]
            south = grid[row+1:grid.shape[0],col]
            west = grid[row,0:col]
            east = grid[row,col+1:grid.shape[1]]
            print(grid[row-3:row+4,col-3:col+4])
            # print(north[::-1])
            # print(south)
            # print(east)
            # print(west[::-1])
            _max = max(_max,getScenicScore(north, south, west, east, value))
        
print(_max)


