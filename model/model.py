import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


dataset = pd.read_csv('house_prices.csv')

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)


regressor = LinearRegression()
regressor.fit(x_train, y_train)


with open('model.pkl', 'wb') as file:
    pickle.dump(regressor, file)

print("model saved")


