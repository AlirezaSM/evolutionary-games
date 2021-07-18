import numpy as np


class NeuralNetwork():

    def __init__(self, layer_sizes):

        # TODO
        # layer_sizes example: [4, 10, 2]
        self.w = [np.random.uniform(-1, 1, size=(layer_sizes[1], layer_sizes[0])),
                  np.random.uniform(-1, 1, size=(layer_sizes[2], layer_sizes[1]))]
        # self.b = [np.zeros((layer_sizes[1], 1)),
        #           np.zeros((layer_sizes[2], 1))]
        self.b = [np.random.uniform(-1, 1, size=(layer_sizes[1], 1)),
                  np.random.uniform(-1, 1, size=(layer_sizes[2], 1))]
        self.a = [np.zeros((layer_sizes[1], 1)),
                  np.zeros((layer_sizes[2], 1))]
        self.z = [np.zeros((layer_sizes[1], 1)),
                  np.zeros((layer_sizes[2], 1))]

        pass

    def activation(self, x):
        
        # TODO
        # Sigmoid function
        x = 1.0/(1.0+np.exp(-x))
        return x

    def forward(self, x):
        # TODO
        # x example: np.array([[0.1], [0.2], [0.3]])
        self.z[0] = np.add(np.matmul(self.w[0], x), self.b[0])
        self.a[0] = self.activation(self.z[0])
        for i in range(1, len(self.a)):
            self.z[i] = np.add(np.matmul(self.w[i], self.a[i - 1]), self.b[i])
            self.a[i] = self.activation(self.z[i])
        # return the output
        return self.a[1]
        # pass
