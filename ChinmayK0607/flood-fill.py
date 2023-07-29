from pyamaze import maze, agent

def floodmap(puzzle, start, goal):
    # Function to generate a flood map from the goal cell to all reachable cells

    queue = [goal]
    visited = [goal]
    floodmap = {goal: 0}
    
    i = 1
    while queue:
        x, y = queue.pop(0)

        if (x, y) == start:
            floodmap[(x, y)] = i
            break

        mover = {'E': 0, 'W': 0, 'N': -1, 'S': 1}
        movec = {'E': 1, 'W': -1, 'N': 0, 'S': 0}
        for d in 'EWNS':
            nx = x + mover[d]
            ny = y + movec[d]

            if puzzle.maze_map[(x, y)][d] == True and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.append((nx, ny))
                floodmap[(nx, ny)] = i

        i += 1
    return floodmap

def floodfill(puzzle, start, goal):
    # Function to find the path from the floodmap
    
    flood_map = floodmap(puzzle, start, goal)
    
    # To make a list of path coordinates from the floodmap
    flood_path = [start]
    x, y = start
    while (x, y) != goal:
        mover = {'E': 0, 'W': 0, 'N': -1, 'S': 1}
        movec = {'E': 1, 'W': -1, 'N': 0, 'S': 0}
        for d in 'EWNS':
            nx = x + mover[d]
            ny = y + movec[d]

            if puzzle.maze_map[(x, y)][d] == True and (nx, ny) in flood_map:
                if flood_map[((nx, ny))] < flood_map[(x, y)]:
                    flood_path.append((nx, ny))
        
        x, y = flood_path[-1]
    
    # To convert this list into a path
    floodfill_path = {}
    for i in range(len(flood_path) - 1, 0, -1):
        floodfill_path[flood_path[i - 1]] = flood_path[i]

    return floodfill_path

def main():
    # Create a maze and initialize the agent
    puzzle = maze(9, 9)
    puzzle.CreateMaze(5, 5, loopPercent=10)
    a = agent(puzzle, shape='arrow', footprints=True)

    # Define the start and goal coordinates
    start = (9, 9)
    goal = (5, 5)

    # Find the path using floodfill and trace the agent's path in the maze
    path = floodfill(puzzle, start, goal)
    puzzle.tracePath({a: path})
    puzzle.run()

if __name__ == '__main__':
    main()
