from item import Item
from knapsack import knapsack, initMatrix
from modules.pygame_textinput import TextInput
from interface import *
import random as rnd
import pygame
import time



def backgroundKnapsack():
    items = []

    limitWeight = rnd.randint(10, 30)
    sizeArray = rnd.randint(5, 10)

    matrix = initMatrix(limitWeight, sizeArray)

    count = 0
    while(count < sizeArray):
        item = Item()

        item.setName(count)
        item.setValue(rnd.randint(10, 30))
        item.setWeight(rnd.randint(5, 10))
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

    display = Display()
    display.initDisplay()
    textInput = TextInput()
    gameExit = True
    retry = 3
    weightArray, valueArray, limitWeight, sizeArray, result = backgroundKnapsack()

    while gameExit:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                gameExit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    response = int(textInput.get_text())
                    if (response != result):
                        display.drawElements("Resposta errada, tente novamente", 0, 140)
                        retry = retry - 1
                    else:
                        display.drawElements("Parabéns você acertou!", 0, 140)

        if retry < 1:
            display.drawElements("Você perdeu =(", 0, 160)
            gameExit = False
        display.drawElements("Limite da mochila: " + str(limitWeight), 0, 0)
        display.drawElements("Quantidade de itens: " + str(sizeArray), 0, 20)
        display.drawElements("Pesos: " + str(weightArray), 0, 60)
        display.drawElements("Valores: " + str(valueArray), 0, 80)
        display.drawElements("Digite o valor de resposta: ", 0, 100)
        display.writeOnDisplay(textInput, events)

        pygame.display.update()
        display.clock.tick(30)

    time.sleep(1)
    pygame.quit()