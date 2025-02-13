from typing import Tuple, List


def solve_by_left_hand_rule(
        maze: List[List[int]],
        start: Tuple[int, int],
        end: Tuple[int, int],
):
    """
    1. Si podemos doblar a la izquierda, doblamos.
    2. Sino, seguir hacia delante.
    3. Sino, doblar a la derecha.
    4. Si ninguna de las 3 se posible, entonces volver hacia atrás.
    """
    result = [start]
    #versor: Tuple[int, int] = None
    return result
