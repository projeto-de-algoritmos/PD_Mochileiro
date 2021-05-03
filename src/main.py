from item import Item
from knapsack import knapsack, initMatrix
from interface import *
import random as rnd
import pygame


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

    return weightArray, valueArray, result


if __name__ == "__main__":

    display = Display()
    running = True
    weightArray, valueArray, result = backgroundKnapsack()

    while running:
        display.initDisplay()
        display.drawElements(weightArray)

        pygame.display.flip()