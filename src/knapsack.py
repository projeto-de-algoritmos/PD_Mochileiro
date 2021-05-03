

def knapsack(weightArray, valueArray, limitWeight, sizeArray, auxMatrix):
    recursiveMatrix = auxMatrix

    if sizeArray == 0 or limitWeight == 0:
        return 0
    if recursiveMatrix[sizeArray][limitWeight] != -1:
        return recursiveMatrix[sizeArray][limitWeight]
 
    if weightArray[sizeArray - 1] <= limitWeight:
        recursiveMatrix[sizeArray][limitWeight] = max(valueArray[sizeArray-1] + 
            knapsack(
                weightArray, 
                valueArray, 
                limitWeight - weightArray[sizeArray-1],
                sizeArray-1,
                recursiveMatrix),
            knapsack(
                weightArray, 
                valueArray, 
                limitWeight, 
                sizeArray - 1,
                recursiveMatrix))
        return recursiveMatrix[sizeArray][limitWeight]
    
    elif weightArray[sizeArray-1] > limitWeight:
        recursiveMatrix[sizeArray][limitWeight] = knapsack(weightArray, valueArray, limitWeight, sizeArray - 1, recursiveMatrix)
        return recursiveMatrix[sizeArray][limitWeight]

def initMatrix(limitWeight, sizeArray):
    matrix = [[-1 for i in range(limitWeight + 1)] for j in range(sizeArray + 1)]
    return matrix
