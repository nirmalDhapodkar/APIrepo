import pandas as pd
import timeconv as tc
import matplotlib.pyplot as plt
import numpy as np
import datetime
import pickle
import joblib
from sklearn.tree import DecisionTreeRegressor


def mktimestmp():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%H:%M')
    month =  current_time.month
    arr = np.array([month ,formatted_time])  # Initialize array with formatted_time
    for i in range(0, 1):
        tmp = arr[-1]
        tmp = tc.time_to_minutes(tmp)
        tmp += 10
        tmp = tc.minutes_to_time(tmp)
        arr = np.append(arr, tmp)  # Append tmp to arr
    return arr


def fmttimestmp(arr):
    tmp = arr
    tmp[1] = tc.time_to_minutes(tmp[1])
    tmp[2] = tc.time_to_minutes(tmp[2])
    return tmp


def generate_jdict():
    t_stamp = mktimestmp()
    st = t_stamp[1]
    ft = t_stamp[2]
    t_stamp = fmttimestmp(t_stamp)
    y_pred = model.predict([t_stamp])
    y_pred = y_pred[0]
    ndict = {'StartTime' : st, 'FinishTime' : ft, 'Predicted' : y_pred}
    return ndict

if __name__ == "__main__":
    dataset = pd.read_csv('dtdata1.csv')

    x = dataset[['Month', 'StTime', 'FinTime']].values
    # x = [tc.time_to_minutes(i) for i in series]
    # print('x : ',x)
    y = dataset['Consumption'].values
    # print('y : ',y)

    #Creating model and train it
    model = DecisionTreeRegressor()
    model.fit(x, y)

    #Saving Model for again use
    joblib.dump(model, 'learn_model.pkl')
