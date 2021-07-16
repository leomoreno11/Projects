# This script pretends to analyse the previous prices from cryptocurrencies and predict 
# what the next price will be
# The value will be shown in US Dolar (USD) with plans to convert it to Brazillian Real (BRL)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

crypto = 'BTC' #Informs what crypto you are interested in
real_currency = 'USD' #Real world currency for comparison

start_time = dt.datetime(2016,1,1)
end_time = dt.datetime.now()

#Collects the data from the Yahoo finance API
data = web.DataReader(f'{crypto}-{real_currency}', 'yahoo', start_time, end_time)

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))

prediction_days = 120
x_train, y_train = [], []

#Organizes the data and prepares it for the ML model
for x in range(prediction_days, len(scaled_data)):
    x_train.append(scaled_data[x - prediction_days:x, 0])
    y_train.append(scaled_data[x, 0])

x_train, ytrain = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1]))

#Building the Neural Network
#provalvemnte instalar numpy 1.19.5

model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.Dense(units=1)

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, epochs=25, batch_size=32)