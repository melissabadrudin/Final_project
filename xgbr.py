###### Tutuorial XGBR


#IMPORTS

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

#DATA

df_dummie = pd.read_csv('df_dummie.csv')
df_dummie.drop(columns=['Unnamed: 0'],inplace=True)

#Separate data into X and Y Parts

X= df_dummie.drop(columns='Price', axis=1 )
y = df_dummie['Price']

#split 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 0)

xgbr= XGBRegressor(verbosity =0)

print(xgbr)

xgbr.fit(X_train,y_train)
score = xgbr.score(X_train,y_train)
score2= xgbr.score(X_test,y_test)
print('Training score is:' + str(score))
print('Test score is:' + str(score2))
cv_score= cross_val_score(xgbr,X_train,y_train, cv=10)
print (cv_score.mean())

y_pred = xgbr.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("MSE: %.2f" % mse)
print("RMSE: %.2f" % mse**(0.5))

x_ax = range(len(y_test))
plt.scatter(x_ax, y_test, s=5, color="blue", label="original")
plt.plot(x_ax, y_pred, lw=0.8, color="red", label="predicted")
plt.legend()
plt.show()