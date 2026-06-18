import time

import numpy as np
import pygame

from . import config as st
from .game_logic import next_state
from .render import draw_state


def run() -> None:
    pygame.init()

    screen = pygame.display.set_mode((st.width, st.height))
    screen.fill(st.bg)
    pygame.display.set_caption("La Vida")

    nxC, nyC = st.nxC, st.nyC

    gameState = np.zeros((nxC, nyC))

    dimCW = st.width / nxC
    dimCH = st.height / nyC

    gameState = st.generateGameState(gameState)

    pauseExect = False

    while True:
        time.sleep(0.1)

        screen.fill(st.bg)

        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                pauseExect = not pauseExect

        newGameState = next_state(gameState, pauseExect, nxC, nyC)

        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            if 0 <= celX < nxC and 0 <= celY < nyC:
                newGameState[celX, celY] = 1

        draw_state(screen, newGameState, nxC, nyC, dimCW, dimCH)

        gameState = np.copy(newGameState)

        pygame.display.flip()
