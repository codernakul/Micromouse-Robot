#for dfs algorithm we can use "pop" instead of "popleft"
from pyamaze import maze,agent
def dfs(m):
    start=(m.rows,m.cols)
    s=[start]
    vis=[start]
    dfspath={}
    while len(s)>0:
        t=s.pop()
        if t==(1,1):
            break
        for d in "ESWN":
            if m.maze_map[t][d]==True:
                if d=="E":
                    cell=(t[0],t[1]+1)
                elif d=="S":
                    cell=(t[0]+1,t[1])
                elif d=="W":
                    cell=(t[0],t[1]-1)
                elif d=="N":
                    cell = (t[0]-1,t[1])
                if cell not in vis:
                    s.append(cell)
                    vis.append(cell)
                    dfspath[cell]=t
                else:
                    continue
    ogpath={}
    ccell=(1,1)
    while ccell!=start:
        ogpath[dfspath[ccell]]=ccell
        ccell=dfspath[ccell]
    return ogpath

m = maze(10,10)
m.CreateMaze()
path = dfs(m)
a=agent(m)
m.tracePath({a:path})
m.run()
