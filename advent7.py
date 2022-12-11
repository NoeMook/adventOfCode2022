
class Node:
    def __init__(self,data = None, weight = 0, _type = 'f'):
        self.type = _type
        self.data = data
        self.weight = weight
        self.childrens = []
        self.parent = None
    
    def add_child(self,kiddo):
        self.childrens.append(kiddo)
        self.childrens[-1].parent = self

    def print_node(self,_str=''):
        for child in self.childrens:
            print('{}{} - {} - {}'.format(_str,child.data,child.type,child.weight))
            if child.type == 'd':
                child.print_node(_str+'\t')

    def count(self):
        res = 0
        for child in self.childrens:
            if child.type == 'd':
                if child.weight <= 100000:
                    res += child.weight
                res += child.count()
        return res

    def get_min(self,_min,to_empty):
        for child in self.childrens:
            if child.type == 'd':
                print('{} - {} - {}'.format(child.data,child.type,child.weight))
                if child.weight >= to_empty:
                    _min = min(_min,child.weight)
                _min = child.get_min(_min,to_empty)
        return _min




def upt_weight(n: Node):
    for child in n.childrens:
        if child.type == 'f':
            n.weight += child.weight
        else:
            upt_weight(child)
            n.weight += child.weight


_fp = 'input.txt'
with open(_fp) as file:
    _input = file.readlines()

txtFile = ''.join(_input)
commands = [a.split('\n') for a in txtFile.split('$')]
currentDir = Node('/')
root = currentDir
for command in commands[2:]:
    if 'cd' in command[0]:
        #moveDir to first arg
        dirName = command[0].split(' ')[-1]
        if dirName == '..':
            currentDir = currentDir.parent
        else:
            currentDir = [a for a in currentDir.childrens if a.data == dirName][0]
    elif 'ls' in command[0]:
        for dis in command[1:]:
            if dis != '':
                args = dis.split(' ')
                if args[1] not in [a.data for a in currentDir.childrens]:
                    if 'dir' in dis:
                        #dir display get names to put in childrens of current dir
                        currentDir.add_child(Node(args[1],_type = 'd'))
                    else:
                        currentDir.add_child(Node(args[1],int(args[0])))





maxCapacity = 70000000 #: max capacity
# ((maxCapacity - usedSpace) - toEmpty)

upt_weight(root)
updt_need = 30000000
usedSpace = root.weight
to_empty = (updt_need - (maxCapacity - usedSpace))
#print(to_empty)
# print(root.weight)
# root.print_node()
print(root.get_min(updt_need ** 2,to_empty))
        
                
