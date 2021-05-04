from enum import Enum
from modules.pygame_textinput import TextInput
import pygame
import time
import sys

class Color(Enum):
    BLACK = (0,0,0)
    WHITE = (255, 255, 255)

class Display:
    def __init__(self):
        self.height = 500
        self.width = 500
        self.screen = None

    def initDisplay(self):
        pygame.init()

        windowSize = (self.height, self.width)
        self.screen = pygame.display.set_mode(windowSize)
        pygame.display.set_caption("O Mochileiro")
        self.screen.fill(Color.BLACK.value)

    def drawElements(self, elements, posX, posY, condition):
        pygame.font.init()

        text = str(elements)
        textSize = sys.getsizeof(text)
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(text, False, Color.WHITE.value)
        self.screen.blit(text, (posX, posY))
        pygame.display.update()

        if condition:
            time.sleep(1)
            self.screen.fill(pygame.Color("black"), (posX, posY, textSize*5, 35))

        pygame.display.update()

    def writeOnDisplay(self, textInput: TextInput(), events, condition):
        textInput.update(events)
        self.screen.blit(textInput.get_surface(), (0, 120))

        if condition:
            time.sleep(1)
            self.screen.fill(pygame.Color("black"), (0, 120, 500, 35))
        pygame.display.update()
