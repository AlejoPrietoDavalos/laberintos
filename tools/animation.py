import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from typing import List, Tuple

def animate_maze_solution(maze: np.ndarray, start: Tuple[int, int], end: Tuple[int, int], result: List[Tuple[int, int]], output_filename="maze_solution.gif"):
    frames = []

    for step in range(1, len(result) + 1):  # Desde el primer paso hasta el final
        fig, ax = plt.subplots()
        ax.imshow(maze, cmap="gray")

        # Dibujar inicio y fin
        ax.scatter(start[1], start[0], color="red", label="Inicio", s=100)
        ax.scatter(end[1], end[0], color="green", label="Final", s=100)

        # Dibujar la línea del camino recorrido con transparencia (alpha)
        if step > 1:
            prev_steps = np.array(result[:step])  # Camino recorrido hasta ahora
            ax.plot(prev_steps[:, 1], prev_steps[:, 0], color="blue", alpha=0.5, linewidth=2)

        # Dibujar la posición actual como una pelota azul más grande
        current_pos = result[step - 1]
        ax.scatter(current_pos[1], current_pos[0], color="blue", s=150)  # Última posición

        ax.legend()
        plt.axis("off")
        fig.canvas.draw()

        # Convertir la figura en imagen de PIL
        img = Image.frombuffer("RGBA", fig.canvas.get_width_height(), fig.canvas.buffer_rgba(), "raw", "RGBA", 0, 1)
        frames.append(img.convert("RGB"))

        plt.close(fig)  # Liberar memoria

    # Guardar como GIF
    frames[0].save(output_filename, save_all=True, append_images=frames[1:], duration=300, loop=0)
