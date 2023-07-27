from pyamaze import maze, agent, COLOR

def depth_first_search(puzzle):
    # Starting position of the maze
    start = (puzzle.rows, puzzle.cols)
    
    # Initialize the list to store explored cells (frontier is renamed to to_be_explored)
    explored = [start]
    to_be_explored = [start]
    
    # Dictionary to store the path from the start to each cell using DFS
    dfs_path = {}
    
    while to_be_explored:
        current_cell = to_be_explored.pop()
        
        # If the current cell is the goal cell (1, 1), exit the loop
        if current_cell == (1, 1):
            break
        
        # Explore all neighboring cells
        for direction in 'ESNW':
            if puzzle.maze_map[current_cell][direction] == True:
                if direction == 'E':
                    child_cell = (current_cell[0], current_cell[1] + 1)
                elif direction == 'W':
                    child_cell = (current_cell[0], current_cell[1] - 1)
                elif direction == 'S':
                    child_cell = (current_cell[0] + 1, current_cell[1])
                elif direction == 'N':
                    child_cell = (current_cell[0] - 1, current_cell[1])
                
                # If the child cell is already explored, skip it
                if child_cell in explored:
                    continue
                
                # Add the child cell to both explored and to_be_explored lists
                explored.append(child_cell)
                to_be_explored.append(child_cell)
                
                # Store the path from the child cell to the current cell
                dfs_path[child_cell] = current_cell
    
    # Backtrack from the goal cell to the start cell to find the forward path
    forward_path = {}
    cell = (1, 1)
    while cell != start:
        forward_path[dfs_path[cell]] = cell
        cell = dfs_path[cell]
        
    return forward_path

if __name__ == '__main__':
    # Create a maze and initialize the agent
    puzzle = maze(15, 10)
    puzzle.CreateMaze(loopPercent=100)
    
    # Find the forward path using DFS and trace the agent's path in the maze
    path = depth_first_search(puzzle)
    a = agent(puzzle, footprints=True)
    puzzle.tracePath({a: path})
    puzzle.run()
