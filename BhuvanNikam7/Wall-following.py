#code for wall following
b=[]
n = int(input())
m = int(input())
print(n,m)
for i in range(0,n):
    col=[]
    for j in range(0,m):
        k = input()
        col.append(k)
    b.append(col)
for i in range(0,n):
    print (b[i])
from collections import deque
#by right hand rule

def wallfallowing(grid):
   
    path = ''
    x,y =0,0
    n = len(grid)
    m = len(grid[0])
    end =(n-1,m-1)
    i=0
    j=0
    while (x,y) != end :
        if x < n-1 and grid[x+1][y]!='#' and  grid[x][y+1]!='#':
            path += 'R'
            x=x+1
        elif y < m-1 and grid[x][y+1]!='#':
            path +='D'
            y=y+1
        elif x > 0 and grid[x-1][y]!='#':
            path +='U'
            x=x-1
        elif y > 0 and grid[x][y-1]!='#':
            path +='L'
            y=y-1
        else:
            print("No path exists!")
            break
    print(path)
wallfallowing(b)
