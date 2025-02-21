from typing import Tuple, Literal, List
from datetime import datetime, UTC

from tools.random_maze import create_random_maze
from tools.animation import animate_maze_solution
from tools.solutions.tremaoux import solve_by_tremaoux
from tools.solutions.left_hand_rule import solve_by_left_hand_rule

# Acá vamos a listar todas las formas de resolver un laberinto programada por nosotrxs.
TypeSolve = Literal[
    "tremaoux",
    "left-hand-rule"
]

def solve_maze(
        maze: List[List[int]],
        start: Tuple[int, int],
        end: Tuple[int, int],
        how_solve: TypeSolve
):
    if how_solve == "tremaoux":
        result = solve_by_tremaoux(maze, start, end)
    elif how_solve == "left-hand-rule":
        result = solve_by_left_hand_rule(maze, start, end)
    else:
        raise ValueError(f"how_solve={how_solve} es incorrecto. Usar {TypeSolve}")
    return result


def main(dim: int, how_solve: TypeSolve):
    maze, start, end = create_random_maze(dim)
    print(f"Maze aleatorio generado con dim={dim} - start={start} - end={end}")
    result = solve_maze(maze, start, end, how_solve)

    path_gif = f"({how_solve}) {datetime.now(tz=UTC).strftime('%Y-%m-%d %H-%M-%S')}.gif"
    animate_maze_solution(maze, start, end, result, path_gif)
    print("Resueltoooooo!!!!")


if __name__ == "__main__":
    dim = 10
    how_solve = "left-hand-rule"
    main(dim, how_solve)
