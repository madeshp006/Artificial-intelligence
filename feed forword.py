import random
import math
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
def init_weights(rows, cols):
    return [[random.uniform(-1, 1) for _ in range(cols)] for _ in range(rows)]
X = [[0,0], [0,1], [1,0], [1,1]]
y = [[0], [1], [1], [0]]
input_nodes = 2
hidden_nodes = 2
output_nodes = 1
learning_rate = 0.5
epochs = 10000
w1 = init_weights(input_nodes, hidden_nodes)
w2 = init_weights(hidden_nodes, output_nodes)
for epoch in range(epochs):
    for i in range(len(X)):
        input_layer = X[i]
        hidden_input = [sum(input_layer[k] * w1[k][j] for k in range(input_nodes)) for j in range(hidden_nodes)]
        hidden_output = [sigmoid(x) for x in hidden_input]
        final_input = [sum(hidden_output[k] * w2[k][j] for k in range(hidden_nodes)) for j in range(output_nodes)]
        final_output = [sigmoid(x) for x in final_input]
        error = [y[i][j] - final_output[j] for j in range(output_nodes)]
        d_output = [error[j] * sigmoid_derivative(final_output[j]) for j in range(output_nodes)]
        for j in range(hidden_nodes):
            for k in range(output_nodes):
                w2[j][k] += learning_rate * d_output[k] * hidden_output[j]
        error_hidden = [sum(d_output[k] * w2[j][k] for k in range(output_nodes)) for j in range(hidden_nodes)]
        d_hidden = [error_hidden[j] * sigmoid_derivative(hidden_output[j]) for j in range(hidden_nodes)]
        for j in range(input_nodes):
            for k in range(hidden_nodes):
                w1[j][k] += learning_rate * d_hidden[k] * input_layer[j]
print("\nTrained XOR Neural Network (No Libraries):")
for x in X:
    hidden = [sigmoid(sum(x[k] * w1[k][j] for k in range(input_nodes))) for j in range(hidden_nodes)]
    output = [sigmoid(sum(hidden[k] * w2[k][j] for k in range(hidden_nodes))) for j in range(output_nodes)]
    print(f"Input: {x} -> Output: {round(output[0], 3)}")
