import math, CalculateNeuronValue

def tanh(neuronValue: float) -> float:
    output = (math.exp(neuronValue) - math.exp(neuronValue * -1))/(math.exp(neuronValue) + math.exp(neuronValue * -1))
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

    print(f"Calculando utilizando Tangente Hiperbólica: {tanh(neuronValue):.3f}")


if __name__ == '__main__':
    neuralNetwork()
