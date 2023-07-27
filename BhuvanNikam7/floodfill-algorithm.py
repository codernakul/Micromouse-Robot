from pyamaze import maze, agent
from collections import deque

def floodfillpath(m):
    start = (1, 1)
    ff = {start: 0}
    q = deque()
    q.append((1,1))
    vis =[start]
    i = 1
    while q:
        cell= q.popleft()
        x=cell[0]
        y=cell[1]
        if (x, y) == (m.rows, m.cols):
            ff[(x, y)]=i
            break
        for d in 'ESNW':
            if m.maze_map[(x,y)][d] == True:
                if d == 'E':
                    chcell = (x, y+1)
                elif d == 'S':
                    chcell = (x+1, y)
                elif d == 'W':
                    chcell = (x, y-1)
                elif d == 'N':
                    chcell = (x-1, y)
                if chcell not in vis:
                    q.append(chcell)
                    vis.append(chcell)
                    ff[chcell]=i
                else:
                    continue
        i = i+1
    beg = (m.rows,m.cols)
    print(ff)
    ffpath = {}
    while True:
        if beg == (1,1):
            break
        for d in 'ESNW':
            if m.maze_map[beg][d] == True:
                if d == 'E' and ff[beg] > ff[(beg[0], beg[1]+1)] and beg in ff:
                    ffpath[beg] = (beg[0], beg[1]+1)
                    beg = (beg[0], beg[1]+1)
                elif d == 'S' and ff[beg] > ff[(beg[0]+1, beg[1])] and beg in ff:
                    ffpath[beg] = (beg[0]+1, beg[1])
                    beg = (beg[0]+1, beg[1])
                elif d == 'W' and ff[beg] > ff[(beg[0], beg[1]-1)] and beg in ff:
                    ffpath[beg] = (beg[0], beg[1]-1)
                    beg = (beg[0], beg[1]-1)
                elif d == 'N' and ff[beg] > ff[(beg[0]-1, beg[1])] and beg in ff:
                    ffpath[beg] = (beg[0]-1, beg[1])
                    beg = (beg[0]-1, beg[1])
    return ffpath

m = maze(7, 7)
m.CreateMaze()# Debugging line
path = floodfillpath(m)
a = agent(m,footprints=True)
m.tracePath({a:path},)
m.run()
