
### Lets Get Modeling!!!!

#import libraries
from sklearn.model_selection import train_test_split
import pandas as pd

#import df
df_dummie = pd.read_csv('df_dummie.csv')
df_dummie.drop(columns=['Unnamed: 0'],inplace=True)


##Test train split

# define X and y
X= df_dummie.drop(columns='Price', axis=1 )
y = df_dummie['Price']


#1 Model -> Nearest Neighbors

#import the model
from sklearn.neighbors import KNeighborsRegressor
knnr = KNeighborsRegressor(n_neighbors = 500)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 0)

model = knnr.fit(X_train, y_train)  #fit the model
y_pred = knnr.predict(X_test)

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

#this is rubish tbh.
#new game plan: try random forest and if it doesn't work try classification and then regression for each classification. 
