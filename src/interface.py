from enum import Enum
import pygame

class Level(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class Color(Enum):
    BLACK = (20,20,20)
    WHITE = (0, 0, 0)

class Display:
    def __init__(self):
        self.height = 500
        self.width = 500
        self.background = None
        self.screen = None

    def initDisplay(self):
        pygame.init()

        windowSize = (self.height, self.width)
        self.screen = pygame.display.set_mode(windowSize)
        pygame.display.set_caption("O Mochileiro")
        clock = pygame.time.Clock()

        self.background = pygame.Surface.fill(self.screen, Color.BLACK.value)

    def drawElements(self, elements):
        pygame.font.init()
        

        text = str(elements)
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(text, True, Color.WHITE.value)
        self.screen.blit(text, (0, 0))