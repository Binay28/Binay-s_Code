#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 16:55:51 2018

@author: beneragon
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#importing dataset
dataset=pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:,1:2].values
Y=dataset.iloc[:,2].values
#taking care of missing data
'''from sklearn.preprocessing import Imputer
Imput=Imputer(missing_values="NaN",strategy='most_frequent',axis=0)
Imput=Imput.fit(X[:,1:3])
X[:,1:3]=Imput.transform(X[:,1:3])'''
#encoding categorial data
'''from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
ohe=OneHotEncoder(categorical_features=[0])
X=ohe.fit_transform(X).toarray()
labelencoder_Y=LabelEncoder()
Y=labelencoder_Y.fit_transform(Y)'''
#splitting the dataset
'''from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)'''
#feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
sc_Y=StandardScaler()
X=sc_X.fit_transform(X)
Y=sc_Y.fit_transform(X)
#creating the regressor
from sklearn.svm import SVR
regressor=SVR(kernel='rbf')
regressor.fit(X,Y)
#predicting the result
Y_predict=sc_Y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))
#visualising the result
plt.scatter(X,Y,color='red')
plt.plot(X,regressor.predict(X),color='blue')
plt.title('Truth or Bluff(SVR)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()