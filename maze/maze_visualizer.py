# maze/maze_visualizer.py

import pygame
import time

def visualize_maze(maze, path, smooth=False):
    pygame.init()
    
    # Calculate cell size based on maze dimensions
    max_size = 800
    cell_size = min(max_size // len(maze), max_size // len(maze[0]))
    
    width = len(maze[0]) * cell_size
    height = len(maze) * cell_size
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maze Visualization")

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    screen.fill(WHITE)

    # Draw the maze
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, (x * cell_size, y * cell_size, cell_size, cell_size))

    # Draw the path
    if path:
        for i, (x, y) in enumerate(path):
            color = RED if (x, y) == path[-1] else BLUE
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
            if smooth:
                pygame.display.flip()
                time.sleep(0.01)  # Reduced delay for smoother visualization

    pygame.display.flip()

    if not smooth:
        # Keep the window open for 3 seconds if not in smooth mode
        pygame.time.wait(3000)
