# -*- coding: utf-8 -*-
"""Banknote_Authentication.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b8tDVBRRNjLUhbxOFyiEQoYstuPAtQp_
"""

import pandas as pd
import numpy as np

df=pd.read_csv('BankNote_Authentication.csv')

df

#independent & dependent features
X=df.iloc[:,:-1]
y=df.iloc[:,-1]

X.head()

y.head(20)

#train test split
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

#implement rnadom forest classifier 
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train,y_train)

#prediction
y_pred=classifier.predict(X_test)

#check Accuracy
from sklearn.metrics import accuracy_score
score =accuracy_score(y_test,y_pred)

score

#creating a picke file using serialization
import pickle
pickle_out=open("classifier.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()

import numpy as np

classifier.predict([[2,3,4,1]])

