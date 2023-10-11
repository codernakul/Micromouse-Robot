from pyamaze import maze, agent

def RCW():
    global direction
    k=list(direction.keys())
    v=list(direction.values())
    v_rotated=[v[-1]]+v[:-1]
    direction=dict(zip(k,v_rotated))

def RCCW():
    global direction
    k=list(direction.keys())
    v=list(direction.values())
    v_rotated=v[1:]+[v[0]]
    direction=dict(zip(k,v_rotated))

def moveForward(cell):
    if direction['forward']=='E':
        return (cell[0],cell[1]+1),'E'
    if direction['forward']=='W':
        return (cell[0],cell[1]-1),'W'
    if direction['forward']=='N':
        return (cell[0]-1,cell[1]),'N'
    if direction['forward']=='S':
        return (cell[0]+1,cell[1]),'S'

def wallFollower(m): #change in mapping of directions
    global direction
    direction={'forward':'N', 'left': 'W', 'back':'S', 'right':'E'}
    current=(m.rows, m.cols)
    path=''
    while True:
        if current==(5,5):
            break
        if m.maze_map[current][direction['left']]==0:
            if m.maze_map[current][direction['forward']]==0:
                RCW()
            else:
                current,d=moveForward(current)
                path+=d
        else:
            RCCW()
            current,d=moveForward(current)
            path+=d
    return path

m=maze(9,9)
m.CreateMaze(5,5)
a=agent(m, footprints='true', shape='arrow', color='green')
Path=wallFollower(m)
m.tracePath({a:Path}, delay=100)
m.run()
