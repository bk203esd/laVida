import numpy as np


def count_neighbors(game_state: np.ndarray, x: int, y: int, nx_cells: int, ny_cells: int) -> int:
    return int(
        game_state[(x - 1) % nx_cells, (y - 1) % ny_cells]
        + game_state[(x) % nx_cells, (y - 1) % ny_cells]
        + game_state[(x + 1) % nx_cells, (y - 1) % ny_cells]
        + game_state[(x - 1) % nx_cells, (y) % ny_cells]
        + game_state[(x + 1) % nx_cells, (y) % ny_cells]
        + game_state[(x - 1) % nx_cells, (y + 1) % ny_cells]
        + game_state[(x) % nx_cells, (y + 1) % ny_cells]
        + game_state[(x + 1) % nx_cells, (y + 1) % ny_cells]
    )


def next_state(current_state: np.ndarray, paused: bool, nx_cells: int, ny_cells: int) -> np.ndarray:
    new_state = np.copy(current_state)

    if paused:
        return new_state

    for y in range(ny_cells):
        for x in range(nx_cells):
            neighbors = count_neighbors(current_state, x, y, nx_cells, ny_cells)

            if current_state[x, y] == 0 and neighbors == 3:
                new_state[x, y] = 1
            elif current_state[x, y] == 1 and (neighbors < 2 or neighbors > 3):
                new_state[x, y] = 0

    return new_state
