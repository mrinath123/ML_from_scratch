import numpy as np

class Linear_reg:
    def __init__(self , learning_rate = 0.001 , epochs = 10000):
        self.lr = learning_rate
        self.e = epochs
        self.weights = None
        self.bias = None
    def train(self,X, y):
        n_samples , n_feats = X.shape
        self.weights = 0.01 *np.random.randn(1,n_feats)
        self.bias = 0.

        for epoch in range(self.e):
            y_pred = X*self.weights + self.bias
            loss = 1/(len(y))*(np.sum(y_pred - y)**2)

            dW = 1/(len(y))* (np.sum(X*(y_pred - y)))
            db = 1/(len(y))* (np.sum(y_pred - y))

            self.weights -= self.lr*dW
            self.bias -= self.lr*db

            if(epoch % 1000 ==0 or epoch == self.e):
                print(f' epoch {epoch} training loss {loss}')
    
    def predict(self,X):
        y_pred = X*self.weights + self.bias
        return y_pred
    
    def get_parameters(self):
        return self.weights,self.bias









