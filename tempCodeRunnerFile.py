# main.py

import timeit
from maze.maze_generator import generate_maze
from maze.maze_visualizer import visualize_maze
from algorithms.dfs import dfs
from algorithms.bfs import bfs
from algorithms.astar import astar

def main():
    maze = generate_maze(20, 20)
    start = (1, 1)
    goal = (18, 18)

    # Run DFS
    dfs_time = timeit.timeit(lambda: dfs(maze, start, goal), number=1)
    dfs_path = dfs(maze, start, goal)
    print(f"DFS took {dfs_time:.4f} seconds")
    visualize_maze(maze, dfs_path)

    # Run BFS
    bfs_time = timeit.timeit(lambda: bfs(maze, start, goal), number=1)
    bfs_path = bfs(maze, start, goal)
    print(f"BFS took {bfs_time:.4f} seconds")
    visualize_maze(maze, bfs_path)

    # Run A*
    astar_time = timeit.timeit(lambda: astar(maze, start, goal), number=1)
    astar_path = astar(maze, start, goal)
    print(f"A* took {astar_time:.4f} seconds")
    visualize_maze(maze, astar_path)

if __name__ == "__main__":
    main()
