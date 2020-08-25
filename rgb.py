# now trying 
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import make_scorer, accuracy_score

#conda install xgboost
##Test train split


df_dummie = pd.read_csv('df_dummie.csv')
df_dummie.drop(columns=['Unnamed: 0'],inplace=True)

# define X and y
X= df_dummie.drop(columns='Price', axis=1 )
y = df_dummie['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 0)



# initialize the model
model = XGBRegressor(verbosity=0) 
# fit the model
model.fit(X_train, y_train)

score = model.score(X_train, y_train)  
print("Training score: ", score)

# The training gives me an impressive 99%

y_pred = model.predict(X_test)

