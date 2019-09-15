import numpy as np
from matplotlib import pyplot as plt
from numpy import linalg as la
import random as rand
from io import StringIO
import csv
import pandas as pd
from sklearn.model_selection import train_test_split #This packet splits the data set into training and testing 
                                                     #dataset with stratified partionong keeping the ratio of both 
                                                     #the dataset constant 
from sklearn import preprocessing

def WeatherDataExtract():
    dataArray = pd.read_csv("test.csv", delimiter=",", header=None)
    Data_Y = dataArray.iloc[0:1055, 41]                    #labels
    Data_X = dataArray.iloc[0:1055, 0:41]                  #features
	print(Data_X)
	print(Data_Y)
    # make col 41 values numerical
    Data_Y = np.where(Data_Y == "RB", 1, -1)
    return Data_X, Data_Y
