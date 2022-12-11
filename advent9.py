import os
import numpy as np

directions = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}

_fp = 'input.txt'
with open(_fp) as file:
    _input = file.readlines()

def isInRange(pos1,pos2):
    if pos1[0] in [pos2[0]-1,pos2[0],pos2[0]+1]:
        if pos1[1] in [pos2[1]-1,pos2[1],pos2[1]+1]:
            return True
    return False

instructions = [a[:-1].split(' ') for a in _input]

grid = np.zeros((100,100))
startingPos = np.array([grid.shape[0]/2,grid.shape[1]/2])
tPos = np.full(shape=(10,2),fill_value=np.copy(startingPos))

tPosHist = []
tPosHist.append(np.copy(tPos[9]))
for instruction in instructions:
    move = np.array(directions[instruction[0]])
    for i in range(int(instruction[1])):
        tPos[0] += move
        for node in range(1,len(tPos)):
            if not isInRange(tPos[node-1],tPos[node]):
                tPos[node] += np.rint(((tPos[node-1] - tPos[node])/2)+1)-1
        tPosHist.append(np.copy(tPos[9]))

print(len(np.unique(tPosHist,axis=0)))