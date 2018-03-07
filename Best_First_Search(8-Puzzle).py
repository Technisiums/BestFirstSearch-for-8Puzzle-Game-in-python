#please don't forget to read the ReadMe.txt file
import copy
import operator
start = [[2,8,3],[1,6,4],[7,-1,5]]
goal = [[1,2,3],[8,-1,4],[7,6,5]]
childs = []
def displace(puzzle_box,goal):
    count=0
    for i in range(0,3):
        for j in range(0,3):
            if(puzzle_box[i][j]!=goal[i][j]):
                if(puzzle_box[i][j]!=-1):
                    count=count+1
                else:
                    count=count
    return count
def move_left(puzzle_box,x,y):
    root=copy.deepcopy(puzzle_box)
    root[x][y],root[x][y-1] = root[x][y-1],root[x][y]
    return root

def move_right(puzzle_box,x,y):
    root=copy.deepcopy(puzzle_box)
    root[x][y],root[x][y+1] = root[x][y+1],root[x][y]
    return root

def move_up(puzzle_box,x,y):
    root=copy.deepcopy(puzzle_box)
    root[x][y],root[x-1][y] = root[x-1][y],root[x][y]
    return root

def move_down(puzzle_box,x,y):
    root=copy.deepcopy(puzzle_box)
    root[x][y],root[x+1][y] = root[x+1][y],root[x][y]
    return root

def star(puzzle_box):
    for i in range(0,3):
        for j in range (0,3):
            if(puzzle_box[i][j]==-1):
                return i,j

def genrate_childs(puzzle_box,x,y):
    if y==0 and x==0:
        child1=move_right(puzzle_box,x,y)
        child2=move_down(puzzle_box,x,y)
        childs=[child1,child2]
    elif y==2 and x==2:
        child1=move_left(puzzle_box,x,y)
        child2=move_up(puzzle_box,x,y)
        childs=[child1,child2]
    elif y==2:
        child1=move_down(puzzle_box,x,y)
        child2=move_up(puzzle_box,x,y)
        child3=move_left(puzzle_box,x,y)
        childs=[child1,child2,child3]
    elif x==0:
        child1=move_right(puzzle_box,x,y)
        child2=move_down(puzzle_box,x,y)
        child3=move_left(puzzle_box,x,y)
        childs=[child1,child2,child3]
    elif y==0:
        child1=move_right(puzzle_box,x,y)
        child2=move_down(puzzle_box,x,y)
        child3=move_up(puzzle_box,x,y)
        childs=[child1,child2,child3]
    elif x==2:
        child1=move_right(puzzle_box,x,y)
        child2=move_up(puzzle_box,x,y)
        child3=move_left(puzzle_box,x,y)
        childs=[child1,child2,child3]
    else:
        child1=move_right(puzzle_box,x,y)
        child2=move_down(puzzle_box,x,y)
        child3=move_up(puzzle_box,x,y)
        child4=move_left(puzzle_box,x,y)
        childs=[child1,child2,child3,child4]
    return childs

def open_compare(op,open1):
    extract = []
    for i in open1:
        extract.append(i[1])
    for j in extract:
        if op == j:
            return 1
        else:
            return 0
def open_close(x,close):
    for i in close:
        if i==x:
            return 1
    return 0+
def set_x(open1):
    x =[]
    minimum = min(open1,key=lambda x:x[0])
    min_val = minimum[0]
    for i in open1:
        if i[0] == min_val:
         x.append(i)
    return x
def remove_from_open(x,open1):
    for i in x:
        open1.remove(i)
    return open1
def best_first_search(root):
    root_value=displace(root,goal)+1
    open1 = [[root_value,root]]
    close = []
    level = 2
    keylist=[]
    k=root_value
    v = 1
    while open1:
        x = set_x(open1)
        remove_from_open(x,open1)
        for k in x:
            print("Selected Block")
            print(k)
            if displace(k[1],goal) == 0:
                print('Success')
                return level
            else:
                s1,s2=star(k[1])
                childs = genrate_childs(k[1],s1,s2)
                print("Childs")
                for i in childs:
                    print(i)
                    #if (open_close(i,close)==0 and open_compare(i,open1)==0):
                    value = displace(i,goal) + level
                    open1.append([value,i])
                close.append(k[1])
        open1.sort(key=lambda x:x[0])
        print("Arranged Open List")
        print(open1)
        level=level+1
    return -1
print(best_first_search(start))    


