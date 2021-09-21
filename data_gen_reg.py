import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Generate:
    def __init__(self , no_of_samples):
        self.n = no_of_samples

    def generate(self):
        x = np.array(range(self.n))
        noise = np.random.uniform(-20, 20, size=self.n)
        y = 4.2069*x + noise 
        return x , y
    
    def make_data(self):
        x,y = self.generate()
        x = np.expand_dims(x,axis=1)
        y = np.expand_dims(y,axis=1)
        data =  np.hstack((x,y))
        df = pd.DataFrame(data, columns=["X", "y"])
        return df


        





