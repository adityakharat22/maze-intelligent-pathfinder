

import timeit
import pygame
import time
from maze.maze_generator import generate_complex_maze
from maze.maze_visualizer import visualize_maze
from algorithms.dfs import dfs
from algorithms.bfs import bfs
from algorithms.astar import astar

def run_algorithm(maze, start, goal, algorithm, algorithm_name):
    try:
        algorithm_time = timeit.timeit(lambda: algorithm(maze, start, goal), number=1)
        path = algorithm(maze, start, goal)
        print(f"{algorithm_name} took {algorithm_time:.4f} seconds")
        
        if path:
            # Visualize the path with smooth transitions
            visualize_maze(maze, path, smooth=True)
            
            # Keep the window open for 3 seconds
            pygame.time.wait(3000)
        else:
            print(f"{algorithm_name} couldn't find a path.")
    except Exception as e:
        print(f"An error occurred while running {algorithm_name}: {str(e)}")

def main():
    # Generate a more complex maze
    maze_size = 40
    maze = generate_complex_maze(maze_size, maze_size)
    
    # Set start and goal positions at opposite corners
    start = (1, 1)
    goal = (maze_size - 2, maze_size - 2)

    # Run DFS
    run_algorithm(maze, start, goal, dfs, "DFS")

    # Run BFS
    run_algorithm(maze, start, goal, bfs, "BFS")

    # Run A*
    run_algorithm(maze, start, goal, astar, "A*")

    # Keep the final window open until the user closes it
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Complex Maze Solving Algorithms")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()
