### MODELING -> RANDOM FOREST

#IMPORTS
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import mean_squared_error

#GET DATA
df_dummie = pd.read_csv('df_dummie.csv')
df_dummie.drop(columns=['Unnamed: 0'],inplace=True)

# define X and y
X= df_dummie.drop(columns='Price', axis=1 )
y = df_dummie['Price']


#TEST TRAIN SPLIT
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 0)


##RANDOM FOREST REGRESSOR!
#import
from sklearn.ensemble import RandomForestRegressor
#fit
forest = RandomForestRegressor(random_state = 0).fit(X_train, y_train)
#predict
y_pred = forest.predict(X_test)
print('with the training data', forest.score(X_train, y_train))
print('with the test data', forest.score(X_test,y_test))
# The score was 55% for the test data and 86 for the trained -> overfitting

## LETS TRY HYPERPARAMETER TUNNUNG!!!

# Lets start with RandomizedSearchCV but to use it we need  to create a parameter grid to sample from during fitting 

from sklearn.model_selection import RandomizedSearchCV


#CREATE THE GRID
#n_estimators = Number of trees in random forest
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

#RANDOM SEARCH TRAINING

forest_random = RandomizedSearchCV(estimator = forest, param_distributions = grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)

forest_random.fit(X_train, y_train)
#We can view the best parameters from fitting the random search:
forest_random.best_params_

#compare the base model with the best random search model

def evaluate(model, xx, yy):
    predictions = model.predict(xx)
    errors = abs(predictions - yy)
    mape = 100 * np.mean(errors / yy)
    accuracy = 100 - mape
    print('Model Performance')
    print('Average Error: {:0.4f} degrees.'.format(np.mean(errors)))
    print('Accuracy = {:0.2f}%.'.format(accuracy))
    
    return accuracy

base_model = RandomForestRegressor(n_estimators = 10, random_state = 42)
base_model.fit(X_train, y_train)
base_accuracy = evaluate(base_model, X_test, y_test)

best_random = forest_random.best_estimator_
random_accuracy = evaluate(best_random, X_test, y_test)

#### PICKLE MY MODEL
import pickle

stand_virtual = 'finalized_model.sav'
pickle.dump(best_random, open(stand_virtual, 'wb'))

##########


print('Improvement of {:0.2f}%.'.format( 100 * (random_accuracy - base_accuracy) / base_accuracy))
print(random_accuracy) #74 test #81 train
print(base_accuracy) #80 test #91 train

#I think now I have an accurancy of 74???

from sklearn.model_selection import GridSearchCV

param_grid = {'max_depth': [10, 15, 20, 25],
              'max_features': ['auto', 'sqrt'],
              'n_estimators': [100, 500, 1000, 1500]}



rf = RandomForestRegressor()
grid_search = GridSearchCV(estimator = rf, param_grid = param_grid, 
                          cv = 3, n_jobs = -1, verbose = 2)

grid_search.fit(X_train, y_train)

grid_search.best_params_
best_grid = grid_search.best_estimator_
grid_accuracy = evaluate(best_grid, X_test, y_test)

# best result so far 75.56% and training 86%

y_pred = grid_search.predict(X_test)
mse = mean_squared_error(y_test, y_pred)



##################### LOADING PICKLE MODEL
loaded_model = pickle.load(open(stand_virtual, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)