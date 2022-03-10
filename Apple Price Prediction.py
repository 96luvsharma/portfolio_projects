import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')



#Get the stock quote,

df = web.DataReader('AAPL',data_source = 'yahoo', start='2015-01-01', end='2022-01-01')

print(df.shape)

# plt.figure(figsize=(16,8))
# plt.title('Close Price History')
# plt.plot(df['Close'])
# plt.xlabel('Date',fontsize =18)
# plt.ylabel('Close Price USD($)',fontsize = 18)
# plt.show()

#Create a new dataframe with the Close Column.

data =df.filter(['Close'])

#Convert the dataframe to numpy array 

dataset = data.values

#Getting the number of rows to train the model

training_data_len = math.ceil(len(dataset) * 0.8)

print(training_data_len)


#Scale the data 

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)

#Create the training data set

#Creating the scaled data set

train_data = scaled_data[0:training_data_len,:]

#Split the data into x_train and y_train data set

x_train = []
y_train = []

for i in range(60,len(train_data)):
    x_train.append(train_data[i-60:i,0])
    y_train.append(train_data[i,0])
    if i<=61:
        print(x_train)
        print(y_train)
        print()
        
#Convert X & Y train to numpy array to use LSTM Model.

x_train, y_train = np.array(x_train), np.array(y_train)

#Reshape the data as LSTM expects the data to be in 3-Dimensions
# numper of samples, number of timesteps, and number of features, while right now it is 2-Dimensional

    
x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))

# print(x_train.shape)

#Building the LSTM Model

model = Sequential()
model.add(LSTM(200, return_sequences=True, input_shape=(x_train.shape[1],1)))
model.add(LSTM(200,return_sequences=False ))
model.add(Dense(50))
model.add(Dense(1))


#Compile the model
model.compile(optimizer='adam',loss = 'mean_squared_error')

#training the model

model.fit(x_train,y_train,batch_size=1,epochs=10)    #fit a method to train the model.

#Create the testing dataset

#Create a new array containing scaled values from index 1351 to the end of the data set

test_data = scaled_data[training_data_len - 60:, :]

x_test = []
y_test = dataset[training_data_len:, :]

for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i,0])

#Convert the data again to a numpy array 

x_test = np.array(x_test)

#Reshape again to use in the LSTM Model again for 3D inputs.

x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# x_test.shape[0] -> number of rows we have, x_test.shape[1] -> number of rows

#Get the models predicted price values
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

#Get the Root Mean Squared Error (RMSE) - tells the accuracy of the model, using standard deviation,
# a lower value means a better fit.
# a value of zero would mean the prediction is perfect.

rmse = np.sqrt(np.mean(predictions-y_test)**2)
print(rmse) 

#Plot the data 
train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions

#visualize the data

plt.figure(figsize=(16,8))
plt.title('LSTM Model Prediction (AAPL)')
plt.xlabel('Date',fontsize=18)
plt.ylabel('Close Price USD($)',fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close','Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.show()