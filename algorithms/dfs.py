# algorithms/dfs.py

from maze.maze_utils import get_neighbors

def dfs(maze, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        (current, path) = stack.pop()
        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor in get_neighbors(maze, current):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None
