# Now trying the classification and then smaller regression problems:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.model_selection import GridSearchCV
import time
from sklearn.neighbors import NearestNeighbors
from sklearn.naive_bayes import GaussianNB
from sklearn import neighbors
from sklearn import tree


#import data

data = pd.read_csv('df_dummie.csv')
data.drop(columns=['Unnamed: 0'],inplace=True)

a=data['Price']
for i in range(len(a)):
    if a[i]>=min(a) and a[i]<=5000:
        a[i]=1
    elif a[i]>5000 and a[i]<=10000:
        a[i]=2
    elif a[i]>10000 and a[i]<=15000:
        a[i]=3
    elif a[i]>15000 and a[i]<=20000:
        a[i]=4
    elif a[i]>20000 and a[i]<=25000:
        a[i]=5
    elif a[i]>25000 and a[i]<=30000:
        a[i]=6
    elif a[i]>35000 and a[i]<=40000:
        a[i]=7
    elif a[i]>40000:
        a[i]=8
        
X= data.drop(columns='Price', axis=1 )
y = data['Price']

num_test = 0.20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=num_test, random_state=23)


clf =RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy',
            max_depth=20, max_features='log2', max_leaf_nodes=None,
            min_samples_leaf=2, min_samples_split=4,
            min_weight_fraction_leaf=0.0, n_estimators=9, n_jobs=1,
            oob_score=False, random_state=None, verbose=0,
            warm_start=False)


clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print("RandomForest score: "+str(accuracy_score(y_test, predictions)))




#Previsão utilizando o classifier KNeighbors
clf = neighbors.KNeighborsClassifier(15, weights='distance')
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print("KNeighbors score: "+str(accuracy_score(y_test, predictions)))

#Previsão utilizando o classifier DecisionTree
clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print("DecisionTree score: "+str(accuracy_score(y_test, predictions)))













