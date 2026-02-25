def dotProduct(inputVector: [float], weightVector: [float]) -> [float]:
    inputVectorWeighted = []
    for n in range(0, len(inputVector)):
        inputVectorWeighted.append(inputVector[n] * weightVector[n])
    return inputVectorWeighted


def calculateNeuronValue(inputVector: [float], weightVector: [float], bias: float) -> float:
    inputVectorWeighted = dotProduct(inputVector, weightVector)
    neuronValue = bias
    for n in range(0, len(inputVectorWeighted)):
        neuronValue += inputVectorWeighted[n]
    return neuronValue