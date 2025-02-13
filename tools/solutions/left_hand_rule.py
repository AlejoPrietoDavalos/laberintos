from typing import Tuple, List

Point = Tuple[int, int]
Direction = Tuple[int, int]


def get_versor_left_y_todos_los_demas_no_se(versor: Direction) -> List[Direction]:
    dirs_horario = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    idx_versor = dirs_horario.index(versor)
    idx_versor_left = (idx_versor - 1) % len(dirs_horario)

    return dirs_horario[idx_versor_left:] + dirs_horario[:idx_versor_left]


def is_solved(last_ij: Point, end: Point) -> bool:
    return last_ij == end


def get_point_first(maze: List[List[int]], last_ij: Point) -> Point:
    # Verificamos los 4 puntos de izquierda derecha arriba y abajo.
    # El primero que NO sea una pared, nos movemos hacia allí.
    p_left, p_up, p_right, p_bottom = get_neighbors(last_ij)
    if is_not_wall(maze, p_left):
        return p_left
    elif is_not_wall(maze, p_up):
        return p_up
    elif is_not_wall(maze, p_right):
        return p_right
    elif is_not_wall(maze, p_bottom):
        return p_bottom
    else:
        raise ValueError("El laberinto está mal diseñado, callejón sin salida.")


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


def is_wall(maze: List[List[int]], point: Point) -> bool:
    return not is_not_wall(maze, point)


def get_versor(result: List[Point]) -> Direction:
    """ Hacemos la resta vectorial del último punto con el anteúltimo."""
    p1_i, p1_j = result[-2]
    p2_i, p2_j = result[-1]
    direction = (p2_i - p1_i, p2_j - p1_j)
    return direction


def next_point_from_versor_point(last_ij: Point, versor: Direction) -> Point:
    i, j = last_ij
    versor_i, versor_j = versor
    return (i + versor_i, j + versor_j)


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
    
    point_first = get_point_first(maze, last_ij)
    result.append(point_first)

    sarlanga = 0
    while sarlanga < 1000 and not is_solved(last_ij, end):
        # Obtenemos la dirección actual de movimiento.
        versor = get_versor(result)
        last_ij = result[-1]

        # Sacamos el versor de la izquierda, y todos los demás en sentido horario.
        versors_to_try = get_versor_left_y_todos_los_demas_no_se(versor)

        for versor_to_try in versors_to_try:
            point_to_try = next_point_from_versor_point(last_ij, versor_to_try)
            if is_not_wall(maze, point_to_try):
                # Sino fuera una pared (camino), entonces lo agrega al resultado.
                result.append(point_to_try)
                break
            # Continúa si ese versor es una pared.
        sarlanga += 1
    return result
