from pyamaze import maze, agent

def BFS(m,start,end):
    q=[start]
    visited=[start]
    mydict={}
    while len(q)>0:
        current=q.pop(0)
        if current==end:
            break
        for d in 'ESNW':
            if m.maze_map[current][d]==True:
                if d=='E':
                    nbr=(current[0],current[1]+1)
                elif d=='S':
                    nbr=(current[0]+1,current[1])
                elif d=='N':
                    nbr=(current[0]-1,current[1])
                elif d=='W':
                    nbr=(current[0],current[1]-1)   
                if nbr in visited:
                    continue
                q.append(nbr)
                visited.append(nbr)   
                mydict[nbr]=current   
    mypath={}
    cell=end
    while cell!=start:
        mypath[mydict[cell]]=cell
        cell=mydict[cell]
    return mypath

m=maze(9,9)
m.CreateMaze(5,5,loopPercent=30)
start=(9,9)
end=(5,5)
path=BFS(m,start,end)
a=agent(m, footprints='true', shape='arrow')
m.tracePath({a:path})
m.run()
