from item import Item
from knapsack import knapsack, initMatrix
from modules.pygame_textinput import TextInput
from interface import *
import random as rnd
import pygame
import time



def backgroundKnapsack(level):
    rand_level = level * 2
    items = []

    limitWeight = rnd.randint(10 + rand_level, 30 + rand_level)
    sizeArray = rnd.randint(5 + rand_level, 10 + rand_level)

    matrix = initMatrix(limitWeight, sizeArray)

    count = 0
    while(count < sizeArray):
        item = Item()

        item.setName(count)
        item.setValue(rnd.randint(1, 30))
        item.setWeight(rnd.randint(1, 10))
        items.append(item)

        count = count+1


    weightArray = []
    valueArray = []
    for item in items:
        weightArray.append(item.weight)
        valueArray.append(item.value)

    result = knapsack(weightArray, valueArray, limitWeight, sizeArray, matrix)

    return weightArray, valueArray, limitWeight, sizeArray, result


if __name__ == "__main__":
    global FPSCLOCK
    FPSCLOCK=pygame.time.Clock()
    display = Display()
    display.initDisplay()
    textInput = TextInput()
    gameExit = True
    retry = 3
    level = 0
    weightArray, valueArray, limitWeight, sizeArray, result = backgroundKnapsack(level)

    while gameExit:
        condition = 0
        flushValues = 0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                gameExit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    response = int(textInput.get_text())
                    if (response != result):
                        display.drawElements("Resposta errada, tente novamente", 0, 140, 1)
                        retry = retry - 1
                        textInput.clear_text()
                        pygame.display.update()
                        condition = 1
                    else:
                        level = level + 1
                        weightArray, valueArray, limitWeight, sizeArray, result = backgroundKnapsack(level)
                        display.drawElements("Parabéns você acertou!", 0, 140, 1)
                        textInput.clear_text()
                        pygame.display.update()
                        flushValues = 1
                        condition = 1

        if retry < 1:
            display.drawElements("Você perdeu =(", 0, 160, 1)
            gameExit = False

        display.drawElements("Limite da mochila: " + str(limitWeight), 0, 0, flushValues)
        display.drawElements("Quantidade de itens: " + str(sizeArray), 0, 20, flushValues)
        display.drawElements("Pesos: " + str(weightArray), 0, 60, flushValues)
        display.drawElements("Valores: " + str(valueArray), 0, 80, flushValues)
        display.drawElements("Digite o valor de resposta: ", 0, 100, 0)
        display.writeOnDisplay(textInput, events, condition)

        pygame.display.flip()
        pygame.display.update()

        FPSCLOCK.tick_busy_loop(60)

    time.sleep(1)
    pygame.quit()