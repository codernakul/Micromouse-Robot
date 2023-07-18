from pyamaze import maze, agent, COLOR


def WallFollower(maze1: maze, orient_map: dict):
    maze_data = maze1.maze_map
    curpos = [16, 16]
    orient = 'N'
    pos_change = {'N' : (-1, 0), 'E' : (0, 1), 'W' : (0, -1), 'S' : (1, 0)}
    path = ""

    while curpos != [8, 8]:

        adj = maze_data[tuple(curpos)][orient_map[orient]]
        forward = maze_data[tuple(curpos)][orient]

        if forward == 0 and adj == 0:
            orient = list(orient_map.keys())[list(orient_map.values()).index(orient)]
            continue
        if adj == 1:
            orient = orient_map[orient]

        path += orient
        curpos[0] += pos_change[orient][0]
        curpos[1] += pos_change[orient][1]
        
    return path

maze1 = maze(16, 16)
maze1.CreateMaze(8, 8)

l = agent(maze1, shape = 'arrow')
r = agent(maze1, shape = 'arrow', color = COLOR.red)

left_map = {'N' : 'W', 'W' : 'S', 'E' : 'N', 'S' : 'E'}
right_map = {'N' : 'E', 'W' : 'N', 'E' : 'S', 'S' : 'W'}

maze1.tracePath({l : WallFollower(maze1, left_map)}, kill = True, delay = 25)
maze1.tracePath({r : WallFollower(maze1, right_map)}, kill = True, delay = 25)

maze1.run()