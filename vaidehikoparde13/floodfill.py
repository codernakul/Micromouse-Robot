from pyamaze import maze,agent,COLOR

def floodmap(maze_map,end):
    q=[end]
    visited=[end]
    value_dict={}
    value_dict[end]=0
    while len(q)>0:
        current=q.pop(0)
        for d in 'ESNW':
            if maze_map[current][d]==True:
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
                value_dict[nbr]=value_dict[current]+1
    return value_dict


def findPath(value_dict,start,maze_map, end):
    path=[]
    current=start
    while current!=end:
        if maze_map[current]['E']==True and value_dict[(current[0],current[1]+1)]==value_dict[current]-1:
            current=(current[0],current[1]+1)
            path.append(current)
        elif maze_map[current]['S']==True and value_dict[(current[0]+1,current[1])]==value_dict[current]-1:
            current=(current[0]+1,current[1])
            path.append(current)
        elif maze_map[current]['N']==True and value_dict[(current[0]-1,current[1])]==value_dict[current]-1:
            current=(current[0]-1,current[1])
            path.append(current)
        elif maze_map[current]['W']==True and value_dict[(current[0],current[1]-1)]==value_dict[current]-1:
            current=(current[0],current[1]-1)
            path.append(current)
    return path


def floodfill(start, end, maze_map, emptyMaze): 
    current=start
    while current!=end:    
        emptyMaze[current]=maze_map[current]
        for d in 'EWNS':
            if d=='E' and maze_map[current][d]==0 and (current[0],current[1]+1) in maze_map:
                emptyMaze[(current[0],current[1]+1)]['W']=0
            if d=='W' and maze_map[current][d]==0 and (current[0],current[1]-1) in maze_map:
                emptyMaze[(current[0],current[1]-1)]['E']=0
            if d=='N' and maze_map[current][d]==0 and (current[0]-1,current[1]) in maze_map:
                emptyMaze[(current[0]-1,current[1])]['S']=0
            if d=='S' and maze_map[current][d]==0 and (current[0]+1,current[1]) in maze_map:
                emptyMaze[(current[0]+1,current[1])]['N']=0
        ffPath=findPath(floodmap(emptyMaze, end), current, emptyMaze, end)
        current=ffPath.pop(0)
    return emptyMaze


emptyMaze={(1, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, (2, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 1}, (3, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 1}, (4, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 1}, (5, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 1}, (6, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 1}, (7, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 1}, (8, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 1}, (9, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (1, 2): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (2, 2): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (3, 2): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (4, 2): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (5, 2): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (6, 2): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (7, 2): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (8, 2): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (9, 2): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, (1, 3): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (2, 3): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (3, 3): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (4, 3): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (5, 3): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (6, 3): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (7, 3): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (8, 3): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (9, 3): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, (1, 4): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (2, 4): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (3, 4): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (4, 4): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (5, 4): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (6, 4): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (7, 4): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (8, 4): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (9, 4): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, (1, 5): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (2, 5): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (3, 5): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (4, 5): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (5, 5): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (6, 5): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (7, 5): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (8, 5): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (9, 5): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, (1, 6): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (2, 6): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (3, 6): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (4, 6): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (5, 6): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (6, 6): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (7, 6): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (8, 6): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (9, 6): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, (1, 7): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (2, 7): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (3, 7): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (4, 7): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (5, 7): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (6, 7): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (7, 7): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (8, 7): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (9, 7): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, (1, 8): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (2, 8): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (3, 8): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (4, 8): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (5, 8): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (6, 8): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (7, 8): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (8, 8): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (9, 8): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, (1, 9): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, (2, 9): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (3, 9): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (4, 9): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (5, 9): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (6, 9): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (7, 9): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (8, 9): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (9, 9): {'E': 0, 'W': 1, 'N': 1, 'S': 0}}
start=(9,9)
end=(5,5)
m=maze(9,9)
m.CreateMaze(5,5, loopPercent=10)
maze1=floodfill(start, end, m.maze_map, emptyMaze)#start to end
maze2=floodfill(end, start, m.maze_map, maze1)#end to start

Path=findPath(floodmap(maze2, end), start, maze1, end)
a=agent(m, footprints='true', shape='arrow', color='red')
m.tracePath({a:Path}, delay = 100)
m.run()
