from typing import Tuple, List
from collections import deque
import random

def create_random_maze(dim: int) -> Tuple[List[List[int]], Tuple[int, int], Tuple[int, int]]:
    # Crear una cuadrícula llena de paredes (0) usando listas anidadas
    maze = [[0 for _ in range(dim * 2 + 1)] for _ in range(dim * 2 + 1)]

    # Punto de inicio fijo en (1,1)
    x, y = 0, 0
    maze[2*x+1][2*y+1] = 1  # Marcar como camino

    # Inicializar la pila con el punto de inicio
    stack = [(x, y)]
    
    while stack:
        x, y = stack[-1]

        # Definir posibles direcciones (Derecha, Abajo, Izquierda, Arriba)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < dim and 0 <= ny < dim and maze[2*nx+1][2*ny+1] == 0:
                # Marcar como camino
                maze[2*nx+1][2*ny+1] = 1
                # Eliminar la pared intermedia
                maze[2*x+1+dx][2*y+1+dy] = 1
                # Agregar nuevo punto a la pila
                stack.append((nx, ny))
                break
        else:
            stack.pop()

    # BFS para encontrar el punto más alejado del inicio
    def find_farthest_point(start):
        queue = deque([start])
        visited = set([start])
        farthest = start

        while queue:
            node = queue.popleft()
            farthest = node

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbor = (node[0] + dx, node[1] + dy)
                if neighbor in visited:
                    continue
                if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]):
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        queue.append(neighbor)
                        visited.add(neighbor)
        return farthest

    start = (1, 1)
    end = find_farthest_point(start)

    return maze, start, end
