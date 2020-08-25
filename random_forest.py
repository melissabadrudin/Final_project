import pandas as pd
from sklearn.model_selection import train_test_split

df_dummie = pd.read_csv('df_dummie.csv')
df_dummie.drop(columns=['Unnamed: 0'],inplace=True)


##Test train split

# define X and y
X= df_dummie.drop(columns='Price', axis=1 )
y = df_dummie['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 0)


from sklearn.ensemble import RandomForestRegressor

forest = RandomForestRegressor(random_state = 0).fit(X_train, y_train)

y_pred = forest.predict(X_test)
print('with the training data', forest.score(X_train, y_train))
print('with the test data', forest.score(X_test,y_test))

#Now lets try with hyperparameters:

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

# Number of trees in random forest
n_estimators = [100,500,1000,1500]

# Number of features to consider at every split
max_features = ['auto', 'sqrt']

# Maximum number of levels in each tree
max_depth = [10,15,20,25]

# Create the  grid
grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth
               }

# estimator
forest = RandomForestRegressor()

grid_forest = GridSearchCV(estimator = forest, param_grid = grid, cv = 3)

# Fit the grid search to the data
grid_forest.fit(X_train, y_train)

#grid_forest.best_params_

# in the grid search you know for sure, that he tested all the combinations you gave him

grid_forest.score(X_test, y_test)
grid_forest.score(X_train, y_train)

#predictions: test data
y_pred = grid_forest.predict(X_test)
probs = grid_forest.predict_proba(X_test)
print(probs)
# compare predictions to actual answers
print('Confusion matrix')
print(confusion_matrix(y_pred,y_test))
print('-------------------------------------------------------')
# accuracy_score
# fitted X_test data vs. y_test data (actual answer)
print('Accuracy score')
print(accuracy_score(y_pred,y_test))
print('-------------------------------------------------------')
# classification report
print('Classification report')
print(classification_report(y_pred,y_test))
