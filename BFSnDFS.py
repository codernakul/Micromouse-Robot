from pyamaze import maze, agent, COLOR

maze1 = maze(16, 16)
maze1.CreateMaze(8, 8, loopPercent = 20)

maze_data = maze1.maze_map
pos_change = {'N':(-1, 0), 'S':(1, 0), 'E':(0, 1), 'W':(0, -1)}

queue = []
curpos = (16, 16)
visited = []
path = {}

while curpos != (8, 8):
    visited.append(curpos)

    for i in ['N', 'S', 'E', 'W']:
        pos = (curpos[0] + pos_change[i][0], curpos[1] + pos_change[i][1])
        if maze_data[curpos][i] == 1 and pos not in visited and pos not in queue:
            queue.append(pos)
            path[pos] = curpos

    curpos = queue[0]
    queue = queue[1:]

actual_path = {}
while curpos != (16, 16):
    actual_path[path[curpos]] = curpos
    curpos = path[curpos]


search = agent(maze1, footprints = True)
ag = agent(maze1, shape = 'arrow', footprints = True)


maze1.tracePath({search : visited}, kill = True, delay = 100)
maze1.tracePath({ag : actual_path}, kill = True, delay = 150)


stack = []
curpos = (16, 16)
visited = []
path = {}

while curpos != (8, 8):
    visited.append(curpos)

    for i in ['N', 'S', 'E', 'W']:
        pos = (curpos[0] + pos_change[i][0], curpos[1] + pos_change[i][1])
        if maze_data[curpos][i] and pos not in visited:
            stack.append(pos)
            path[pos] = curpos

    curpos = stack.pop()

actual_path = {}
while curpos != (16, 16):
    actual_path[path[curpos]] = curpos
    curpos = path[curpos]


search = agent(maze1, footprints = True, color = COLOR.red)
ag = agent(maze1, shape = 'arrow', footprints = True, color = COLOR.red)

maze1.tracePath({search : visited}, kill = True, delay = 100)
maze1.tracePath({ag : actual_path}, kill = True, delay = 150)

maze1.run()