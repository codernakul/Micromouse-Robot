from pyamaze import maze, agent
from collections import deque

def bfs(m):
    # Starting position of the maze
    start = (m.rows, m.cols)
    
    # Initialize front and back queues for BFS traversal
    front = deque([start])
    back = [start]
    
    # Store the path from start to each cell in the 'path' dictionary
    path = {}
    
    while front:
        current = front.popleft()
        
        # If the current cell is the goal cell (1, 1), exit the loop
        if current == (1, 1):
            break
        
        # Explore all neighboring cells
        for d in 'ESNW':
            if m.maze_map[current][d]:
                if d == 'E':
                    child = (current[0], current[1] + 1)
                elif d == 'W':
                    child = (current[0], current[1] - 1)
                elif d == 'N':
                    child = (current[0] - 1, current[1])
                elif d == 'S':
                    child = (current[0] + 1, current[1])
                
                # If the child cell is already visited, skip it
                if child in back:
                    continue
                
                # Add the child cell to both front and back queues
                front.append(child)
                back.append(child)
                
                # Store the path from the child cell to the current cell
                path[child] = current
    
    # Backtrack from the goal cell to the start cell to find the path
    path1 = {}
    cell = (1, 1)
    while cell != start:
        path1[path[cell]] = cell
        cell = path[cell]
        
    return path1

def main():
    # Create a maze and initialize the agent
    m = maze(11, 10)
    m.CreateMaze()
    a = agent(m, filled=True)
    
    # Find the path using BFS and trace the agent's path in the maze
    path = bfs(m)
    m.tracePath({a: path})
    m.run()

if __name__ == "__main__":
    main()
