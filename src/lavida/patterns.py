import numpy as np


def seed_game_state(game_state: np.ndarray) -> np.ndarray:
    # Oscillator 1
    game_state[38, 20] = 1
    game_state[39, 20] = 1
    game_state[40, 20] = 1

    # Oscillator 2
    game_state[10, 10] = 1
    game_state[11, 10] = 1
    game_state[12, 10] = 1
    game_state[10, 11] = 1
    game_state[11, 11] = 1
    game_state[12, 11] = 1

    # Runner 1
    game_state[10, 5] = 1
    game_state[12, 5] = 1
    game_state[11, 6] = 1
    game_state[12, 6] = 1
    game_state[11, 7] = 1

    # Runner 2
    game_state[20, 5] = 1
    game_state[22, 5] = 1
    game_state[21, 6] = 1
    game_state[22, 6] = 1
    game_state[21, 7] = 1

    # Box 1
    game_state[18, 15] = 1
    game_state[17, 16] = 1
    game_state[17, 15] = 1
    game_state[18, 16] = 1

    # Serpent 1
    game_state[30, 20] = 1
    game_state[31, 20] = 1
    game_state[32, 20] = 1
    game_state[32, 19] = 1
    game_state[33, 19] = 1
    game_state[34, 19] = 1

    # Frog 1
    game_state[50, 20] = 1
    game_state[51, 20] = 1
    game_state[52, 20] = 1

    return game_state
