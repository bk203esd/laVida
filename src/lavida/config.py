from .patterns import seed_game_state

width, height = 400, 400
bg = 25, 25, 25

nxC, nyC = 60, 60


def generateGameState(gameState):
    return seed_game_state(gameState)
