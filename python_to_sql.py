###### Import my csv file with the dataset

import pandas as pd

df = pd.read_csv('/Users/melissabadrudin/Documents/GitHub/Final_project/stand_df.csv')


###### Pass the dataset to mySQL
#conda install pymysql

#import the module
from sqlalchemy import create_engine

# create sqlalchemy engine
engine =create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="descobri93",
                               db="stand_virtual"))

# pass the data in one line code to sql:
df.to_sql('dataset', con = engine, if_exists = "append")


print("Done")

#it worked! 