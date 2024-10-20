# algorithms/bfs.py

from collections import deque
from maze.maze_utils import get_neighbors  # Import the get_neighbors function

def bfs(maze, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (current, path) = queue.popleft()
        if current == goal:
            return path

        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # No path found
