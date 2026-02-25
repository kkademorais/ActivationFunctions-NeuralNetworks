import math, CalculateNeuronValue

"""
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
"""

def sigmoidFunction(neuronValue: float) -> float:
    exponencial = math.exp(neuronValue * -1)
    output = 1 / (1 + exponencial)
    return output


def neuralNetwork():
    numberOfInputs = int(input("Digite quantos inputs você deseja inserir na RN: "))

    inputVector = []
    for n in range(0, numberOfInputs):
        inputValue = float(input("Digite o valor que deseja inserir no vetor de entrada: "))
        inputVector.append(inputValue)

    weightsVector = []
    for n in range(0, numberOfInputs):
        inputWeights = float(input("Agora digite o valor para o vetor de pesos: "))
        weightsVector.append(inputWeights)

    bias = float(input("Digite um valor para o bias: "))

    print("\n")
    print("Printando o vetor de inputs: ")
    print(inputVector)
    print("\n")
    print("Printando o vetor de peso: ")
    print(weightsVector)
    print("\n")
    print("Bias: ", bias)
    print("\n")

    neuronValue = CalculateNeuronValue.calculateNeuronValue(inputVector, weightsVector, bias)
    print(f"Calculando valor do neuron unit a partir do vetor de input, os pesos e o bias: {neuronValue:.3f}")
    print("\n")

    print(f"Calculando utilizando Sigmoid: {sigmoidFunction(neuronValue):.3f}")


if __name__ == '__main__':
    neuralNetwork()
