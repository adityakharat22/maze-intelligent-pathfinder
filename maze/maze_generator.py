# maze/maze_generator.py

import numpy as np
import random

def generate_maze(rows, cols):
    maze = np.ones((rows, cols), dtype=int)  # Start with all walls
    maze[1:-1, 1:-1] = 0                    # Create open space in the maze
    return maze

def generate_complex_maze(width, height):
    # Initialize the maze with walls
    maze = [[1 for _ in range(width)] for _ in range(height)]
    
    def carve_path(x, y):
        maze[y][x] = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[y + dy][x + dx] = 0
                carve_path(nx, ny)
    
    # Start carving from the top-left corner
    carve_path(1, 1)
    
    # Ensure start and goal are open
    maze[1][1] = maze[height - 2][width - 2] = 0
    
    return maze

# Example maze:
# 1 1 1 1 1 1
# 1 0 0 0 0 1
# 1 0 1 0 1 1
# 1 0 0 0 0 1
# 1 1 1 1 1 1
