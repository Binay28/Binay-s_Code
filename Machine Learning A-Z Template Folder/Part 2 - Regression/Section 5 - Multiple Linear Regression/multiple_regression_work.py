#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 14:19:06 2018

@author: beneragon
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#importing dataset
dataset=pd.read_csv('50_Startups.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,4].values
#taking care of missing data
'''from sklearn.preprocessing import Imputer
Imput=Imputer(missing_values="NaN",strategy='most_frequent',axis=0)
Imput=Imput.fit(X[:,1:3])
X[:,1:3]=Imput.transform(X[:,1:3])'''
#encoding categorial data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,3]=labelencoder_X.fit_transform(X[:,3])
ohe=OneHotEncoder(categorical_features=[3])
X=ohe.fit_transform(X).toarray()
#avoiding the Dummy variable trap
X=X[:,1:]
#splitting the dataset
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
#feature Scaling
'''from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)'''
#fitting multiple linear regression
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)
#predicting the Test set result
Y_pred=regressor.predict(X_test)
#building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
X=np.append(arr=np.ones((50,1)).astype(int),values=X,axis=1)
X_opt=X[:,[0,1,2,3,4,5]]
regressor_OLS=sm.OLS(endog=Y,exog=X_opt).fit()
regressor_OLS.summary()