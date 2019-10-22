# -*- coding: utf-8 -*-
#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#importing dataset
dataset=pd.read_csv('Data.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,3].values
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
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)
#feature Scaling
'''from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)'''