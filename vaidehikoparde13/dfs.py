from pyamaze import maze, agent

def DFS(m,start,end):
    stack=[start]
    visited=[start]
    mydict={}
    while len(stack)>0:
        current=stack.pop()
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
                stack.append(nbr)
                visited.append(nbr)
                mydict[nbr]=current
    mypath={}
    temp=end
    while temp!=start:
        mypath[mydict[temp]]=temp
        temp=mydict[temp]
    return mypath

m=maze(9,9)
m.CreateMaze(5,5,loopPercent=60)
start=(9,9)
end=(5,5)
path=DFS(m,start,end)
a=agent(m)
m.tracePath({a:path})
m.run()
