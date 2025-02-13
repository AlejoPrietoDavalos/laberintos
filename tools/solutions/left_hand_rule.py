from typing import Tuple, List

Point = Tuple[int, int]


def is_solved(last_ij: Point, end: Point) -> bool:
    return last_ij == end

def get_neighbors(last_ij: Point) -> Tuple[Point, Point, Point, Point]:
    """
    Retorna los vecinos de un i-j.
    - `p_left, p_up, p_right, p_bottom`.
    """
    i, j = last_ij
    p_left =  i, j-1
    p_up = i-1, j
    p_right = i, j+1
    p_bottom = i+1, j
    return p_left, p_up, p_right, p_bottom

def is_not_wall(maze: List[List[int]], point: Point) -> bool:
    i, j = point
    return maze[i][j] != 0


def solve_by_left_hand_rule(
        maze: List[List[int]],
        start: Point,
        end: Point,
) -> List[Point]:
    """
    1. Si podemos doblar a la izquierda, doblamos.
    2. Sino, seguir hacia delante.
    3. Sino, doblar a la derecha.
    4. Si ninguna de las 3 se posible, entonces volver hacia atrás.
    """
    last_ij = start
    result = [last_ij]
    
    # Verificamos los 4 puntos de izquierda derecha arriba y abajo.
    # El primero que NO sea una pared, nos movemos hacia allí.
    p_left, p_up, p_right, p_bottom = get_neighbors(last_ij)
    if is_not_wall(maze, p_left):
        result.append(p_left)
    elif is_not_wall(maze, p_up):
        result.append(p_up)
    elif is_not_wall(maze, p_right):
        result.append(p_right)
    elif is_not_wall(maze, p_bottom):
        result.append(p_bottom)
    else:
        raise ValueError("El laberinto está mal diseñado, callejón sin salida.")

    #while not is_solved(last_ij, end):
    #    #versor: Tuple[int, int] = None
    #    pass
    return result
