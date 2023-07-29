from pyamaze import maze,agent
def bfs(m):
    start=(m.rows,m.cols)
    q=[start]
    vis=[start]
    bfspath={}
    while len(q)>0:
        k=q.pop(0)
        if k==(1,1):
            break
        for d in "ESWN":
            if m.maze_map[k][d]==True:
                if d=="E":
                    cell=(k[0],k[1]+1)
                elif d=="S":
                    cell=(k[0]+1,k[1])
                elif d=="W":
                    cell=(k[0],k[1]-1)
                elif d=="N":
                    cell = (k[0]-1,k[1])
                if cell not in vis:
                    q.append(cell)
                    vis.append(cell)
                    bfspath[cell]=k
                else:
                    continue
    ogpath={}
    ccell=(1,1)
    while ccell!=start:
        ogpath[bfspath[ccell]]=ccell
        ccell=bfspath[ccell]
    return ogpath

m = maze(10,10)
m.CreateMaze()
path = bfs(m)
a=agent(m)
m.tracePath({a:path})
m.run()
