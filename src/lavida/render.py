import pygame
import numpy as np


def draw_state(
    screen: pygame.Surface,
    game_state: np.ndarray,
    nx_cells: int,
    ny_cells: int,
    dim_cell_w: float,
    dim_cell_h: float,
) -> None:
    for y in range(ny_cells):
        for x in range(nx_cells):
            poly = [
                (x * dim_cell_w, y * dim_cell_h),
                ((x + 1) * dim_cell_w, y * dim_cell_h),
                ((x + 1) * dim_cell_w, (y + 1) * dim_cell_h),
                (x * dim_cell_w, (y + 1) * dim_cell_h),
            ]

            if game_state[x, y] == 0:
                pygame.draw.polygon(screen, (40, 40, 40), poly, 1)
            else:
                pygame.draw.polygon(screen, (200, 100, 100), poly, 0)
