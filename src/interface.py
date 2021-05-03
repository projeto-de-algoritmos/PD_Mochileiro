from enum import Enum
from modules.pygame_textinput import TextInput
import pygame

class Level(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class Color(Enum):
    BLACK = (0,0,0)
    WHITE = (255, 255, 255)

class Display:
    def __init__(self):
        self.height = 500
        self.width = 500
        self.screen = None
        self.clock = None

    def initDisplay(self):
        pygame.init()

        windowSize = (self.height, self.width)
        self.screen = pygame.display.set_mode(windowSize)
        pygame.display.set_caption("O Mochileiro")
        self.clock = pygame.time.Clock()
        self.screen.fill(Color.BLACK.value)

    def drawElements(self, elements, posX, posY):
        pygame.font.init()

        text = str(elements)
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(text, True, Color.WHITE.value)
        self.screen.blit(text, (posX, posY))

    def writeOnDisplay(self, textInput: TextInput(), events):
        textInput.update(events)
        self.screen.blit(textInput.get_surface(), (0, 120))