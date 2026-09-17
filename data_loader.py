import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

class DataLoader:
    def __init__(self):
        self.california = fetch_california_housing()

    def get_train_test_data(self):
        df = pd.DataFrame(self.california.data, columns=self.california.feature_names)
        df['Price'] = self.california.target
        X = df.drop('Price', axis=1)
        y = df['Price']
        return train_test_split(X, y, test_size=0.2, random_state=42)